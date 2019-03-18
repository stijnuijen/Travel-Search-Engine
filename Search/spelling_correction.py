from spellchecker import SpellChecker
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
tokens = tokenizer.tokenize('hapenning in paris')
spelling_correction = SpellChecker()
tokens2 = []
print(tokens)
for word in tokens:
    tokens2.append(spelling_correction.correction(word))
print(tokens2)