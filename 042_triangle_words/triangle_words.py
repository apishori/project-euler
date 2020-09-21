def triangleWords(file_name):
    words_file = open(file_name, 'r')
    wordstr = words_file.read()
    words = wordstr.split()
    print(words)
    return len(words)

if __name__ == "__main__":
    print(triangleWords('042_triangle_words/words.txt'))
