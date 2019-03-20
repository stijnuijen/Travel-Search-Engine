from requests import get
from bs4 import BeautifulSoup
import json

def htmls_to_title_strings(urls_file_dir):
    """ expects location of textfile containing URLs and returns 
    list of pure text strings from the corresponding HTML texts"""
    string_list = []
    url_dict = {}
    with open(urls_file_dir) as f:
        content = f.readlines()
    url_list = [line.strip() for line in content] 

    lenght = len(url_list)
    count = 0
    for url in url_list:
            
            try:
                html = get(url).content
                soup = BeautifulSoup(html, 'html.parser')

                # get text
                text = soup.find("title").get_text()    
                
                url_dict[url] = text
            except:
                continue 
            count += 1
            if count % 1000 == 0:
                print("processed ", count, " of ", lenght, " urls.")


    return url_dict

title_index = htmls_to_title_strings('C:/Users/leonv/Documents/development/Master/Information_retrieval/travelsearch/data/url_list_large.txt')

print("length of title dict: ", len(title_index))

with open('index_titles.json', 'w') as fp:
    json.dump(title_index, fp)