import json
import csv

# ecxtract urls of index and export as csv file 

JSON_dir = "C:/Users/leonv/Documents/development/Master/Information_retrieval/INDEX.json"
with open(JSON_dir) as f:
    INDEX = json.load(f)

# determine all unique urls
pages = []
count = 0
for word in INDEX:
    for url in INDEX[word]:
        if url not in pages:
            pages.append(url)
    
    print(len(pages))
        
pages = sorted(pages)

print(len(pages), " url pages")

with open("urls_in_order.csv", "w", encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows([pages])
