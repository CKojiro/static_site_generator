import unittest

from leafnode import *

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click here", props={"href": "https://boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://boot.dev">Click here</a>')
