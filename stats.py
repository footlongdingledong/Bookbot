def num_of_words(file_contents):
    words = file_contents.split()
    y = len(words)
    print(f"Found {y} total words")
    return y


def char_count(file_contents):
    char_count = {}
    for char in file_contents:
        if char.isalpha():
            char = char.lower()
            char_count[char] = char_count.get(char, 0) + 1
    return char_count


def create_list(char_count):
    letters = []
    for char in char_count:
        num = char_count[char]
        x = {"char": char, "num": num}
        letters.append(x)
    return letters


def sort_on(letters):
    return letters["num"]


def sort_dict(letters):
    letters.sort(reverse=True, key=sort_on)
    return letters
