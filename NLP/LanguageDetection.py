from textblob import TextBlob
text = "Today is a beautiful day. Tomorrow looks like bad weather."
blob = TextBlob(text)
chinese = blob.translate(from_lang="en", to="de")
print(chinese)