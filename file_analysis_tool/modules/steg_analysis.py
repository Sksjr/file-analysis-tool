from PIL import Image

def lsb_analysis(image_path):
    """
    Performs Least Significant Bit (LSB) analysis on an image to detect hidden data.
    """
    try:
        img = Image.open(image_path)
        pixels = list(img.getdata())
        
        lsb_data = []
        for pixel in pixels:
            if isinstance(pixel, int):  # Grayscale image
                lsb_data.append(pixel & 1)
            else:  # Color image
                lsb_data.extend([channel & 1 for channel in pixel[:3]])  # RGB
        
        # Convert LSB data to binary string and check for patterns
        binary_data = ''.join(map(str, lsb_data))
        return f"Binary LSB data preview (first 128 bits): {binary_data[:128]}"
    except Exception as e:
        return f"Error performing LSB analysis: {e}"

import numpy as np

def custom_steg_analysis(image_path):
    """
    Custom method to detect hidden data in an image by analyzing pixel intensity patterns.
    """
    try:
        img = Image.open(image_path)
        pixels = np.array(img)

        # Example: Check variance in pixel intensity to detect anomalies
        if len(pixels.shape) == 3:  # Color image
            pixel_variances = np.var(pixels, axis=(0, 1))  # Variance of R, G, B channels
        else:  # Grayscale image
            pixel_variances = np.var(pixels)

        if np.any(pixel_variances > 200):  # Threshold for anomaly detection
            return f"Potential steganographic data detected (high variance: {pixel_variances})."
        return "No anomalies detected in pixel intensity."
    except Exception as e:
        return f"Error in custom steganography detection: {e}"


import matplotlib.pyplot as plt
import numpy as np

def lsb_analysis(image_path):
    """
    Performs LSB analysis and creates a histogram for hidden data detection.
    """
    try:
        img = Image.open(image_path)
        pixels = np.array(img)
        
        lsb_data = []
        for pixel in pixels.flatten():
            lsb_data.append(pixel & 1)  # Extract LSB
        
        # Generate histogram for visual inspection
        plt.hist(lsb_data, bins=2, color='blue', edgecolor='black')
        plt.title("Histogram of LSBs")
        plt.xlabel("LSB Value (0 or 1)")
        plt.ylabel("Frequency")
        plt.savefig("lsb_histogram.png")
        plt.close()

        return "LSB analysis completed. Histogram saved as 'lsb_histogram.png'."
    except Exception as e:
        return f"Error performing LSB analysis: {e}"
