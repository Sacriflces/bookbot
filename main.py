def get_book_text(filePath):
    text = ""
    with open(filePath) as f:
        text = f.read()
    
    return text

def get_book_word_num(text):
    return len(text.split())

def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = get_book_word_num(text)
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()