from copy_source_to_dir import *
from generate_page import generate_pages_recursively

def main():
    copy_source_to_dir("static", "public")
    generate_pages_recursively("content", "template.html", "public")

if __name__ == "__main__":
    main()
