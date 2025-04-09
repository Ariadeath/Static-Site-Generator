import os
from pathlib import Path
from markdown_to_html import markdown_to_blocks, markdown_to_html_node
from extract_title import extract_title 

def generate_page(from_path, template_content, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path}")
    with open(from_path, 'r') as file:
        markdown_content = file.read()
    
    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)
    final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    final_html = final_html.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w') as file:
        file.write(final_html)

def generate_pages_recursive(dir_path_content, template_content, dest_dir_path, basepath):
    dir_path_content = Path(dir_path_content)
    dest_dir_path = Path(dest_dir_path)

    for item in dir_path_content.iterdir():
        if item.is_file() and item.suffix == '.md':
            relative_path = item.relative_to(dir_path_content)
            dest_path = dest_dir_path / relative_path.with_suffix('.html')
            generate_page(str(item), template_content, str(dest_path), basepath)
        elif item.is_dir():
            new_dest_dir = dest_dir_path / item.name
            new_dest_dir.mkdir(parents=True, exist_ok=True)

            generate_pages_recursive(item, template_content, new_dest_dir, basepath)