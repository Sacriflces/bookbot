def get_num_words(text):
    return len(text.split())

def get_char_nums(text):
    char_counts = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in char_counts:
            char_counts[char_lower] += 1
        else:
            char_counts[char_lower] = 1
    return char_counts

def sort_char_dict(dict):
    sorted_list = sorted([{key: value} for key, value in dict.items()], key=get_first_dict_value, reverse=True)

    return sorted_list

def get_first_dict_value(dict):
    if len(dict) == 0:
        return None
    return dict[list(dict)[0]]
    