from htmlnode import LeafNode

text_type_text  = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode():
    def __init__(self, text, text_type, url = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self,other):
        return (self.text == other.text 
                and self.text_type == other.text_type 
                and self.url == other.url) 
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
        
def text_node_to_html_node(text_node:TextNode) -> LeafNode :

    match text_node.text_type:
        case text_type_text:
            return LeafNode(None, text_node.text)
        
        case text_type_bold:
            return LeafNode("b", text_node.text)

        case text_type_italic:
            return LeafNode("i", text_node.text)

        case text_type_code:
            return LeafNode("code", text_node.text)

        case text_type_link:
            return LeafNode("a", text_node.text, {"href":f"{text_node.url}"})

        case text_type_image:
            return LeafNode("img", props= {"src":f"{self.url}", "alt":f"{text_node.text}"})
        case _:
            raise Exception("Text type not known!!!")