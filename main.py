from stats import get_num_words, get_char_nums, sort_char_dict
import sys
def get_book_text(filePath):
    text = ""
    with open(filePath) as f:
        print(f"Analyzing book found at {filePath}...")
        text = f.read()
    
    return text



def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    text = get_book_text(book_path)
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