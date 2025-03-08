import os
import re

def clean_srt(file_path):
    """
    Reads an SRT file and returns a cleaned string by removing:
      - numeric index lines
      - timestamp lines (those containing -->)
      - empty lines
    """
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    cleaned_lines = []
    for line in lines:
        # Remove lines that contain only numbers (caption indices)
        if re.match(r'^\d+$', line.strip()):
            continue
        # Remove lines with timestamps (contain "-->")
        if "-->" in line:
            continue
        # If the line isn't empty, keep it
        if line.strip():
            cleaned_lines.append(line.strip())

    # Join all cleaned lines with a newline
    return "\n".join(cleaned_lines)

def main():
    """
    Asks the user for a directory path to process .srt files.
    If no directory is provided, uses the current script's directory.
    Cleans each .srt file and saves the output as <filename>_cleaned.txt.
    """
    # Ask user for a target directory
    user_input = input("Enter a directory path (press Enter to use current directory): ").strip()

    # If user didn't provide anything, use current directory
    if not user_input:
        target_dir = os.getcwd()
        print("No directory provided. Using current directory:")
        print(target_dir)
    else:
        # Use the provided directory
        target_dir = user_input
        print("Using directory:")
        print(target_dir)

    # Get a list of all .srt files in the chosen directory
    srt_files = [f for f in os.listdir(target_dir) if f.endswith(".srt")]

    if not srt_files:
        print("No .srt files found in the specified directory.")
        return

    # Clean and save each .srt file as <original>_cleaned.txt
    for srt_file in srt_files:
        input_file = os.path.join(target_dir, srt_file)
        output_file = os.path.join(
            target_dir,
            srt_file.replace(".srt", "_cleaned.txt")
        )

        # Clean the SRT file content
        cleaned_text = clean_srt(input_file)

        # Write the cleaned captions to a new .txt file
        with open(output_file, "w", encoding="utf-8") as out:
            out.write(cleaned_text)

        print(f"Processed: {srt_file} → {os.path.basename(output_file)}")

    print("\nAll SRT files have been cleaned and saved as .txt!")

if __name__ == "__main__":
    main()
