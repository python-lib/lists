

def words(letters, string):
    word_length = []
    sentence = string.split(" ")
    for x in sentence:
        if len(x) > letters:
            word_length.append(x)
    return word_length


