import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        prop1 = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        prop2 = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node1 = HTMLNode("tag", 5, None, prop1)
        node2 = HTMLNode("tag", 5, None, prop2)
        output1 = node1.props_to_html()
        output2 = node2.props_to_html()
        self.assertEqual(output1, output2)

    def test_repr(self):
        output = f"tag = tag\n"
        output += f"value = value\n"
        output += f"children = child\n"
        output += f"props = props"
        node = HTMLNode("tag", "value", "child", "props")
        nodeRep = repr(node)
        self.assertEqual(output, nodeRep)
