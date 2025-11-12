sorted = [{'char': ' ', 'num': 70480}, {'char': 'e', 'num': 44538}, {'char': 't', 'num': 29493}]

def print_report(path, words_no, list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_no} total words")
    print("--------- Character Count -------")
    for dictionary in list:
        if dictionary["char"].isalpha():
            print(f"{dictionary["char"]}: {dictionary["num"]}")
    print("============= END ===============")
print_report("books/frankenstein.txt", 75767, sorted)