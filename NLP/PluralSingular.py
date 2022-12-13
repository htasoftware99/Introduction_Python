from textblob import Word
from textblob import TextBlob
index = Word("index")
print(index.pluralize())
cacti = Word("cacti")
print(cacti.pluralize())

animals = TextBlob("dog, cat, fish, bird").words
print(animals.pluralize())