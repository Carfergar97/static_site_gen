
def markdown_to_blocks(markdown:str) -> list:
    if markdown == "":
        return [""]
    
    blocks_lst = markdown.split("\n\n")
    for i in range(blocks_lst.count("")):
        blocks_lst.remove("")
    for line in blocks_lst: 
        blocks_lst[blocks_lst.index(line)] = line.strip()
        
    return blocks_lst

def block_to_block_type(markdown:str) -> str:
    if(markdown.split("#").count("") != 0 and markdown[markdown.split("#").count("")]==" "):
        return "heading"
    elif(markdown[:3] == "```" and markdown[-3:] == "```"):
        return "code"
    elif(markdown[0] == ">"):
        return "quote"
    elif(markdown[:2] == "- " or markdown[:2] == "* "):
        return "unordered_list"
    elif(markdown[0].isdecimal and markdown[1:3] == ". "): 
        return "ordered_list"
    else:
        return "paragraph"

if __name__ == "__main__":

    print(markdown_to_blocks("# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n\
    * This is the first list item in a list block\n\
    * This is a list item\n\
    * This is another list item            "))