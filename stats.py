def sort_on(dct):
    return dct["num"]

def get_sorted_chars(dict_chars):
    lst = []
    for c in dict_chars:
        lst.append({"name": c, "num": dict_chars[c]})
    lst.sort(key=sort_on, reverse=True)
    return lst

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
