from textnode import TextType, TextNode
from htmlnode import LeafNode, ParentNode


def main():
    text_node = TextNode(
        "This is some anchor text", TextType.LINK, "https://www.boot.dev"
    )
    print(text_node)
    leaf_node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com"})
    print(leaf_node.to_html())

    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    print(parent_node.to_html())


if __name__ == "__main__":
    main()
