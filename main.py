import sys
from stats import get_num_words, get_each_char, dict_to_sorted, get_book_text, sort_on, chars_dict_to_sorted_list

def main():
    book_path = sys.argv[1] if len(sys.argv) >= 2 else "books/frankenstein.txt"

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_path)} total words")

    sorted_list = chars_dict_to_sorted_list(get_each_char(book_path))
    print(sorted_list)

    print("--------- Character Count -------")

    for item in dict_to_sorted(get_each_char(book_path)):
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()