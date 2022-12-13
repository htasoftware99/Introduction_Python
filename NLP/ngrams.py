from textblob import TextBlob, Word
text = "Today is a good day. The weather is nice today. The weather is nice today."
blob = TextBlob(text)
print(blob.ngrams(6))