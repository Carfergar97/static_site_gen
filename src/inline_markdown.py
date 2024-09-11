import re

def extract_markdown_images(text:str) -> list: 
    markdown_images_list = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return markdown_images_list

def extract_markdown_links(text:str) -> list:
    markdown_links_list = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return markdown_links_list

if __name__ == "__main__":

    print(extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"))
    print(extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"))