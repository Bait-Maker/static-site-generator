import os
import shutil
from copy_static import copy_files_recursive
from generate_page import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
file_path_content = "./content/index.md"
file_path_template = "template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        try:
            shutil.rmtree(dir_path_public)
            print(f"Direcory {dir_path_public} deleted")
        except Exception as e:
            print(f"Error: {e}")
    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    generate_page(file_path_content, file_path_template, dir_path_public)


if __name__ == "__main__":
    main()
