import definition as definition
import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from nltk import pos_tag,ne_chunk
import numpy
#nltk.download('all')

ps = SnowballStemmer('english')


desc=wn.synsets('phone')
for a in desc:
    print (a.definition())
    print("/n")


print("3.Apply Tokenization on the text")
file = open("sample").read()
print file
token=nltk.word_tokenize(file)
print (nltk.word_tokenize(file))

print("4.Apply Stemming on the text")
for w in file.split():
    print (w+" : "+ps.stem(w))

print("5.Apply POS on the text")
print nltk.pos_tag(token)

print("5.Apply Lemmatization on the text")
wnl = WordNetLemmatizer()
print(wnl.lemmatize('loving', pos='v'))

print("6.Apply ngram on the text")
n = 3
sixgrams = ngrams(file.split(), n)
for grams in sixgrams:
  print grams

print('8.Apply Named Entity Recognition on the text')
print(ne_chunk(pos_tag(token)))


