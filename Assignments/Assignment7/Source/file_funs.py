import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import string
text1 = ""
fr = open("sample").read()

sw = set(stopwords.words('english'))            #stop words
for s in fr.lower().split():
    if s not in sw:
        text1 = text1 + ' ' + s
print ("Data after removing the stop words:")
print (text1)
print(" ")


puncs = set(string.punctuation)               #punction removal
text2 = ''.join(s for s in text1 if s not in puncs)
print ("Data After Removing The Punctions:")
print(text2)
print(" ")

t = word_tokenize(text2)                 #tokenzing the data
rv = nltk.pos_tag(t)
rv = nltk.pos_tag(t)
text3 = []
for p in rv:
    if 's' not in p[1]:
        text3.append(p[0])
print ("Data After Removing Verbs:")
print (text3)
print(" ")

#counting the frequency
summary = ""
freq = Counter(text3).most_common(5)
print("Most Frequent Words:")
print (freq)
print(" ")


# summarizing the text
for most in freq:
    for rew in sent_tokenize(fr.lower()):
        if rew not in summary:
            if most[0] in word_tokenize(rew):
                summary = summary + rew
print("Sentences with frequent words:")
print(summary)
print(" ")

