import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            tag="link",
            value="Click me",
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        node2 = HTMLNode(
            tag="h1",
            value="Click me",
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_eq2(self):
        node = HTMLNode(
            tag="link",
            value="Click me",
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )

        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )

    def test_eq_false(self):
        node = HTMLNode(
            tag="h1",
            value="Heading",
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        self.assertNotEqual("href: https://www.google.com", node.props_to_html())


if __name__ == "__main__":
    unittest.main()
