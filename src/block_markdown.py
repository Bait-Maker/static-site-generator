from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordored_list"
    OLIST = "ordered_list"


def block_to_block_type(block):
    lines = block.split("\n")

    # Heading Block
    headings = (
        "# ",
        "## ",
        "### ",
        "#### ",
        "##### ",
        "###### ",
    )
    if block.startswith(headings, 0, 7):
        return BlockType.HEADING

    # Code Block
    if (
        len(lines) > 1
        and lines[0].startswith("```")
        and lines[-1][-3:].startswith("```")
    ):
        return BlockType.CODE

    # Quote Block
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    # Unorderd List Block
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST

    # Ordored List Block
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST

    return BlockType.PARAGRAPH


def markdown_to_blocks(markdown: str):
    block_strings = markdown.split("\n\n")
    blocks = []
    for string in block_strings:
        if string != "":
            blocks.append(string.strip())

    return blocks


# b = "## This is a heading block"
# code_block = """```this is a code block
# more code```"""
# quote_block = """> This is a quote
# >more quote
# >even more quote"""
# unordered_list = """- This is one point
# - This is another
# - This is a Third"""
# ordered_list = """1. One
# 2. Two
# 3. Three
# 4. Four
# 5. Five"""

# print(block_to_block(code_block))
