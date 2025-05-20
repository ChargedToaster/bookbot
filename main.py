import sys
from stats import character_count
from stats import word_number
from stats import sort_list


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
        
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]  # Make sure this path is correct
    book_text = get_book_text(book_path)

    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: File not found at path '{book_path}'")
        sys.exit(1)

    
    # Get the word count
    word_count = word_number(book_text)
    
    # Get character frequencies
    char_freq = character_count(book_text)
    
    # Sort characters by frequency
    sorted_chars = sort_list(char_freq)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print only alphabetical characters
    for char_dict in sorted_chars:
        char = char_dict["char"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {char_dict['num']}")
    
    print("============= END ===============")


if __name__ == "__main__":
    main()

    