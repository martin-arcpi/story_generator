from nltk.corpus import brown
from random import randint, shuffle, choice


# TODO add varying length sentences using a for loop to create a paragraph simulating a twitter message.


def generate_text():
    word_list = list(set(brown.words()))
    words = [choice(word_list) for i in range(280)]

    sentences = []
    text = ''

    for i in range(20):
        for j in range(randint(1, 10)):
            text += choice(words)
            text += ' '
        sentences.append(text)
        text = ''

    print(sentences )
            
    

print(generate_text())


