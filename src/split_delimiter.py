import re

from enum import Enum
from parentnode import *
from textnode import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")
    if block.startswith("#"):
        parts = block.split(" ", 1)
        if len(parts) > 1 and 1 <= len(parts[0]) <= 6 and all(c == "#" for c in parts[0]):
            return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    if all(line.startswith(f"{i+1}. ") for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            new_nodes.append(node)
            continue
        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    image_pattern = re.compile(r"!\[(.*?)\]\((.*?)\)")
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        last_index = 0
        for match in image_pattern.finditer(text):
            if match.start() > last_index:
                new_nodes.append(TextNode(text[last_index:match.start()], TextType.TEXT))
            alt_text = match.group(1)
            url = match.group(2)
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            last_index = match.end()
        if last_index < len(text):
            new_nodes.append(TextNode(text[last_index:], TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    link_pattern = re.compile(r"\[(.*?)\]\((.*?)\)")
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        last_index = 0
        for match in link_pattern.finditer(text):
            if match.start() > last_index:
                new_nodes.append(TextNode(text[last_index:match.start()], TextType.TEXT))
            anchor_text = match.group(1)
            url = match.group(2)
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            last_index = match.end()
        if last_index < len(text):
            new_nodes.append(TextNode(text[last_index:], TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = [block.strip() for block in blocks if block.strip() != ""]
    return cleaned_blocks

def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            normalized = " ".join(block.split())
            text_nodes = text_to_textnodes(normalized)
            html_children = [text_node_to_html_node(tn) for tn in text_nodes]
            children.append(ParentNode("p", html_children))
        elif block_type == BlockType.HEADING:
            hashes, text = block.split(" ", 1)
            level = len(hashes)
            normalized = " ".join(text.split())
            text_nodes = text_to_textnodes(normalized)
            html_children = [text_node_to_html_node(tn) for tn in text_nodes]
            children.append(ParentNode(f"h{level}", html_children))
        elif block_type == BlockType.CODE:
            code_content = block[3:-3]
            if code_content.startswith("\n"):
                code_content = code_content[1:]
            tn = TextNode(code_content, TextType.CODE)
            code_html = text_node_to_html_node(tn)
            children.append(ParentNode("pre", [code_html]))
        elif block_type == BlockType.QUOTE:
            quote_text = "\n".join(line.lstrip("> ").rstrip() for line in block.splitlines())
            text_nodes = text_to_textnodes(quote_text)
            html_children = [text_node_to_html_node(tn) for tn in text_nodes]
            children.append(ParentNode("blockquote", html_children))
        elif block_type == BlockType.UNORDERED_LIST:
            li_nodes = []
            for line in block.splitlines():
                item_text = line[2:].strip()
                text_nodes = text_to_textnodes(item_text)
                html_children = [text_node_to_html_node(tn) for tn in text_nodes]
                li_nodes.append(ParentNode("li", html_children))
            children.append(ParentNode("ul", li_nodes))
        elif block_type == BlockType.ORDERED_LIST:
            li_nodes = []
            for line in block.splitlines():
                _, item_text = line.split(". ", 1)
                item_text = item_text.strip()
                text_nodes = text_to_textnodes(item_text)
                html_children = [text_node_to_html_node(tn) for tn in text_nodes]
                li_nodes.append(ParentNode("li", html_children))
            children.append(ParentNode("ol", li_nodes))
        else:
            normalized = " ".join(block.split())
            text_nodes = text_to_textnodes(normalized)
            html_children = [text_node_to_html_node(tn) for tn in text_nodes]
            children.append(ParentNode("p", html_children))
    return ParentNode("div", children)

