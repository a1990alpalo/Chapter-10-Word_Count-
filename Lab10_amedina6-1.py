""""Word Count Analyzer
Author: Alberto Medina 
Purpose: This program uses (OOP), pathlib, file I/O, exception handling, as well as string manipulation to count 
the frequency of words in a text file

Starter code: No starter code was used. It was built using the assignment requirements
Date: July 5, 2026"""

from pathlib import Path
import string 


class WordAnalyzer: 
    """Analyzes word frequency in a text file."""

    def __init__(self, filepath):
        """Starts the analyzer with a file path and an empty dictionary."""
        self._filepath = Path(filepath)
        self._word_frequencies = {}

    
    def process_file(self):
        """Read the file and count the frequency of each word."""
        try:
            if not self._filepath.exists():
                raise FileNotFoundError(self._filepath)

            punctuation_table = str.maketrans("", "", string.punctuation)

            with self._filepath.open("r", encoding="utf-8") as file:
                for line in file:
                    clean_line = line.translate(punctuation_table)
                    clean_line = clean_line.lower()
                    words = clean_line.split()

                    for word in words:
                        if word in self._word_frequencies:
                            self._word_frequencies[word] += 1
                        else:
                            self._word_frequencies[word] = 1

            return True

        except FileNotFoundError:
            print(f"Error: The file '{self._filepath}' was not found.")
            return False
    
    def print_report(self):
        """Print an alphabetical report of word frequencies."""
        words = sorted(self._word_frequencies.keys())

        for word in words:
            print(f"{word:<15} :: {self._word_frequencies[word]}")

def main():
    """Display a menu and analyze the selected text file."""
    files = {
    "1": {
        "name": "Princess Mars",
        "path": Path("princess_mars.txt"),
    },
    "2": {
        "name": "Tarzan",
        "path": Path("Tarzan.txt"),
    },
    "3": {
        "name": "Treasure Island",
        "path": Path("treasure_island.txt"),
    },
    "4": {
        "name": "Monte Cristo",
        "path": Path("monte_cristo.txt"),
    },
}

    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")

        for choice, file_info in files.items():
            print(f"{choice}. {file_info['name']}")

        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "5":
            print("\nGoodbye!")
            break

        if choice not in files:
            print("\nInvalid choice. Please select from 1-5.")
            input("\nPress Enter to return to the menu...")
            continue

        selected_file = files[choice]["path"]

        print(f"\nProcessing '{selected_file}'...\n")

        analyzer = WordAnalyzer(selected_file)

        if analyzer.process_file():
            analyzer.print_report()

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()