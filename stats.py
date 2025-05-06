def get_word_count(text):
    return len(text.split())

def char_count(text):
    char_count_dict = {}
    lowered = text.lower()
    sorted_list = {}
    for char in lowered:
        if char not in char_count_dict:
            char_count_dict[char] = 1
        else:
            char_count_dict[char] += 1

    return char_count_dict

def sort_on(dict):
    return dict["num"]

def sorted_dict(dict):
    new_chars_list = []

    for char, count in dict.items():
        new_chars_list.append({"char": char, "num": count})

    new_chars_list.sort(reverse=True, key=sort_on)

    for i in range(0,len(new_chars_list)):
        print(f"{new_chars_list[i]["char"]}: {new_chars_list[i]["num"]}")

    