from htmlnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag, value, children, props):
        super().__init__(tag, value, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode has no tag")
        if self.children is None:
            raise ValueError("ParentNode children is missing a value")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}>{children_html}<{self.tag}>"
