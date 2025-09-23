
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        output = f""
        for key, value in self.props.items():
            output += f" {key}=\"{value}\""
        return output

    def __repr__(self):
        output = f"tag = {self.tag}\n"
        output += f"value = {self.value}\n"
        output += f"children = {self.children}\n"
        output += f"props = {self.props}"
        return output
