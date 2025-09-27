
def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No H1 header found")
