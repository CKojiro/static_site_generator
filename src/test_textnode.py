import unittest

from textnode import *
from htmlnode import *
from leafnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_init(self):
        node = TextNode("Text node", TextType.LINK, "https://boot.dev")
        node2 = TextNode("Text node", TextType.LINK, "https://boot.dev")
        self.assertEqual(node, node2)

    def test_type(self):
        node = TextNode("This is a node", TextType.TEXT, "http://boot.dev")
        node2 = TextNode("This is a node", TextType.BOLD, "http://boot.dev")
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("Node", TextType.IMAGE, "https://boot.dev")
        node2 = TextNode("Node", TextType.IMAGE, None)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

if __name__ == "__main__":
    unittest.main()
