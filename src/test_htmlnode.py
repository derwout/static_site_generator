import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )
    
    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, None, {'class': 'primary'})",
        )


    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leafnode_to_html_wprops(self):
        node = LeafNode("a", "this is anchor text", {"href": "testurl", "target": "_blank" })
        self.assertEqual(
            node.to_html(),
            '<a href="testurl" target="_blank">this is anchor text</a>'
        )
    
    def test_leafnode_tagless(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


    def test_parentnode_onechild(self):
        node = ParentNode(
            "p",
            [LeafNode("i", "italic text")],
        )
        self.assertEqual(
            node.to_html(),
            "<p><i>italic text</i></p>"
        )
    
    def test_parentnode_twochildren(self):
        node = ParentNode(
            "p",
            [LeafNode("i", "italic text"), 
             LeafNode("b", "bold text")],
        )
        self.assertEqual(
            node.to_html(),
            "<p><i>italic text</i><b>bold text</b></p>"
        )

    def test_parentnode_repr(self):
        node = ParentNode(
            "p",
            [],
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "ParentNode(p, [], {'class': 'primary'})",
        )

if __name__ == "__main__":
    unittest.main()