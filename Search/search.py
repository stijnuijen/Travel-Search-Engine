# this file is for search
import csv
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import numpy as np
import math


def l2_norm(a):  
    return math.sqrt(np.dot(a, a))

def cosine_similarity(a, b):
    return np.dot(a,b) / (l2_norm(a) * l2_norm(b))

def Search(query):

    # same preprocessing as in index creation:
    text = query.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    ps = nltk.PorterStemmer()
    words = [ps.stem(word) for word in tokens]
    stopset = set(stopwords.words('english'))
    words = [word for word in words if word not in stopset]

    # put the path of the folder with vectors file
    vectors_dir = "C:/Users/leonv/Documents/development/Master/Information_retrieval/clean_index.csv" 
    with open(vectors_dir, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for count, row in enumerate(csv_reader):
            words_vector = row[1:]
            break
    
    query_vector = []
    for word in words_vector:
        if word in words:
            query_vector.append(1)
        else:
            query_vector.append(0)

    top = []

    with open(vectors_dir, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for count, row in enumerate(csv_reader):
            try:
                url_vector = [float(i) for i in row[1:]]
                top.append([row[0], cosine_similarity(np.array(query_vector), np.array(url_vector))]) 
                print(count)
                if count == 3:
                    break
            except:
                continue

    return top
    

print(Search("Hello Worlds!"))