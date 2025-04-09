import os
import shutil
from textnode import TextType, TextNode
from htmlnode import HTMLNode
from generator import generate_page

def main():
    public_setup("static", "public")
    copy_files("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")   

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