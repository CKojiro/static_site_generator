from htmlnode import *

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            if self.tag == "img":
                return f"<img{self.props_to_html()}>"
            raise ValueError("All leaf nodes must have a value")
        elif self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
