def count_words(text):
    words = text.split()
    return len(words)

def each_character_count(text):
    lowered_text = text.lower()
    char_count = {}
    for character in lowered_text:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1
    return char_count

def sort_on(items):
    return items['num']

def sorted_char_count(char_count):
    sorted_chars = []
    for key in char_count:
        if key.isalpha():
            sorted_chars.append({"char":key, "num": char_count[key]})
    
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars