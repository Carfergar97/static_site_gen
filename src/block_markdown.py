
def markdown_to_blocks(markdown:str) -> list:
    if markdown == "":
        return [""]
    
    blocks_lst = markdown.split("\n")
    for i in range(blocks_lst.count("")):
        blocks_lst.remove("")
    for line in blocks_lst: 
        blocks_lst[blocks_lst.index(line)] = line.strip()
        
    return blocks_lst


if __name__ == "__main__":

    print(markdown_to_blocks("# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n\
    * This is the first list item in a list block\n\
    * This is a list item\n\
    * This is another list item            "))