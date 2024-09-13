import unittest
from block_markdown import *

class TestMarkdownToBlocks(unittest.TestCase):
    def test_no_text(self):
        self.assertEqual("","")
    def test_one_line_leading_space(self):
        self.assertListEqual(markdown_to_blocks("       # This is a heading\n"),
                         ["# This is a heading"])
    def test_one_line_trailing_space(self):
        self.assertListEqual(markdown_to_blocks("# This is a heading            \n"),
                         ["# This is a heading"])
    def test_one_line_leading_and_trailing_space(self):
        self.assertListEqual(markdown_to_blocks("            # This is a heading            \n"),
                         ["# This is a heading"])
    def test_remove_empty_blocks(self):
        self.assertListEqual(markdown_to_blocks("# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n"),
                             ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it."])

if __name__ == "__main__":

    unittest.main()