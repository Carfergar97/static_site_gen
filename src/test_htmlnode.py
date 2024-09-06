import unittest
from htmlnode import HTMLNode

class HTMLNodeTest(unittest.TestCase):
    def test_node_eq(self):
        node = HTMLNode("p", "Hello")
        node2 = HTMLNode("p", "Hello")
        self.assertEqual(node, node2)
    
    def test_node_neq(self):
        node = HTMLNode("p", "Hello")
        node2 = HTMLNode("a", "Hello")
        self.assertNotEqual(node,node2)

    def test_node_props_to_hmtl(self):
        node = HTMLNode("p", "Hello", props={"href": "https://www.google.com", 
        "target": "_blank",})
        self.assertEqual(node.props_to_html(),'href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    
    unittest.main()