def extract_title(markdown):
    if not markdown.startswith("#"):
        raise Exception("Error: not a heading")
    return markdown.strip("# ")
