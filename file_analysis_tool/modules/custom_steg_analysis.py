def custom_steg_analysis(image_path):
    """
    Analyzes statistical properties of image pixels to detect hidden data.
    """
    try:
        img = Image.open(image_path)
        pixels = np.array(img)
        
        # Calculate means for RGB channels
        if len(pixels.shape) == 3:  # Color image
            r_mean = np.mean(pixels[:, :, 0])
            g_mean = np.mean(pixels[:, :, 1])
            b_mean = np.mean(pixels[:, :, 2])
            diff_rg = abs(r_mean - g_mean)
            diff_gb = abs(g_mean - b_mean)

            if diff_rg > 10 or diff_gb > 10:  # Example thresholds
                return f"Anomalies detected (R-G: {diff_rg:.2f}, G-B: {diff_gb:.2f})."
        else:  # Grayscale image
            mean_intensity = np.mean(pixels)
            if mean_intensity < 50 or mean_intensity > 200:
                return f"Potential hidden data detected (mean intensity: {mean_intensity:.2f})."

        return "No significant anomalies detected."
    except Exception as e:
        return f"Error in custom steganography detection: {e}"

