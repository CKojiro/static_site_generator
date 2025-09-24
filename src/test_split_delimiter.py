import unittest

from textnode import *
from split_delimiter import *

class TestSplitDelimiter(unittest.TestCase):
    def test_split_delimiter(self):
        node = TextNode("This is text with **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        same_nodes = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, same_nodes)

    def test_extract_markdown_images1(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images2(self):
        matches = extract_markdown_images("This is text with a ![meme](https://i.imgur.com/aKaOqIh.gif)")
        self.assertEqual([("meme", "https://i.imgur.com/aKaOqIh.gif")], matches)

    def test_extract_markdown_links1(self):
        matches = extract_markdown_links("This is text with a link [to google](https://www.google.com) and [to youtube](https://www.youtube.com)")
        self.assertEqual([("to google", "https://www.google.com"), ("to youtube", "https://www.youtube.com")], matches)
