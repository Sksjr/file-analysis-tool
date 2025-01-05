from modules.file_type_detector import detect_file_type
from modules.text_extractor import extract_readable_text
from modules.hex_analyzer import analyze_hex
from modules.steg_analysis import lsb_analysis, custom_steg_analysis
from modules.report_generator import generate_report

def main():
    file_path = input("Enter the file path: ")
    
    # File Type Detection
    file_type = detect_file_type(file_path)
    print(f"File Type: {file_type}")
    
    # Text Extraction
    text = extract_readable_text(file_path)
    print(f"Extracted Text (Preview): {text[:100]}...")  # Show first 100 characters
    
    # Hex Dump and Header Analysis
    hex_result = analyze_hex(file_path)
    print(f"Hex Dump (First 64 bytes): {hex_result['Hex Dump (First 64 bytes)']}")
    print(f"Header Preview: {hex_result['Header Preview']}")
    
    # Steganography Analysis
    if file_type.startswith("image"):
        lsb_result = lsb_analysis(file_path)
        custom_result = custom_steg_analysis(file_path)
        print(f"LSB Analysis: {lsb_result}")
        print(f"Custom Steganography Detection: {custom_result}")
    else:
        lsb_result = "Not applicable (not an image)."
        custom_result = "Not applicable (not an image)."
    
    # Report Generation
    results = {
        "File Type": file_type,
        "Extracted Text (Preview)": text[:100],
        "Hex Analysis": hex_result,
        "LSB Analysis": lsb_result,
        "Custom Steganography Detection": custom_result
    }
    report_status = generate_report(results, "analysis_report.txt")
    print(report_status)

if __name__ == "__main__":
    main()


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

from utils.logger import setup_logger

logger = setup_logger("tool.log")

def main():
    try:
        file_path = input("Enter the file path: ")
        logger.info(f"Analyzing file: {file_path}")
        # Validation and analysis logic
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print("An error occurred. Check the log for details.")

