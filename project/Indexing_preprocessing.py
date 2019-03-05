import nltk
from requests import get
from requests.exceptions import RequestException
import os
from contextlib import closing
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import time


def htmls_to_strings(urls_file_dir):
    """ expects location of textfile containing URLs and returns 
    list of pure text strings from the corresponding HTML texts"""
    string_list = []
    url_dict = {}
    all_info_dict = {}

    with open(urls_file_dir) as f:
        content = f.readlines()
    url_list = [line.strip() for line in content] 

    count = 0
    
    for url in url_list:
            
            # if count ==  3:
            #     break
            try: 
                html = get(url).content
            except:
                continue
            
            soup = BeautifulSoup(html, 'html.parser')
            
            info_of_page = {'url': url, 
                'title': soup.find('title').get_text(),
                'text': None, # add these
                'score': None # two later
                }

            # kill all script and style elements
            for script in soup(["script", "style"]):
                script.extract()    # rip it out
            # get text
            text = soup.get_text()
            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in text.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # drop blank lines
            text = '\n'.join(chunk for chunk in chunks if chunk)
            text = text.replace("\n"," ")
            
            # add text to page dict
            info_of_page["text"] = text

            # add info to right dataobjects 
            string_list.append(text)
            url_dict[text] = url
            all_info_dict[url] = info_of_page

            # increment count
            count += 1

    # print(all_info_dict)
    print("done with extracting from HTMLs.")
    print("")
    return string_list, url_dict, all_info_dict

def word_index(text):
    ''' Performs preprocessing on raw text and
     returns for every word a tuple (index, word)'''
    text = text.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    ps = nltk.PorterStemmer()
    words=[(index,ps.stem(word)) for index,word in enumerate(tokens)]
    # filtered_words = [word for word in words if word not in stopwords.words('english')]

    return words

def inverted_positions(text):
    '''returns for every word a dictionary, where the word is the key,
    and the value contains a list of positions of that word in this document'''
    inverted = {}
    for index, word in word_index(text):
       locations = inverted.setdefault(word, [[]])
       locations[0].append(index)
    return inverted

def inverted_index_add(inverted, doc_id, doc_index):
    '''adds a new document to the inverted index'''
    for word, locations in doc_index.items():
        indices = inverted.setdefault(word, {})
        indices[doc_id] = locations
    return inverted

