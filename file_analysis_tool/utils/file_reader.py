import os

def validate_file(file_path):
    """
    Validates the file path and checks if the file exists and is accessible.
    """
    if not os.path.exists(file_path):
        return False, "Error: File does not exist."
    if not os.path.isfile(file_path):
        return False, "Error: Path is not a file."
    if not os.access(file_path, os.R_OK):
        return False, "Error: File is not readable."
    return True, "File is valid."
