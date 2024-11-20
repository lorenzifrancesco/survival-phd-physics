import re

def generate_toc(file_path):
    """Generate a Table of Contents from a Markdown file."""
    with open(file_path, 'r') as f:
        lines = f.readlines()

    headers = []
    for line in lines:
        # Match Markdown headers (e.g., #, ##, ###)
        match = re.match(r'^(#{1,6})\s+(.*)', line)
        if match:
            level = len(match.group(1))  # Number of `#` determines header level
            title = match.group(2).strip()
            # Generate slug for anchor link
            slug = re.sub(r'[^a-zA-Z0-9 -]', '', title)  # Remove special chars
            slug = slug.lower().replace(' ', '-')
            headers.append((level, title, slug))

    # Build ToC lines
    toc_lines = []
    for level, title, slug in headers:
        indent = '  ' * (level - 1)  # Indentation based on header level
        toc_lines.append(f"{indent}- [{title}](#{slug})")

    # Output ToC
    toc_text = "\n".join(toc_lines)
    return toc_text


# Example usage
if __name__ == "__main__":
    # Path to your Markdown file
    input_file = "README.md"
    toc = generate_toc(input_file)
    
    print("\nGenerated Table of Contents:\n")
    print(toc)

    # # Optionally save ToC to a file or print it to console
    # output_file = "TOC.md"
    # with open(output_file, "w") as f:
    #     f.write("# Table of Contents\n\n")
    #     f.write(toc)
    # print(f"\nToC saved to {output_file}")
