import sys

from copy_source_to_dir import *
from generate_page import generate_pages_recursively

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1].rstrip("/") + "/"
    else:
        basepath = "/"
    copy_source_to_dir("static", "docs")
    generate_pages_recursively("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()
