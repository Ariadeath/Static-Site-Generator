def markdown_to_blocks(markdown):
    markdown = markdown.strip()
    split = markdown.split("\n\n")
    new_blocks = []
    for block in split:
        if block.strip():
            lines = block.split("\n")
            cleaned_lines = [line.strip() for line in lines]
            cleaned_block = "\n".join(cleaned_lines)
            new_blocks.append(cleaned_block)
    return new_blocks
