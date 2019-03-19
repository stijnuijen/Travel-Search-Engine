# this file is for search
import csv
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from spellchecker import SpellChecker
import numpy as np
import math
import json
import operator
import time
    
tokenizer = RegexpTokenizer(r'\w+')
text='Holidaay in Vietnam!'
print(text)
text = text.lower()
print(text)
tokens = tokenizer.tokenize(text)
print(tokens)
spelling_correction = SpellChecker()
tokens2 = []
for word in tokens:
    tokens2.append(spelling_correction.correction(word))

print(tokens2)