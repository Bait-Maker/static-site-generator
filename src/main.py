import os
import shutil
from copy_static import copy_files_recursive

dir_path_static = "./static"
dir_path_public = "./public"


def main():
    # text_node = TextNode(
    #     "This is some anchor text", TextType.LINK, "https://www.boot.dev"
    # )
    # print(text_node)
    # leaf_node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com"})
    # print(leaf_node.to_html())

    # grandchild_node = LeafNode("b", "grandchild")
    # child_node = ParentNode("span", [grandchild_node])
    # parent_node = ParentNode("div", [child_node])
    # print(parent_node.to_html())
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        try:
            shutil.rmtree(dir_path_public)
            print(f"Direcory {dir_path_public} deleted")
        except Exception as e:
            print(f"Error: {e}")
    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)


if __name__ == "__main__":
    main()
