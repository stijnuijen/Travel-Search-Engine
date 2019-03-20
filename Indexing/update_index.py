from Indexing_preprocessing import create_inverted_index

def update_index(urls_file_dir):
    """ expects location of textfile containing URLs, dir of the current index,
    and 
    
     and returns 
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
