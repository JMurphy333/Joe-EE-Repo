def get_num_words(text):
    words = text.split()
    splity = len(words)
    return splity


def get_char_count(text):
    characters = text.lower()
    char_count = {}
    for char in characters:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sort_on(char_count: tuple[str, int]) -> int:
    return char_count[1]

def chars_dict_to_sorted_list(char_count):
    sorted_list = []
    for char in char_count:
        char_tuple = (char, char_count[char])
        sorted_list.append(char_tuple)
    final_sort = sorted(sorted_list, reverse=True, key=sort_on)
    return final_sort
