from nltk.corpus import brown
from random import randint, shuffle, choice

word_list = list(set(brown.words()))
words = []

for i in range(280):
    words.append(choice(word_list))

print(words)

