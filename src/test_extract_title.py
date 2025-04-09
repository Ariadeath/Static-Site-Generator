import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        title = extract_title("# This is a header")
        self.assertEqual(title, "This is a header")

    def test_multiple_spaces(self):
        title = extract_title("#   This is a header")
        self.assertEqual(title, "This is a header")
    
    def test_multiple_headerws(self):
        title = extract_title("# This is a header. # This is too")
        self.assertEqual(title, "This is a header. # This is too")

    def test_no_header(self):
        with self.assertRaises(Exception):
            extract_title("No header here")