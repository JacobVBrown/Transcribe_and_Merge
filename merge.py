import os

def main():
    """
    Merges all .txt files from the user-specified directory (or current directory if none is provided)
    into one file named 'merged_captions.txt'.
    """
    user_input = input("Enter a directory path (press Enter to use current directory): ").strip()

    if not user_input:
        target_dir = os.getcwd()
        print("No directory provided. Using current directory:")
        print(target_dir)
    else:
        target_dir = user_input
        print("Using directory:")
        print(target_dir)

    # Name of the merged output file
    output_filename = "merged_captions.txt"
    output_path = os.path.join(target_dir, output_filename)

    # Get a list of all .txt files in the target directory (excluding the merged output file)
    txt_files = [
        f for f in os.listdir(target_dir)
        if f.endswith(".txt") and f != output_filename
    ]

    if not txt_files:
        print("No .txt files found in the specified directory.")
        return

    # Merge all .txt files into one
    with open(output_path, "w", encoding="utf-8") as outfile:
        for txt_file in txt_files:
            file_path = os.path.join(target_dir, txt_file)

            with open(file_path, "r", encoding="utf-8") as infile:
                # Optional: write the filename as a header
                outfile.write(f"\n--- {txt_file} ---\n")

                # Write the content of the file
                outfile.write(infile.read())
                outfile.write("\n")  # Add spacing between files

    print(f"All .txt files have been merged into {output_path}!")

if __name__ == "__main__":
    main()
