def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_characters(text):
    character_count = {}
    for char in text.lower():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort(dictionary):
    list = []
    for d in dictionary:
        list.append({"char": d, "num": dictionary[d]})

    def sort_on(items):
        return items["num"]
    
    list.sort(reverse = True, key = sort_on)
    return list

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