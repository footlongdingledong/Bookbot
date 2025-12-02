def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


import sys
from tokenize import NUMBER

from stats import char_count, create_list, num_of_words, sort_dict, sort_on


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        n = num_of_words(get_book_text(sys.argv[1]))
        t = char_count(get_book_text(sys.argv[1]))
        f = create_list(t)
        p = sort_dict(f)

        for i in p:
            val = i["num"]
            print(f"{i['char']}: {val}")


main()
