from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if delimiter is None:
            new_nodes.append(node)
        elif node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {node.text} ")
            inside_delimiter = False
            for part in split_text:
                if inside_delimiter:
                    new_nodes.append(TextNode(part, text_type))
                else:
                    new_nodes.append(TextNode(part, TextType.TEXT))
                inside_delimiter = not inside_delimiter
    return new_nodes