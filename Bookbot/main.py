import sys

def have_book():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

from stats import get_num_words
from stats import get_char_count
from stats import chars_dict_to_sorted_list

def print_report(book_path, splity, final_sort):
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book_path + "...")
    print("----------- Word Count ----------")
    print(f"Found {splity} total words")
    print("--------- Character Count -------")
    for letter in final_sort:
        if letter[0].isalpha() is True:
            print(f'{letter[0]}: {letter[1]}')
    print("============= END ===============")

def main():
    have_book()
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    splity = get_num_words(text)
    char_count = get_char_count(text)
    final_sort = chars_dict_to_sorted_list(char_count)

    print_report(book_path, splity, final_sort)

main()
