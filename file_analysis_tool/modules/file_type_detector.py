import magic

def detect_file_type(file_path):
    """
    Detects the type of a file based on its magic bytes.
    """
    try:
        file_type = magic.from_file(file_path, mime=True)
        return file_type
    except Exception as e:
        return f"Error detecting file type: {e}"
