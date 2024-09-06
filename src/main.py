from textnode import *
def main():

    my_first_text_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    my_second_text_node = TextNode("This is a text node", "bold", "https://www.boot.dev")

    print(my_first_text_node == my_second_text_node)
    print(my_first_text_node)
    

if __name__ == "__main__":
    main()