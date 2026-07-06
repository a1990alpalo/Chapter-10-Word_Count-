# Chapter 10 Word Count Analyzer

## Project Overview

The Chapter 10 Word Count Analyzer is a Python program that uses object-oriented programming, file input/output, exception handling, string manipulation, and `pathlib` to analyze text files.

The program displays a menu of four predefined text files. The user selects one file, and the program reads the file, removes punctuation, converts all words to lowercase, counts the frequency of each word, and prints an alphabetical word count report.

## Features

* Menu-driven user interface
* Four predefined text files to analyze
* Object-oriented design using a `WordAnalyzer` class
* File handling with `pathlib`
* Exception handling with `try-except`
* File existence checking with `.exists()`
* Line-by-line file reading with `.open()`
* Punctuation removal using the `string` library
* Lowercase word normalization
* Alphabetical word frequency report
* Invalid menu choice handling
* Exit option

## Files Included

* `Lab10_amedina6-1.py` - Main Python program
* `Monte_cristo.txt` - Sample text file
* `princess_mars.txt` - Sample text file
* `tarzan.txt` - Sample text file
* `treasure_island` - sample text file 
* `.gitignore` - Files and folders ignored by Git

## How the Program Works

The program begins by displaying a menu:

1. Princess Mars
2. Tarzan
3. treasure Island
4. Monte Carlo 
5. Exit

When the user selects a valid option, the program creates a `WordAnalyzer` object using the selected file path. The `process_file()` method reads the file, cleans each line, splits the text into words, and stores each word count in a dictionary.

If the file is processed successfully, the `print_report()` method prints each word and its frequency in alphabetical order.

## Technologies Used

* Python
* `pathlib`
* `string`
* Git
* GitHub

## How to Run the Program

Clone the repository or download the project files. Then, from the project folder, run:

```bash
python Lab10_amedina6-1.py
```

Follow the menu prompts by entering a number from 1 to 5.

## Example Output

```text
--- Word Analyzer ---
Please select a file to analyze:
1. Moby Dick (Chapter 1)
2. Frankenstein (Chapter 1)
3. Alice in Wonderland (Chapter 1)
4. Pride and Prejudice (Chapter 1)
5. Exit

Enter your choice (1-5): 1

Processing 'moby_dick_ch1.txt'...

and             :: 3
call            :: 1
i               :: 2
sea             :: 2
the             :: 5
was             :: 3

Press Enter to return to the menu...
```

## What I Practiced

This project helped me practice several important Python concepts from Chapter 10, including:

* Creating and using classes
* Initializing object attributes with `__init__`
* Using private attributes by convention
* Reading files with `pathlib`
* Checking whether files exist
* Handling missing files with `try-except`
* Cleaning text data
* Using dictionaries to store word frequencies
* Sorting dictionary keys alphabetically
* Creating a menu-driven program
* Using Git and GitHub for version control

## Author

Alberto Medina
