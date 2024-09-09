import unittest
from htmlnode import *

class ParentNodeTest(unittest.TestCase):
    def test_no_children(self):
        node = ParentNode("p")
        with self.assertRaises(ValueError) as context:
            node.to_html()
    def test_no_tag(self):
        node = ParentNode(children = [LeafNode(value = "Hello")])
        with self.assertRaises(ValueError) as context:
            node.to_html() 

    def test_only_leaf_children(self):
        node = ParentNode("p", [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        ])
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parent_and_leaf_children(self):
        node = ParentNode("p",[ParentNode("p", [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]),LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),]
        )
        self.assertEqual(node.to_html(),"<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
if __name__ == "__main__":
    node = ParentNode("p", [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        ])
    node2 = ParentNode("p",[ParentNode("p", [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]),LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),])
    print(node.to_html())
    print(node2.to_html())
    unittest.main()