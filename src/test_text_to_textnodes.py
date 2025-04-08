import unittest
from split_delimiter import split_nodes_delimiter
from split_img_and_link import split_nodes_image, split_nodes_link
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextnodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block`"
        nodes = text_to_textnodes(text)
        # Assert the correct number of nodes
        assert len(nodes) == 6
        # Check some specific nodes
        assert nodes[0].text == "This is "
        assert nodes[1].text == "text"
        assert nodes[1].text_type == TextType.BOLD
        assert nodes[3].text == "italic"
        assert nodes[3].text_type == TextType.ITALIC
        assert nodes[5].text == "code block"
        assert nodes[5].text_type == TextType.CODE