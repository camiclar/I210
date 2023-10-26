def read_words(path):
    with open(path, "r") as wordsFile:
        lines = wordsFile.readlines()

    lines = [line.strip() for line in lines]
    return lines

def get_p_words(words):
    p_words = []

    for word in words:
        try:
            word[0].lower() == "p"
            p_words.append(word)
        except:
            

    
if __name__ == "__main__":
    words = read_words("words.txt")
    print(get_p_words(words))