def create_inverted_index(tpl):
    '''takes a list of documents/strings and dictionary 
    with text:url as input and outputs an inverted index'''
    docs, url_dict = tpl[0], tpl[1]
    inverted = {}
    start_time = time.time()

    for doc_id, doc in enumerate(docs):
        inverted = inverted_index_add(inverted, url_dict[doc], inverted_positions(doc))
    print("create_inverted_index loop 1 --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    
    for word in inverted.values():
        for doc in word.values():
            doc.insert(0,(len(doc[0])))
    print("create_inverted_index loop 2 --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
            
    return inverted

def merge_indices(index1, index2):
    """ function that merges two existing indices """
    new_dict = {}
    for word1, docs1 in index1.items():
        for word2, docs2 in index2.items():
            if word1 == word2:
                # combine value1 and value2
                same_term_dict = {}
                for url1, value in index1[word1].items():
                    same_term_dict[url1] = value
                for url2, value in index2[word1].items():
                    same_term_dict[url2] = value 
                new_dict[word1] = same_term_dict
    
    # add words from index1 not in index2
    for word1, docs1 in index1.items():
         if word1 not in new_dict:
            new_dict[word1] = docs1

    # add remaining words from index2
    for key2, value2 in index2.items():
        if key2 not in new_dict:
            new_dict[key2] = value2
    
    return new_dict



def add_TFIDF_as_score(input_tpl):
    """ takes tuple where 1) a list of strings and 2) dictionary where 
    keys are these strings and the value is the corresponding url
    and returns a inverted index with TF-IDF scores instead of mere 
    term frequencies"""
    
    import math
    start_time = time.time()

    # structure of inv_index:
    # {word1: {url: [frequency_in_doc [index1, index2]]}}

    inv_index = create_inverted_index(input_tpl)
    print("create_inverted_index --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    
    final_TFIDF = inv_index.copy()
    print("copy index --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    
    tf_idf_info = {}

    doc_freqs = {}

    # determine all unique urls
    for word in inv_index:
        for url in inv_index[word]:
            if url not in tf_idf_info:
                tf_idf_info[url] = {'length': None, 'word_freqs': {}}
    print("determine all unique urls --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()

    # determine document lengths:
    for url in tf_idf_info:
        N = 0
        for word in inv_index:
            for suburl in inv_index[word]:
                if url == suburl:
                    N += inv_index[word][url][0]
        tf_idf_info[url]['length'] = N
    print("determine document lengths --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()

    # add term frequencies:
    for word in inv_index:
        for url in inv_index[word]:
            if word not in tf_idf_info[url]['word_freqs']:
                tf_idf_info[url]['word_freqs'][word] = inv_index[word][url][0]
    print("add term frequencies --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
            
    # calculate TF 
    for url in tf_idf_info:
        for word in tf_idf_info[url]['word_freqs']:
            tf_idf_info[url]['word_freqs'][word] = tf_idf_info[url]['word_freqs'][word] / tf_idf_info[url]['length']
    print("calculate TF --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()

    # determine document frequencies:
    for word in inv_index:
        doc_freqs[word] = len(inv_index[word])
    print("determine document frequencies --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()

    # transgrom DF to IDF:
    N_docs = len(tf_idf_info)
    for word in doc_freqs:
        doc_freqs[word] = math.log10(N_docs/ doc_freqs[word])
    print("transgrom DF to IDF --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    
    # create inverted index with TFIDF score
    for word in final_TFIDF:
        for url in final_TFIDF[word]:
            final_TFIDF[word][url].append(tf_idf_info[url]['word_freqs'][word] * doc_freqs[word])
    print("create inverted index with TFIDF score --- %s seconds ---" % (time.time() - start_time))

    return final_TFIDF


print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")


# s1 = "The wolf ate bunny"
# s2 = "The other animal ate"
# s3 = "I ate the bunny"
# string_list = [s1, s2, s3]
# url_dict = {s1: "url1", s2: "url2", s3: "url3"}
# tpl = (string_list, url_dict)

import time
main_start_time = time.time()

## Uncommend the following lines to create the INDEX
# index = add_TFIDF_as_score(htmls_to_strings("C:/Users/leonv/Documents/development/Master/Information_retrieval/travelsearch/data/url_list_large.txt"))

# import json

# with open('INDEX.json', 'w') as fp:
#     json.dump(index, fp)

# # print(add_TFIDF_as_score(tpl))
print("WHOLE PROGRAM: --- %s seconds ---" % (time.time() - main_start_time))

###########################################################
# 250 pages
# 3 pages (mode 2 battery): 9.22
# 3 pages (mode max battery): 6.59
# 20 pages (mode max battery): 65.39
# 100 pages (mode max battert): 455.96

# done with extracting from HTMLs.

# create_inverted_index --- 870.0871112346649 seconds ---
# copy index --- 0.007985115051269531 seconds ---
# determine all unique urls --- 0.0559229850769043 seconds ---
# determine document lengths --- 10.653752088546753 seconds ---
# add term frequencies --- 0.34355902671813965 seconds ---
# calculate TF --- 0.17574596405029297 seconds ---
# determine document frequencies --- 0.039981842041015625 seconds ---
# transgrom DF to IDF --- 0.039946556091308594 seconds ---
# create inverted index with TFIDF score --- 0.3634827136993408 seconds ---

# WHOLE PROGRAM: --- 962.4146590232849 seconds ---
###########################################################


###################################################################################
# final run on all pages:
###################################################################################
# create_inverted_index loop 1 --- 1491.6805884838104 seconds ---
# create_inverted_index loop 2 --- 36.60852074623108 seconds ---
# create_inverted_index --- 1528.3203649520874 seconds ---
# copy index --- 5.271369457244873 seconds ---
# determine all unique urls --- 3.2301249504089355 seconds ---
# determine document lengths --- 33773.14522647858 seconds ---
# add term frequencies --- 46.695765018463135 seconds ---
# calculate TF --- 8.017558574676514 seconds ---
# determine document frequencies --- 0.44992995262145996 seconds ---
# transgrom DF to IDF --- 0.36842894554138184 seconds ---
# create inverted index with TFIDF score --- 111.9523937702179 seconds ---
# WHOLE PROGRAM: --- 74847.1893670559 seconds ---
###################################################################################


