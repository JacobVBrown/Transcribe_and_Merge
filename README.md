# Transcribe and Merge Tools

This repository contains two utility scripts for working with text data:
1. **transcribe_all_srt.py** – Cleans '.srt' subtitle files by removing timing and caption indices, then saves the cleaned text to new '.txt' files.
2. **merge.py** – Merges multiple '.txt' files in the same directory into a single file ('merged_captions.txt').

---

## Usage

### 1. Cleaning '.srt' Files ('transcribe_all_srt.py')

1. Place one or more '.srt' subtitle files in the some directory
2. Open a terminal/command prompt, navigate to python scripts and input
   the directory you would like to transcribe as an arg.
3. Run:
   python3 transcribe_all_srt.py /path/to/directory

### 2. Merging '.txt' Files ('merge.py')

1. Place multiple '.txt' files in the some directory
2. Open a terminal/command prompt, navigate to python scripts and input
   the directory you would like to merge as an arg.
3. Run:
   python3 transcribe_all_srt.py /path/to/directory

