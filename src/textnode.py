from htmlnode import LeafNode
from inline_markdown import *

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
        case "text":
            return LeafNode(None, text_node.text)
        
        case "bold":
            return LeafNode("b", text_node.text)

        case "italic":
            return LeafNode("i", text_node.text)

        case "code":
            return LeafNode("code", text_node.text)

        case "link":
            return LeafNode("a", text_node.text, {"href":f"{text_node.url}"})

        case "image":
            return LeafNode("img", props= {"src":f"{text_node.url}", "alt":f"{text_node.text}"})
        case _:
            raise Exception("Text type not known!!!")

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type:str):
    nodes = [ ]

    for node in old_nodes:

        if node.text_type != "text":
            nodes.append(node)
            continue 

        node_content = node.text.split(delimiter)

        if len(node_content) % 2 == 0 :
            raise Exception("You need two delimiters: opening and closing!!!")

        for section_idx in range(len(node_content)): 
            if node_content[section_idx] == "":
                continue
            if section_idx % 2 == 0:
                nodes.append(TextNode(node_content[section_idx], "text"))
            else:
                nodes.append(TextNode(node_content[section_idx], text_type))
    return nodes

def split_nodes_image(old_nodes:list) -> list:
    nodes:list = [ ]
    
    for node in old_nodes:
        if node.text_type != "text":
            nodes.append(node)
            continue
        
        image = extract_markdown_images(node.text)
        if len(image) == 0:
            nodes.append(node)
            continue

        node_content = node.text.split(f"![{image[0][0]}]({image[0][1]})",1)
        for i in range(len(image)):
            if node_content[0] != "":
                nodes.append(TextNode(node_content[0], "text"))
                
            nodes.append(TextNode(image[i][0],"image",image[i][1]))

            if i < len(image) - 1:
                node_content = node_content[1].split(f"![{image[i + 1][0]}]({image[i + 1][1]})",1)

    return nodes

def split_nodes_link(old_nodes:list) -> list:
    nodes:list = [ ]
    
    for node in old_nodes:
        if node.text_type != "text":
            nodes.append(node)
            continue
        
        link = extract_markdown_links(node.text)
        if len(link) == 0:
            nodes.append(node)
            continue

        node_content = node.text.split(f"[{link[0][0]}]({link[0][1]})",1)
        for i in range(len(link)):
            if node_content[0] != "":
                nodes.append(TextNode(node_content[0], "text"))
                
            nodes.append(TextNode(link[i][0],"link",link[i][1]))

            if i < len(link) - 1:
                node_content = node_content[1].split(f"[{link[i + 1][0]}]({link[i + 1][1]})",1)

    return nodes


if __name__ == "__main__":
    print(split_nodes_image([TextNode("This is text with a image ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
                                    "text")]))
    print(split_nodes_link([TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                                    "text")]))