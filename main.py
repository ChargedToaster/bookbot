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

    book_path = sys.argv[1] 
    book_text = get_book_text(book_path)

    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: File not found at path '{book_path}'")
        sys.exit(1)

    word_count = word_number(book_text)
    
    char_freq = character_count(book_text)
    
    sorted_chars = sort_list(char_freq)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        if char.isalpha(): 
            print(f"{char}: {char_dict['num']}")
    
    print("============= END ===============")


if __name__ == "__main__":
    main()

    
