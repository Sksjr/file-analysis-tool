def generate_report(results, output_file):
    """
    Generates a report summarizing the analysis results.
    """
    try:
        with open(output_file, 'w') as f:
            f.write("File Analysis Report\n")
            f.write("=" * 50 + "\n")
            for section, content in results.items():
                f.write(f"{section}:\n")
                if isinstance(content, dict):
                    for key, value in content.items():
                        f.write(f"  {key}: {value}\n")
                else:
                    f.write(f"  {content}\n")
                f.write("\n")
        return f"Report saved to {output_file}"
    except Exception as e:
        return f"Error generating report: {e}"

from datetime import datetime

def generate_report(results, output_file):
    """
    Generates a report summarizing the analysis results with timestamps.
    """
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(output_file, 'w') as f:
            f.write(f"File Analysis Report\nGenerated: {timestamp}\n")
            f.write("=" * 60 + "\n")
            for section, content in results.items():
                f.write(f"{section}:\n")
                if isinstance(content, dict):
                    for key, value in content.items():
                        f.write(f"  {key}: {value}\n")
                else:
                    f.write(f"  {content}\n")
                f.write("\n")
        return f"Report saved to {output_file}"
    except Exception as e:
        return f"Error generating report: {e}"
