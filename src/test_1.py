import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold_text)
        node2 = TextNode("This is a text node", TextType.italic_text)
        if node != node2:
            return True


if __name__ == "__main__":
    unittest.main()