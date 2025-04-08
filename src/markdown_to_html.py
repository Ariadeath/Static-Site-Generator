from split_blocks import markdown_to_blocks
from blocktype import BlockType, block_to_block_type
from htmlnode import HTMLNode, ParentNode, LeafNode
from node_converter import text_node_to_html_node
from split_delimiter import split_nodes_delimiter
from split_img_and_link import split_nodes_image, split_nodes_link
from text_to_textnodes import text_to_textnodes
from extract_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode,TextType

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            normalized_text = block.replace("\n", " ")
            html_children = text_to_children(normalized_text)
            paragraph_node = ParentNode("p", html_children)
            children.append(paragraph_node)
        elif block_type == BlockType.QUOTE:
            html_children = text_to_children(block)
            quote_node = ParentNode("blockquote", html_children)
            children.append(quote_node)
        elif block_type == BlockType.CODE:
            content = "\n".join(block.split("\n")[1:-1]) + "\n"
            text_node = TextNode(content, TextType.TEXT)
            code_html_node = text_node_to_html_node(text_node)
            code_node = ParentNode("code", [code_html_node])
            prenode = ParentNode("pre", [code_node])
            children.append(prenode)
        elif block_type == BlockType.HEADING:
            level = get_heading_level(block)
            content = block[level:].strip()
            html_children = text_to_children(content)
            header_node = ParentNode(f"h{level}", html_children)
            children.append(header_node)
        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            html_lines = []
            for line in lines:
                content = line[2:].strip()
                html_line = text_to_children(content)
                unordered_line = ParentNode("li", html_line)
                html_lines.append(unordered_line)
            unordered_list = ParentNode("ul", html_lines)
            children.append(unordered_list)
        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            list_items = []
            for line in lines:
                if not line.strip():
                    continue
                if '. ' in line:
                    parts = line.split('. ', 1)
                    content = parts[1].strip()
                    item_children = text_to_children(content)
                    list_item = ParentNode("li", item_children)
                    list_items.append(list_item)
                else:
                    continue
            ordered_list = ParentNode("ol", list_items)
            children.append(ordered_list)
       
    return ParentNode("div", children)

def get_heading_level(block):
    count = 0
    for char in block:
        if char == "#":
            count += 1
        else:
            break
    return count
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes
