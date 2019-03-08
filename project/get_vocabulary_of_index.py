import json
import csv

# ecxtract vocab of index and export as csv file 

JSON_dir = "C:/Users/leonv/Documents/development/Master/Information_retrieval/clean_INDEX.json"
with open(JSON_dir) as f:
    INDEX = json.load(f)

# the remaining vocabulary 
words = sorted(list(INDEX.keys()))

with open("vocabulary.csv", "w", encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows([words])
