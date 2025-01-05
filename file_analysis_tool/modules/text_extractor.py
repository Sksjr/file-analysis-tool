def extract_readable_text(file_path):
    """Extracts readable ASCII text from a binary file."""
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        return ''.join(chr(b) for b in data if 32 <= b < 127)
    except Exception as e:
        return f"Error extracting text: {e}"
def extract_readable_text(file_path):
    """
    Extracts readable ASCII/Unicode text from a binary file.
    """
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        readable_text = ''.join(chr(b) for b in data if 32 <= b < 127 or b == 10)  # ASCII printable + newline
        return readable_text
    except Exception as e:
        return f"Error extracting text: {e}"

