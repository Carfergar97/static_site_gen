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

class TestBlockToBlockType(unittest.TestCase):
    def test_heading_block(self):
        heading_1 = "# Heading"
        heading_2 = "## Heading"
        heading_3 = "### Heading"
        heading_4 = "#### Heading"
        heading_5 = "##### Heading"
        heading_6 = "###### Heading"
        self.assertEqual(block_to_block_type(heading_1),"heading")
        self.assertEqual(block_to_block_type(heading_2),"heading")
        self.assertEqual(block_to_block_type(heading_3),"heading")
        self.assertEqual(block_to_block_type(heading_4),"heading")
        self.assertEqual(block_to_block_type(heading_5),"heading")
        self.assertEqual(block_to_block_type(heading_6),"heading")
    
    def test_code_block(self):
        self.assertEqual(block_to_block_type('``` print("hello world") ```'), "code")

    def test_quote_block(self):
        self.assertEqual(block_to_block_type("> Un fantasma recorre Europa"), "quote")

    def test_unordered_list_block(self):
        self.assertEqual(block_to_block_type("* apples"), "unordered_list")
        self.assertEqual(block_to_block_type("- apples"), "unordered_list")

    def test_ordered_list_block(self):
        self.assertEqual(block_to_block_type("1. The first item in the list"), "ordered_list")

    def test_normal_paragraph(self):
        self.assertEqual(block_to_block_type(" hello this is a normal paragraph"),"paragraph")

if __name__ == "__main__":

    unittest.main()