import unittest
from htmlnode import *

class LeafNodeTest(unittest.TestCase):
    def test_node_eq(self):
        node=LeafNode("p","Hello")

        node2=LeafNode("p","Hello")

        self.assertEqual(node.tag, node2.tag)
        self.assertEqual(node.value, node2.value)
        self.assertEqual(node.props,node2.props)

    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        self.assertEqual(node.to_html(),"<p>This is a paragraph of text.</p>")
        self.assertEqual(node2.to_html(),'<a href="https://www.google.com">Click me!</a>')

    def test_repr(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.__repr__(),f"LeafNode(p, This is a paragraph of text., {None})")

if __name__ == "__main__":
    node = LeafNode("p", "This is a paragraph of text.")
    print(node == node.__repr__())
    unittest.main()
