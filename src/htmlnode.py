class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        return str(self.props)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)

    def append_child(self, child):
        raise Exception("LeafNode cannot have children")
    
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        
        # Opening tag
        html = f"<{self.tag}"

        #Adds attributes if any
        if self.props:
            for key, value in self.props.items():
                html += f' {key}="{value}"'
        
        #Close tag, add value, and add closing tag
        html += f">{self.value}</{self.tag}>"

        return html

if __name__ == "__main__":
    # Example Usage
    node = LeafNode(value="Hello, world!", tag="p")
    print(node.to_html())