from extract_markdown import extract_markdown_links, extract_markdown_images
from textnode import TextNode,TextType
from split_delimiter import split_nodes_delimiter

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        current_text = node.text

        while True:
            
            images = extract_markdown_images(current_text)
            
            if not images:
                if current_text:
                    new_nodes.append(TextNode(current_text, TextType.TEXT))
                break

            image_alt, image_url = images[0]
            image_markdown = f"![{image_alt}]({image_url})"

            parts = current_text.split(image_markdown, 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))

            if len(parts) > 1:
                current_text = parts[1]
            else:
                current_text = ""
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        current_text = node.text

        while True:
            links = extract_markdown_links(current_text)
            
            if not links:
                if current_text:
                    new_nodes.append(TextNode(current_text, TextType.TEXT))
                break

            link_text, link_url = links[0]
            link_markdown = f"[{link_text}]({link_url})"

            parts = current_text.split(link_markdown, 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

            if len(parts) > 1:
                current_text = parts[1]
            else:
                current_text = ""
    
    return new_nodes