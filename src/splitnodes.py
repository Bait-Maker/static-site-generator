import re
from textnode import TextType, TextNode

# This is `an` example -> [This is a , an, example]
# This `has` multiple `ones` -> [This, has, multiple, ones]


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    # for each old node
    # check for and split at delimiter
    #   - raise exeption if delimiter is non matching
    #   - if old node is not a .TEXT type, just add it ot the new list
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("invalid markdown syntax")
        split_nodes = re.split(rf"({delimiter})", node.text)
        joined_nodes = []
        counter = 0
        for part in split_nodes:
            if counter >= 2:
                counter = 0
            if part == delimiter:
                counter += 1
                continue
            if counter == 1:
                joined_nodes.append(TextNode(part, text_type))
            if counter == 0:
                joined_nodes.append(TextNode(part, TextType.TEXT))
    new_nodes.extend(joined_nodes)
    return new_nodes


text = "_apple_ banana _cherry_ pie"
delimiter = "_"
marked_parts = re.split(rf"({delimiter})", text)
print(marked_parts)
node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
print(new_nodes)
