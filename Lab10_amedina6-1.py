"""
Word Count Analyzer

Author: Alberto Medina
Purpose: This program uses pathlib, file I/O, exception handling,
and string manipulation to count the frequency of words in text files.

Starter code: This program was modified from the professor's sample
word_counter.py code.

Date: July 5, 2026
"""

from pathlib import Path


class FileEmptyError(Exception):
    """Raised when there is a file, but the contents are empty."""

    pass


# Creating empty dictionary to use
freq_dict = {}


def is_valid_file(path: Path) -> bool:
    """
    Checks if a file exists and has contents.

    Parameters:
        path(Path): The path of the file.

    Returns:
        bool: True if the file exists and has contents.
    """

    try:
        contents = path.read_text(encoding="utf-8")

        if len(contents) <= 0:
            raise FileEmptyError("The contents of the file is empty")

    except FileEmptyError:
        print(f"\n********ERROR: {path.name} is empty")
        return False

    except FileNotFoundError:
        print(f"\n********ERROR: {path.name} does not exist")
        return False

    else:
        return True


def reset_freq() -> None:
    """Clears contents of dictionary."""

    freq_dict.clear()


def process_file(path: Path) -> None:
    """Processes the file and calculates word frequency."""

    words = convert_content_to_words(path)
    calculate_word_freq(sorted(words))


def convert_content_to_words(path: Path) -> list[str]:
    """
    Takes path and reads contents, splits into lines,
    and splits lines into word lists.
    """

    words = []
    contents = path.read_text(encoding="utf-8")
    lines = contents.splitlines()

    for line in lines:
        line = remove_punc(line)
        words.extend(line.split())

    return words


def remove_punc(contents: str) -> str:
    """Remove all punctuation from words in a string."""

    punctuation_tuple = (
        ".",
        ",",
        "!",
        "?",
        ";",
        ":",
        '"',
        "'",
        "(",
        ")",
        "[",
        "]",
        "{",
        "}",
        "-",
        "_",
        "—",
        "“",
        "”",
        "‘",
        "’",
        "•",
    )

    for punctuation in punctuation_tuple:
        if punctuation == "-" or punctuation == "—":
            contents = contents.replace(punctuation, " ")
        else:
            contents = contents.replace(punctuation, "")

    return contents


def calculate_word_freq(words: list[str]) -> None:
    """Calculate frequency of each word."""

    for word in words:
        temp = word.lower()
        freq_dict[temp] = freq_dict.get(temp, 0) + 1


def display_word_freq() -> None:
    """Display word frequency."""

    if len(freq_dict) == 0:
        print("No words to display.")
        return

    max_key_length = max(len(str(key)) for key in freq_dict.keys())

    for key, value in sorted(freq_dict.items()):
        print(f"{str(key).ljust(max_key_length)} :: {value}")


def run_word_counter(path: Path) -> None:
    """Validate, process, and display the word frequency for one file."""

    reset_freq()

    print(f"\nProcessing '{path.name}'...\n")

    if is_valid_file(path):
        process_file(path)
        display_word_freq()
    else:
        print("Issues with file")


def display_menu() -> None:
    """Display the word analyzer menu."""

    print("\n--- Word Analyzer ---")
    print("Please select a file to analyze:")
    print("1. Princess of Mars")
    print("2. Tarzan")
    print("3. Treasure Island")
    print("4. The Count of Monte Cristo")
    print("5. Exit")


def main() -> None:
    """Run the word analyzer menu."""

    book_files = {
        "1": Path.cwd() / "princess_mars.txt",
        "2": Path.cwd() / "Tarzan.txt",
        "3": Path.cwd() / "treasure_island.txt",
        "4": Path.cwd() / "monte_cristo.txt",
    }

    while True:
        display_menu()

        choice = input("\nEnter your choice (1-5): ")

        if choice == "5":
            print("\nGoodbye!")
            break

        elif choice in book_files:
            run_word_counter(book_files[choice])
            input("\nPress Enter to return to the menu...")

        else:
            print("\nInvalid choice. Please select from 1-5.")
            input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()