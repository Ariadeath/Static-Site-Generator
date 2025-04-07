import unittest
from extract_markdown import extract_markdown_links, extract_markdown_images
from textnode import TextNode,TextType
from split_delimiter import split_nodes_delimiter
from split_img_and_link import split_nodes_image, split_nodes_link

class TestSplitImgAndLink(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
    )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
    )
    
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link to Boot.dev](https://boot.dev) and another [link to Google](https://google.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link to Boot.dev", TextType.LINK, "https://boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("link to Google", TextType.LINK, "https://google.com"),
            ],
            new_nodes,
        )