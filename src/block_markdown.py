def markdown_to_blocks(markdown: str):
    block_strings = markdown.split("\n\n")
    blocks = []
    for string in block_strings:
        if string != "":
            blocks.append(string.strip())

    return blocks
