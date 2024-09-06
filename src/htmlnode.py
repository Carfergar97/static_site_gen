
class HTMLNode():
    def __init__(self, tag:str=None, value:str=None, children:list=None, props:dict=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):

        raise NotImplementedError
    
    def props_to_html(self):
        props_iter = self.props.items()
        key, value = list(props_iter)[0]
        attr_str:str = f'{key}="{value}"'

        for key, value in list(props_iter)[1:]:
            attr_str += f' {key}="{value}"'
        
        return attr_str
        
    def __repr__(self) -> str:

        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other) -> bool:
        
        return (self.tag == other.tag
                and self.value == other.value
                and self.children == other.children
                and self.props == other.props)


class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, props: dict = None) -> None:
        super().__init__(tag, value, props=props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}>"+f"{self.value}"+f"<{self.tag}>"