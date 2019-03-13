import json
import math
import numpy as np
import pandas as pd
import gc
import nltk
from nltk.corpus import stopwords
from sys import getsizeof
import csv

# this file needs pre extracted vocabulary of the entire index and 
# a sub index as input. It will create the word frequencies for the
# given sub index as a word frequency matrix.

part = "1_4" # for naming the csv file in the end
sub_index = "1_4_INDEX.json"
JSON_dir = "C:/Users/leonv/Documents/development/Master/Information_retrieval/" + sub_index
with open(JSON_dir) as f:
    INDEX = json.load(f)

url_dir = "C:/Users/leonv/Documents/development/Master/Information_retrieval/urls_in_order.csv" 
with open(url_dir) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    urls = []
    for row in csv_reader:
        if len(row) > 0:
            urls.append(row)
urls = urls[0]

# the sub vocabulary 
words = sorted(list(INDEX.keys()))

print("Length of words: ", len(words))

# for each word create a list with tf-idf values per document: frequency matrix

vector = []
for url in urls:
    try:
        vector.append(float(INDEX[words[0]][url]))
    except:
        vector.append(0)

frequency_matrix = np.array([vector])
count = 0
length = len(words)

for word in words[1:]:
    frequency_vector = []
    for url in urls:
        try:
            frequency_vector.append(float(INDEX[word][url]))
        except:
            frequency_vector.append(0)
    frequency_matrix = np.append(frequency_matrix, [frequency_vector], axis=0)

    count += 1
    if count % 5000 == 0:
        print(count, " of ", length, " words processed.")

# see: http://www.sfs.uni-tuebingen.de/~ddekok/ir/lectures/tf-idf-dump.html
x = np.array(frequency_matrix) 
index_df = pd.DataFrame(x, index = words, columns = urls)

file_name = "TFIDF_vectors_DF_" + part  
index_df.to_csv(file_name, sep=',', encoding='utf-8')







