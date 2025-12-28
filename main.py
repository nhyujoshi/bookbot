from stats import count_words, each_character_count, sorted_char_count
import sys

def main():
    book_path_input()
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    each_character = each_character_count(book_text)
    sorted_character = sorted_char_count(each_character)

    print_report(book_path, num_words, sorted_character)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(bookpath, num_words, sorted_character):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_character:
        print(f"{char_dict["char"]}: {char_dict["num"]}")

def book_path_input():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()