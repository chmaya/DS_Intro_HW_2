# shmaya gabriel adda 315701847

#A

def reverse (sentence, reverse_word):
    if type(reverse_word) != str:
        return print("invalid input")
    list = sentence.split()
    for word in list:
        if word == reverse_word:
            reverse_word_new = reverse_word[::-1]
            break
        else:
            return print("no match word found")
    new_sentence = sentence.replace(reverse_word,reverse_word_new,1)
       
    return new_sentence
        



