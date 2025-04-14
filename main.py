from stats import get_num_words, get_num_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    chars = get_num_chars(text)
    length = len(get_num_words(text))

    print(f"{length} words found in the document")
    for c in chars:
        print(f"'{c}': {chars[c]}")

main()
