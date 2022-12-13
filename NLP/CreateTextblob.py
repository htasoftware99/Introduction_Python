from textblob import TextBlob
import textblob
text = "Today is a beautiful day. Tomorrow looks like bad weather."
blob = TextBlob(text)
#print(blob.sentences) 
#print(blob.words) 
#print(blob.tags)
#print(blob.noun_phrases) 
print(blob.sentiment.polarity)
print(blob.sentiment.subjectivity)