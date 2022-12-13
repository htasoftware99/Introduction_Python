import nltk
from textblob import TextBlob, Word
happy = Word("happy")
print(happy.definitions)
print(happy.synonyms)
print(happy.antonyms)