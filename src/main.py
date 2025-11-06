from textnode import TextType, TextNode
from htmlnode import LeafNode


def main():
    text_node = TextNode(
        "This is some anchor text", TextType.LINK, "https://www.boot.dev"
    )
    print(text_node)
    leaf_node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com"})
    print(leaf_node.to_html())


if __name__ == "__main__":
    main()
