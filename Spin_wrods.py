
def spin_words(sentence):
    res = []
    words_list = sentence.split(" ")
    for elem in words_list:
        if len(elem) > 4:
            res.append(elem[::-1])
        else: res.append(elem)
    return ' '.join(res)

print(spin_words("This is a test"))

# В одну строчку

def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

# в три строки
def spin_words(sentence):
    words = [word for word in sentence.split(" ")]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)