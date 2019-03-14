# this file is for search
import csv
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import numpy as np
import math
import json
import operator



def l2_norm(a):  
    return math.sqrt(np.dot(a, a))

def cosine_similarity(a, b):
    return np.dot(a,b) / (l2_norm(a) * l2_norm(b))

def Search(query):

    JSON_dir = "C:/Users/leonv/Documents/development/Master/Information_retrieval/clean_INDEX.json" 
    with open(JSON_dir) as f:
        INDEX = json.load(f)

    # same preprocessing as in index creation:
    text = query.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    ps = nltk.PorterStemmer()
    words = [ps.stem(word) for word in tokens]
    stopset = set(stopwords.words('english'))
    words = [word for word in words if word not in stopset]
    freq_dict = {i:words.count(i) for i in set(words)}

    # create query vector with tfidf values:
    N_docs = 36091
    query_vector = []
    for word in freq_dict:
        tf = freq_dict[word] / len(words)
        try:
            df = len(INDEX[word]) + 1
        except:
            df = 1
        idf = math.log10(N_docs/ df)
        query_vector.append(tf*idf)
    query_vector = np.array(query_vector)

    # determine pages with at least one word from the query
    pages_with_words = []
    for word in freq_dict:
        try:
            for url in INDEX[word]:
                if url not in pages_with_words:
                    pages_with_words.append(url)
        except:
            continue
    
    # create tfidf vectors of those pages and 
    # calculate the cosine simularity
    page_distance_to_query = {}
    for url in pages_with_words:
        page_vector = []
        for word in freq_dict:
            try:
                page_vector.append(float(INDEX[word][url]))
            except:
                page_vector.append(0)
        page_vector = np.array(page_vector)
        page_distance_to_query[url] = cosine_similarity(query_vector, page_vector)


    return sorted(page_distance_to_query.items(), key=operator.itemgetter(1))

    

print(Search("Street Food in Hanoi"))