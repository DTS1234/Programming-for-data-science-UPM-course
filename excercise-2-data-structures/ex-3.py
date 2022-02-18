# Represent a small bilingual lexicon as a Python dictionary in the following fashion:
#   merry -> feliz
#   christmas -> Navidad
#   and -> y
#   happy -> próspero
#   new -> nuevo
#   year -> año

# and use it to translate your Christmas cards from English.

# That is, write two functions:
#   1. readSentence() that reads an English sentence from user
#   (standard) input and returns a list with the words
#   - Tip: Check previous slides for User I/O and String operations
#   2. translate() that takes the list of English words and returns a list of Spanish words
#   NOTE: choose any other target language instead of Spanish, if you wish

eng_pol_dictionary = {'merry':'wesolych', "christmas" : "swiat", "and" : "i", "happy" : "szczesliwego", "new" : "nowego", "year":"roku"}

def readSentence():
    return input("enter sentence : ").split(" ")

def translate(words):
    translated = []
    for word in words:
        translated.append(eng_pol_dictionary[word])
    return translated

print(translate(readSentence()))
