import unittest
from textnode import TextNode, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes

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
    
    def test_split_nodes_image(self):
        node_lst = [TextNode("This is text with a image ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
                                    "text")]
        self.assertEqual(split_nodes_image(node_lst), [TextNode("This is text with a image ", "text"),
                                        TextNode("rick roll", "image", "https://i.imgur.com/aKaOqIh.gif"),
                                        TextNode(" and ", "text"),
                                        TextNode("obi wan", "image", "https://i.imgur.com/fJRm4Vk.jpeg")])
    
    def test_split_nodes_link(self):
        node_lst = [TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                                    "text")]
        self.assertEqual(split_nodes_link(node_lst), [TextNode("This is text with a link ", "text"),
                                        TextNode("to boot dev", "link", "https://www.boot.dev"),
                                        TextNode(" and ", "text"),
                                        TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev")])
    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.com/image.png)",
            "text",
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", "image", "https://www.example.com/image.png"),
            ],
            new_nodes,
        )
    
    def test_split_link_single(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev)",
            "text",
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("to boot dev", "link", "https://www.boot.dev"),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertListEqual(text_to_textnodes(text),[
            TextNode("This is ", "text"),
            TextNode("text", "bold"),
            TextNode(" with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word and a ", "text"),
            TextNode("code block", "code"),
            TextNode(" and an ", "text"),
            TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", "text"),
            TextNode("link", "link", "https://boot.dev"),
]
)
if __name__ == "__main__":
    unittest.main()