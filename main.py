from stats import get_num_words, get_char_nums, sort_char_dict

def get_book_text(filePath):
    text = ""
    with open(filePath) as f:
        print(f"Analyzing book found at {filePath}...")
        text = f.read()
    
    return text



def main():
    print("============ BOOKBOT ============")
    text = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_nums = get_char_nums(text)
    sorted_char_list = sort_char_dict(char_nums)
    print("--------- Character Count -------")
    for charDict in sorted_char_list:
        for char, count in charDict.items():
            if not char.isalpha():
                continue
            print(f"{char}: {count}")

if __name__ == "__main__":
    main()