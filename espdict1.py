import nltk
import wordbank
from nltk.tokenize import word_tokenize

def translate_nouns(word):
    if word in wordbank.nouns.keys():
        return wordbank.nouns[word]
    elif word in wordbank.nouns.values():
        val = word
        return list(wordbank.nouns.keys())[list(wordbank.nouns.values()).index(val)]
    else:
        return('unknown_word')
        

def set_ete(raw):
    text = nltk.tokenize.word_tokenize(raw)
    phrase = list(translate_nouns(w) for w in text)
    for w in phrase:
        print(w, end=' ')
