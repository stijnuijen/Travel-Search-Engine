import json
import math
import numpy as np
import pandas as pd
import gc
import nltk
from nltk.corpus import stopwords
from sys import getsizeof

# This preprocesses the INDEX so it becomes smaller

JSON_dir = "C:/Users/leonv/Documents/development/Master/Information_retrieval/INDEX.json"
with open(JSON_dir) as f:
    INDEX = json.load(f)

# remove all non relevent info from INDEX (to free memory)
for word, value in INDEX.items():
    for url in INDEX[word]:
        INDEX[word][url] = INDEX[word][url][2]

# remove stopwords:
stopwords = set(stopwords.words('english'))
for stopword in stopwords:
    if stopword in INDEX:
        INDEX.pop(stopword, None)

# remove words not starting with latin letter:
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(len(INDEX))
for k, v in list(INDEX.items()):
    if k[0] not in alphabet:
        if not k[0].isdigit():
         del INDEX[k]

with open('clean_INDEX.json', 'w') as fp:
      json.dump(INDEX, fp)