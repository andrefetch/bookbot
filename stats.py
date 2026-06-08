def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    
    return contents


def get_num_words(filename):

    counter = 0

    for words in get_book_text(filename).split():
        counter += 1

    return counter

def get_each_char(filename):

    letter_dict = {}

    characters = get_book_text(filename).lower()

    for letters in characters:
        if letters in letter_dict:
            letter_dict[letters] += 1
        else:
            letter_dict[letters] = 1
    
    return letter_dict

def sort_on(item):
    
    return item["num"]

def dict_to_sorted(chars_dict):

    sort_list = []

    for char, count in chars_dict.items():
        
        sort_list.append({
            "char": char,
            "num": count
        })

    sort_list.sort(reverse=True, key=sort_on)
    return sort_list

def sort_on(char: tuple[str, int]):
    
    return char[1]

def chars_dict_to_sorted_list(chars_dict: dict[str, int]) -> list[tuple[str, int]]:

    sorted_list = []

    for char in chars_dict:
        count = chars_dict[char]
        sorted_list.append((char, count))

    return sorted(sorted_list, key=sort_on, reverse=True)

