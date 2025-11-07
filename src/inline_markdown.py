import re
from collections import deque
from textnode import TextType, TextNode
# This is `an` example -> [This is a , an, example]
# This `has` multiple `ones` -> [This, has, multiple, ones]


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    images = re.findall(pattern, text)
    return images


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    links = re.findall(pattern, text)
    return links


def split_nodes_images(old_nodes):
    new_nodes = []
    split_nodes = []
    for nodes in old_nodes:
        images = extract_markdown_images(nodes.text)
        for i in range(len(images)):
            # print(images[i])
            sections = nodes.text.split(f"![{images[i][0]}]({images[i][1]})", 1)
            print(sections)
        if i == 0:
            split_nodes.append(TextNode(sections[0], TextType.TEXT))
            split_nodes.append(TextNode(images[i][0], TextType.IMAGE, images[i][1]))

    print(split_nodes)

    # return sections


def split_nodes_links(old_nodes):
    pass


test = TextNode(
    "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
    TextType.TEXT,
)
test2 = TextNode(
    "This is another text with an ![image2](https://i.imgur.com/zjjcJKZ.png) and another ![second image2](https://i.imgur.com/3elNhQu.png)",
    TextType.TEXT,
)
split_nodes_images([test, test2])
