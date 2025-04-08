import unittest
from blocktype import BlockType, block_to_block_type

class TestBlockToBlock(unittest.TestCase):
    def test_heading_block(self):
        block = "# This is a header"
        block_type= block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_code_block(self):
        block = "```\nThis is a code block\n```"
        block_type= block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)
    
    def test_quote_block(self):
        block = "> This is a quote"
        block_type= block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)
    
    def test_unordered_list(self):
        block = "- This is an unordered list"
        block_type= block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)
    
    def test_ordered_list(self):
        block = "1. This is an ordered list"
        block_type= block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_paragraph_block(self):
        block = "This is a plain paragraph."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)