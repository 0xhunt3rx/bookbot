from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    chars = get_num_chars(text)
    sorted_chars = get_sorted_chars(chars)

    length = len(get_num_words(text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {length} total words")
    print("--------- Character Count -------")
    for c in sorted_chars:
        if c["name"].isalpha():
            print(f"{c["name"]}: {c["num"]}")
    print("============= END ===============")

main()
