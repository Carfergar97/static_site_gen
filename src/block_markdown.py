
def markdownt_to_blocks(markdown:str) -> list:
    if markdown == "":
        return [""]
    
    blocks_lst = markdown.split("\n")

    for line in blocks_lst:
        line.strip()
        if line == "":
            blocks_lst.remove(line)

    return blocks_lst


if __name__ == "__main__":

    print(markdownt_to_blocks("# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n\
    * This is the first list item in a list block\n\
    * This is a list item\n\
    * This is another list item"))