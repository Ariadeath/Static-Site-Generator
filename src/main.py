import os
import shutil
import sys
from pathlib import Path
from textnode import TextType, TextNode
from htmlnode import HTMLNode
from generator import generate_pages_recursive

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    public_setup("static", "docs")
    copy_files("static", "docs")
    template_content = Path("template.html").read_text()
    generate_pages_recursive("content", template_content, "docs", basepath)   

def public_setup(source_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)

def copy_files(source_dir, dest_dir):
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)
        if os.path.isfile(source_path):
            print(f"Copying {item} from {source_path} to {dest_path}")
            shutil.copy(source_path, dest_path)
        else:
            print(f"Copying {source_path} to {dest_path}")
            os.mkdir(dest_path)
            copy_files(source_path, dest_path)

main()