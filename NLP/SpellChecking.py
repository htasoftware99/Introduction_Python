from textblob import TextBlob, Word
word = Word("theyr")
print(word.spellcheck())
print(word.correct())