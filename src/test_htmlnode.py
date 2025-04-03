import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props1(self):
        tag = "bob"
        value = 1
        children = None
        props = "aaron"
    
    def test_props2(self):
        tag = "carol"
        value = 2
        children = None
        props = "chester"
    
    def test_props3(self):
        tag = "john"
        value = 1
        children = None
        props = "billy"

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")