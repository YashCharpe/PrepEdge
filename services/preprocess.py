import re

def clean_page_content(text):
    # Remove leading/trailing whitespace and quotes
    text = text.strip().strip("'").strip('"')
    # Replace multiple newlines with a single newline
    text = re.sub(r'\n+', '\n', text)
    # Remove excessive spaces
    text = re.sub(r'[ \t]+', ' ', text)
    # Remove leading/trailing spaces on each line
    text = '\n'.join(line.strip() for line in text.split('\n'))
    # Optionally, remove empty lines
    text = '\n'.join(line for line in text.split('\n') if line)
    return text
