import os
import shutil


def copy_files_recursive(src_dir, dst_dir):
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    for filename in os.listdir(src_dir):
        src_path = os.path.join(src_dir, filename)
        dst_path = os.path.join(dst_dir, filename)

        print(f" * {src_path} -> {dst_path}")
        if os.path.isdir(src_path):
            copy_files_recursive(src_path, dst_path)
        else:
            shutil.copy(src_path, dst_path)
