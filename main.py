def to_words(text):
    return text.split()

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    length = len(to_words(text))
    print(f"{length} words found in the document")

main()
