import unittest

from extract_title import *

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
