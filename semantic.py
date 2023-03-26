# Note1: I found it interesting because it can relate two words with no direct relationship eg. diet

# Note2: On average, there were smaller correlation coefficients.

import spacy
nlp = spacy.load('en_core_web_m')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))