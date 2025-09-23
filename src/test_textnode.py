import unittest

from textnode import TextNode, TextType

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
        node = TextNode("This is a node", TextType.PLAIN, "http://boot.dev")
        node2 = TextNode("This is a node", TextType.BOLD, "http://boot.dev")
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("Node", TextType.IMAGE, "https://boot.dev")
        node2 = TextNode("Node", TextType.IMAGE, None)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
