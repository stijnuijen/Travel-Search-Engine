import nltk
from requests import get
from requests.exceptions import RequestException
import os
from contextlib import closing
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

def htmls_to_title_strings(urls_file_dir):
    """ expects location of textfile containing URLs and returns 
    list of pure text strings from the corresponding HTML texts"""
    string_list = []
    url_dict = {}
    with open(urls_file_dir) as f:
        content = f.readlines()
    url_list = [line.strip() for line in content] 

    count = 0
    
    for url in url_list:
            if count == 1:
                break
            try: 
                html = get(url).content
            except:
                continue
            soup = BeautifulSoup(html, 'html.parser')

            # get text
            text = soup.find("title").get_text()    
            
            string_list.append(text)
            url_dict[text] = url

            count += 1

    return string_list, url_dict

def htmls_to_body_strings(urls_file_dir):
    """ expects location of textfile containing URLs and returns 
    list of pure text strings from the corresponding HTML texts"""
    string_list = []
    url_dict = {}
    with open(urls_file_dir) as f:
        content = f.readlines()
    url_list = [line.strip() for line in content] 

    count = 0
    
    for url in url_list:
            if count == 1:
                break
            try: 
                html = get(url).content
            except:
                continue
            soup = BeautifulSoup(html, 'html.parser')

            # kill all script and style elements
            for script in soup(["script", "style",'title']):
                script.extract()    # rip it out

            # get text
            text = soup.get_text()
            text = text.replace('\n',' ').encode('utf-8')
            print(text)

            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in text.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.encode('utf-8').strip() for line in lines for phrase in line.split("  "))
            # drop blank lines
            text = '\n'.join(str(chunk) for chunk in chunks if chunk)
            
            string_list.append(text)
            url_dict[text] = url

            count += 1

    return string_list, url_dict

def word_index(text):
    ''' Performs preprocessing on raw text and
     returns for every word a tuple (index, word)'''
    text = text.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    ps = nltk.PorterStemmer()
    words=[(index,ps.stem(word)) for index,word in enumerate(tokens)]
    filtered_words = [word for word in words if word not in stopwords.words('english')]

    return filtered_words

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
    for doc_id, doc in enumerate(docs):
        inverted = inverted_index_add(inverted, url_dict[doc], inverted_positions(doc))
    
    for word in inverted.values():
        for doc in word.values():
            doc.insert(0,(len(doc[0])))
            
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

# #title index
# print(create_inverted_index(htmls_to_title_strings('/Users/stijnuijen/Documents/MSc Data Science/Information Retrieval/Project/travelsearch/data/url_list.txt')))
# print('\n\n')
# #body index
# print(create_inverted_index(htmls_to_body_strings('/Users/stijnuijen/Documents/MSc Data Science/Information Retrieval/Project/travelsearch/data/url_list.txt')))

create_inverted_index(htmls_to_body_strings('/Users/stijnuijen/Documents/MSc Data Science/Information Retrieval/Project/travelsearch/data/url_list.txt'))

