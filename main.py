import sys
from stats import number_of_words, number_of_characters, sort, print_report

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    contents = get_book_text(path)
    word_count = number_of_words(contents)
    character_count = number_of_characters(contents)
    sorted_chars = sort(character_count)
    print_report(path, word_count, sorted_chars)

main()
