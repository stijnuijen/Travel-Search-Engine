import json
import nltk
import re
from nltk.corpus import stopwords
from sys import getsizeof
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from spellchecker import SpellChecker

# Create small DEMO inverted index for faster computation



JSON_dir = "C:/Users/leonv/Documents/development/Master/Information_retrieval/clean_INDEX.json"
with open(JSON_dir) as f:
    INDEX = json.load(f)

# give queries and process in same manner as in search
query = "Planning a trip Argentina Hanoi to Hue Vietnam Rome Italy Restaurants"
text = query.lower()
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(text)
spelling_correction = SpellChecker()
tokens2 = []
for word in tokens:
    tokens2.append(spelling_correction.correction(word))
ps = nltk.PorterStemmer()
words = [ps.stem(word) for word in tokens2]
stopset = set(stopwords.words('english'))
words = [word for word in words if word not in stopset]

demo_index = {}
for word in words:
    if word in INDEX:
        sub_index = {}
        for url in INDEX[word]:
                if not url.startswith("https://en.wikipedia.org"):
                        sub_index[url] = INDEX[word][url]
        demo_index[word] = sub_index

print(demo_index)
print("")
for i in demo_index:
        print(i)


with open('demo_INDEX.json', 'w') as fp:
      json.dump(demo_index, fp)