from textnode import *
from htmlnode import *
def main():

    my_first_text_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    my_second_text_node = TextNode("This is a text node", "bold", "https://www.boot.dev")

    print(my_first_text_node == my_second_text_node)
    print(my_first_text_node)
    
    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

    print(node.to_html())
if __name__ == "__main__":
    main()