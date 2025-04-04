from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from enum import Enum

def text_node_to_html_node(text_node):
    if text_node.text_type is TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type is TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type is TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type is TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type is TextType.LINK:
        props = {"href": text_node.url}
        return LeafNode("a", text_node.text, props)
    elif text_node.text_type is TextType.IMAGE:
        props = {"src": text_node.url, "alt": text_node.text}
        return LeafNode("img", "", props)
    else:
        raise Exception("Invalid text type")