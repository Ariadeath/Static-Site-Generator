from textnode import TextType, TextNode

def main():
    text = "This is some anchor text"
    text_type = TextType.LINK
    url = "https://www.boot.dev"
    example_node = TextNode(text, text_type, url)
    print(example_node)

main()