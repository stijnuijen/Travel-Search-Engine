import nltk
from requests import get
from requests.exceptions import RequestException
import os
from contextlib import closing
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

def htmls_to_strings(urls_file_dir):
    """ expects location of textfile containing URLs and returns 
    list of pure text strings from the corresponding HTML texts"""
    string_list = []
    url_dict = {}
    with open(urls_file_dir) as f:
        content = f.readlines()
    url_list = [line.strip() for line in content] 

    count = 0
    
    for url in url_list:
            if count == 3:
                break
            try: 
                html = get(url).content
            except:
                continue
            soup = BeautifulSoup(html, 'html.parser')

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
    new_dict = {}
    for key, value in index1.items():

        for key2, value2 in index2.items():

            if key == key2:
                # combine value1 and value2
                same_term_dict = {}
                for key, value in index1[key].items():
                    same_term_dict[key] = value

                for key, value in index2[key2].items():
                    same_term_dict[key] = value 
            else:
                new_dict[key] = value
    
    # add remaining words from index2
    for key2, value2 in index2.items():
        if key2 not in new_dict:
            new_dict[key2] = value2
    return new_dict

    
                
   

doc1='In a speech to senior Russian officials in Moscow, Putin said the possible deployment of missiles that could reach Moscow in 10 minutes was dangerous for Russia,and that Moscow would be forced to review symmetrical and asymmetrical actions'

doc2=' In Russia will Moscow be forced to create and deploy types of weapons, which can be used not just against those territories, from which the direct threat will come, but also against those, where the centres of decision-making for using these missile systems will come,the Russian president said'

doc3='The treaty, concluded by Ronald Reagan and Mikhail Gorbachev, banned the development and deployment of land-based missiles with a range of 500-5,500km and was widely credited with banishing nuclear missiles from Europe. The US, led by the national security adviser, John Bolton'


# print(create_inverted_index(htmls_to_strings("url_list_large.txt")))

# update 
pc1 = inverted_index_add({}, 'doc1', inverted_positions(doc1))
pc2 = inverted_index_add({}, 'doc2', inverted_positions(doc2))
print(merge_indices(pc1,pc2))

