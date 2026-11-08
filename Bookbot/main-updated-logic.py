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
    if book_path.endswith(".txt"):
        try:
            text = get_book_text(book_path)
        except FileNotFoundError:
            print(f"Error: could not find file {book_path} please ensure the file is correct")
            sys.exit(1)
    else:
        print(f"Error: {book_path} is not a .txt file. Please ensure submitted file is a .txt")
        print("Also .txt is case sensative and I am too lazy to update it so ensure you lowercase your .TXT file")
        sys.exit(1)
    splity = get_num_words(text)
    char_count = get_char_count(text)
    final_sort = chars_dict_to_sorted_list(char_count)

    print_report(book_path, splity, final_sort)

main()
