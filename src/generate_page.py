from block_markdown import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")

    with open(from_path, "r") as mardown_file:
        markdown = mardown_file.read()
        mardown_file.close()

    with open(template_path, "r") as template_file:
        template = template_file.read()
        template_file.close()

    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown.split("\n")[0])

    new_template = template.replace("{{ Content }}", html_string)
    new_template = new_template.replace("{{ Title }}", title)

    with open(f"{dest_path}", "w") as file:
        try:
            print(f"Writing file into {dest_path}...")
            file.write(new_template)
            print("File written successfully!")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            file.close()


def extract_title(markdown):
    if not markdown.startswith("#"):
        raise Exception("Error: not a heading")
    return markdown.strip("# ")
