def get_word_count(text):
    return len(text.split())

def char_count(text):
    char_count_dict = {}
    lowered = text.lower()
    for char in lowered:
        if char not in char_count_dict:
            char_count_dict[char] = 1
        else:
            char_count_dict[char] += 1
    return char_count_dict