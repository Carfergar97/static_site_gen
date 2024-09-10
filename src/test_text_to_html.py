import unittest
from textnode import * 

class TestTextToHTML(unittest.TestCase):
    def test_text_type(self):
        node = LeafNode(None, "Hello") 
        node2=text_node_to_html_node(TextNode("Hello", "text"))
        
        self.assertEqual(node.tag,node2.tag)
        self.assertEqual(node.value,node2.value)
        self.assertEqual(node.props,node2.props)

    def test_bold_type(self):
        node = LeafNode("b", "Hello")
        node2 = text_node_to_html_node(TextNode("Hello","bold"))
        
        self.assertEqual(node.tag,node2.tag)
        self.assertEqual(node.value,node2.value)
        self.assertEqual(node.props,node2.props)

    def test_italic_type(self):
        node = LeafNode("i", "Hello")
        node2 = text_node_to_html_node(TextNode("Hello","italic"))
        
        self.assertEqual(node.tag,node2.tag)
        self.assertEqual(node.value,node2.value)
        self.assertEqual(node.props,node2.props)

    def test_code_type(self):
        node = LeafNode("code", "Hello")
        node2 = text_node_to_html_node(TextNode("Hello","code"))
        
        self.assertEqual(node.tag,node2.tag)
        self.assertEqual(node.value,node2.value)
        self.assertEqual(node.props,node2.props)

    def test_link_type(self):
        node = LeafNode("a", "Hello", {"href":"https://www.google.com/"})
        node2 = text_node_to_html_node(TextNode("Hello","link","https://www.google.com/"))
        
        self.assertEqual(node.tag,node2.tag)
        self.assertEqual(node.value,node2.value)
        self.assertEqual(node.props,node2.props)
    def test_image_type(self):
        node = LeafNode("img", None, {"src":"https://www.google.com/", "alt": "Hello"})
        node2 = text_node_to_html_node(TextNode("Hello","image","https://www.google.com/"))
        
        self.assertEqual(node.tag,node2.tag)
        self.assertEqual(node.value,node2.value)
        self.assertEqual(node.props,node2.props)

    def test_raise_error(self):
        with self.assertRaises(Exception):
            text_node_to_html_node(TextNode("Hello","bad_tag","https://www.google.com/"))

if __name__ == "__main__":
    unittest.main()