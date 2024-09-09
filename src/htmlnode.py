
class HTMLNode():
    def __init__(self, tag:str=None, value:str=None, children:list=None, props:dict=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):

        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        attr_str:str = "" 

        for prop in self.props:
            attr_str += f' {prop}="{self.props[prop]}"' 
        
        return attr_str
        
    def __repr__(self) -> str:

        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag: str = None, children: list = None, props: dict = None) -> None:
        super().__init__(tag, children=children, props=props)
        
    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent nodes musth have a tag!!!")
        
        if self.children == None:
            raise ValueError("Parent nodes must have childrens!!!")

        
class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, props: dict = None) -> None:
        super().__init__(tag, value, props=props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("Invalid HTML: no value")
        if self.tag == None:
            return self.value
        return  f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            # if self.tag == "p":
            #     return f"<{self.tag}>"+f"{self.value}"+f"</{self.tag}>"
            # elif self.tag == "a":
            #     if self.props == None:
            #         raise Exception("There is not hyperlink available.")
            #     return f"<{self.tag} " + f"href=" + f'"{self.props["href"]}">' + f"{self.value}" + f"</{self.tag}>"
            # else:
            #     raise Exception("This tag is not managed yet...")

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"