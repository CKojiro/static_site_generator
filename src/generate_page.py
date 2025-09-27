import os

from split_delimiter import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    try:
        with open(from_path, "r") as file:
            from_path_contents = file.read()
    except FileNotFoundError:
        print(f"Markdown file not found: {from_path}")
    try:
        with open(template_path, "r") as file:
            template_path_contents = file.read()
    except FileNotFoundError:
        print(f"Template file not found: {template_path}")
    html_string = markdown_to_html_node(from_path_contents).to_html()
    title = extract_title(from_path_contents)
    full_html = template_path_contents.replace("{{ Title }}", title, 1)
    full_html = full_html.replace("{{ Content }}", html_string, 1)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as html_file:
        html_file.write(full_html)

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)
        if os.path.isdir(entry_path):
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursively(entry_path, template_path, dest_path)
        elif entry.endswith(".md"):
            name_without_ext = os.path.splitext(entry)[0]
            if entry == "index.md":
                dest_file_path = os.path.join(dest_dir_path, "index.html")
            else:
                dest_subdir = os.path.join(dest_dir_path, name_without_ext)
                os.makedirs(dest_subdir, exist_ok=True)
                dest_file_path = os.path.join(dest_subdir, "index.html")
            generate_page(entry_path, template_path, dest_file_path)
