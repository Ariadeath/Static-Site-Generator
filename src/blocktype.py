from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE ="code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if all(line.startswith(">") for line in block.splitlines()):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in block.splitlines()):
        return BlockType.UNORDERED_LIST
    lines = block.split("\n")
    count = 1
    is_ordered = True

    for line in lines:
        parts = line.split('. ', 1)
        if len(parts) != 2:
            is_ordered = False
            break

        try:
            number = int(parts[0])
            if number != count:
                is_ordered = False
                break
            count += 1
        except ValueError:
            is_ordered = False
            break

    if is_ordered and lines:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH