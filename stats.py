def get_num_words(text):
    return text.split()

def get_num_chars(text):
    chars = {}
    for c in text:
        c = c.lower()
        if c not in chars:
            chars[c] = 0
        chars[c] += 1
    return chars
