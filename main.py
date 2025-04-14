from stats import *
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    chars = get_num_chars(text)
    sorted_chars = get_sorted_chars(chars)

    length = len(get_num_words(text))


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {length} total words")
    print("--------- Character Count -------")
    for c in sorted_chars:
        if c["name"].isalpha():
            print(f"{c["name"]}: {c["num"]}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

main()
