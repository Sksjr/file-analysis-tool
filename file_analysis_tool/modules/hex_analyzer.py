def analyze_hex(file_path):
    """
    Generates a hex dump of the file and analyzes its header.
    """
    try:
        with open(file_path, 'rb') as f:
            data = f.read(64)  # Read first 64 bytes (header)
        
        hex_dump = ' '.join(f"{byte:02x}" for byte in data)
        header_preview = ''.join(chr(b) if 32 <= b < 127 else '.' for b in data)
        
        return {
            "Hex Dump (First 64 bytes)": hex_dump,
            "Header Preview": header_preview
        }
    except Exception as e:
        return {"Error": str(e)}

def analyze_hex(file_path):
    """
    Generates a formatted hex dump of the file and analyzes its header.
    """
    try:
        with open(file_path, 'rb') as f:
            data = f.read(64)  # Read first 64 bytes
        
        hex_dump = ""
        ascii_preview = ""
        for i in range(0, len(data), 16):  # Process in chunks of 16 bytes
            chunk = data[i:i+16]
            hex_chunk = ' '.join(f"{byte:02x}" for byte in chunk)
            ascii_chunk = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
            hex_dump += f"{i:08x}  {hex_chunk:<48}  {ascii_chunk}\n"
        
        return {
            "Hex Dump (First 64 bytes)": hex_dump.strip(),
            "Header Preview": ascii_preview.strip()
        }
    except Exception as e:
        return {"Error": str(e)}
