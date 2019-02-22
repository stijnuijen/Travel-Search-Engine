import nltk

def word_index(text):
    '''returns for every word a tuple (index, word)'''
    tokens = nltk.word_tokenize(text)
    words=[(index,word) for index,word in enumerate(tokens)]
    return words

def inverted_positions(text):
    '''returns for every word a dictionary, where the word is the key,
    and the value contains a list of positions of that word in this document'''
    inverted = {}
    for index, word in word_index(text):
        locations = inverted.setdefault(word, [])
        locations.append(index)
    return inverted

def inverted_index_add(inverted, doc_id, doc_index):
    '''adds a new document to the inverted index'''
    for word, locations in doc_index.items():
        indices = inverted.setdefault(word, {})
        indices[doc_id] = locations
    return inverted

def create_inverted_index(docs):
    '''takes a list of documents/strings as input and outputs an inverted index'''
    inverted = {}
    for doc_id, doc in enumerate(docs):
        inverted = inverted_index_add(inverted, 'doc' + str(doc_id), inverted_positions(doc))
    
    return inverted

doc1='In a speech to senior Russian officials in Moscow, Putin said the possible deployment of missiles that could reach Moscow in 10 minutes was dangerous for Russia,and that Moscow would be forced to review symmetrical and asymmetrical actions'

doc2='Russia will Moscow be forced to create and deploy types of weapons, which can be used not just against those territories, from which the direct threat will come, but also against those, where the centres of decision-making for using these missile systems will come,the Russian president said'

doc3='The treaty, concluded by Ronald Reagan and Mikhail Gorbachev, banned the development and deployment of land-based missiles with a range of 500-5,500km and was widely credited with banishing nuclear missiles from Europe. The US, led by the national security adviser, John Bolton'


print(create_inverted_index([doc1,doc2,doc3]))
