import unittest
from textnode import TextNode, split_nodes_delimiter


class TestSplitNodes(unittest.TestCase):
    def test_no_inline_delimiter_found(self):
        node_lst = [TextNode("Hello world", "text")]
        new_node_lst = split_nodes_delimiter(node_lst,"`", "code")
        
        self.assertEqual(new_node_lst[0].text, "Hello world")
    
    def test_no_closing_delimiter(self):
        node_lst = [TextNode("This is text with a `code block word","text")]
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(node_lst,"`","code")

    def test_no_text_node(self):
        node_lst = [TextNode("Hello","bold")]
        new_node_lst = split_nodes_delimiter(node_lst, "**", "bold") 
        self.assertEqual(node_lst, new_node_lst)

    def test_code_delimiter(self):
        node_lst = [TextNode("This is text with a `code block` word","text")]
        new_node_lst = split_nodes_delimiter(node_lst,"`","code")
        self.assertEqual(new_node_lst[0].text_type, "text")
        self.assertEqual(new_node_lst[1].text_type, "code")
        self.assertEqual(new_node_lst[2].text_type, "text")
        self.assertEqual(new_node_lst[0].text, "This is text with a ")
        self.assertEqual(new_node_lst[1].text, "code block")
        self.assertEqual(new_node_lst[2].text, " word")

if __name__ == "__main__":
    unittest.main()