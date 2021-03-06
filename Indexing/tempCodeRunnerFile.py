def htmls_to_title_strings(urls_file_dir):
    """ expects location of textfile containing URLs and returns 
    list of pure text strings from the corresponding HTML texts"""
    string_list = []
    url_dict = {}
    with open(urls_file_dir) as f:
        content = f.readlines()
    url_list = [line.strip() for line in content] 

    for url in url_list:

            html = get(url).content
            soup = BeautifulSoup(html, 'html.parser')

            # get text
            text = soup.find("title").get_text()    
            
            url_dict[url] = text

            count += 1

    return url_dict

print(htmls_to_title_strings('/Users/stijnuijen/Documents/MSc Data Science/Information Retrieval/Project/travelsearch/data/url_list_large.txt'))
