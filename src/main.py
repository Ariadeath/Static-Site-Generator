from textnode import TextType, TextNode
from htmlnode import HTMLNode

def main():
    text = "This is some anchor text"
    text_type = TextType.LINK
    url = "https://www.boot.dev"
    example_node = TextNode(text, text_type, url)
    print(example_node)

    props = {
    "href": "https://www.google.com",
    "target": "_blank",
}
    example_html = HTMLNode(None, None, None, props)
    print(example_html)


main()