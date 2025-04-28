from stats import get_num_words

def get_book_text(filePath):
    text = ""
    with open(filePath) as f:
        text = f.read()
    
    return text



def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()