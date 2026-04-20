import sys
from stats import get_num_words, get_each_char, dict_to_sorted, get_book_text, sort_on

def main():
    if len(sys.argv) >= 2:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(sys.argv[1])} total words")
        print("--------- Character Count -------")
    
        for item in dict_to_sorted(get_each_char(sys.argv[1])):
            if item["char"].isalpha():
                print(f"{item['char']}: {item['num']}")
    
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()