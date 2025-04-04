import unittest
from textnode import TextNode, TextType
from markdown_converter import split_nodes_delimiter

class TestMarkdownConverter(unittest.TestCase):
    def test_bold(self):
        nodes = [TextNode("This is a **bold** text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)

        expected = [
            TextNode("This is a ", TextType.TEXT), 
            TextNode("bold", TextType.BOLD), 
            TextNode(" text", TextType.TEXT)
        ]
        
        assert result == expected

    def test_closing_delim_bold(self):
        nodes = [TextNode("This is a **bold text", TextType.TEXT)]

        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertIn("Unmatched delimiter '**' in text", str(context.exception))

    def test_ital(self):
        nodes = [TextNode("This is an _italic_ text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

        expected = [
            TextNode("This is an ", TextType.TEXT), 
            TextNode("italic", TextType.ITALIC), 
            TextNode(" text", TextType.TEXT)
        ]
        
        assert result == expected
    
    def test_closing_delim_ital(self):
        nodes = [TextNode("This is an _italic text", TextType.TEXT)]

        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        self.assertIn("Unmatched delimiter '_' in text", str(context.exception))

    def test_code(self):
        nodes = [TextNode("This is a `code block` text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)

        expected = [
            TextNode("This is a ", TextType.TEXT), 
            TextNode("code block", TextType.CODE), 
            TextNode(" text", TextType.TEXT)
        ]

        assert result == expected
    def test_closing_delim_code(self):
        nodes = [TextNode("This is a `code block text", TextType.TEXT)]

        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertIn("Unmatched delimiter '`' in text", str(context.exception))
