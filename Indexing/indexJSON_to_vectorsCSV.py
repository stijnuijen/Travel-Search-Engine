import json 
import csv
from random import shuffle

JSON_dir = "C:/Users/leonv/Documents/development/Master/Information_retrieval/clean_INDEX.json" 
with open(JSON_dir) as f:
    INDEX = json.load(f)

url_dir = "C:/Users/leonv/Documents/development/Master/Information_retrieval/urls_in_order.csv" 
with open(url_dir) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    urls = []
    for row in csv_reader:
        if len(row) > 0:
            urls.append(row)

shuffle(urls[0])
urls = urls[0][:1000]
words = sorted(list(INDEX.keys()))
   

print(len(urls))
f = open('clean_index.csv','w', encoding='utf-8')
f.write("urls," + ",".join(words)+"\n") #Give your csv text here.
## Python will convert \n to os.linesep
f.close()

count = 0
for url in urls:
    frequency_vector = []
    for word in words:
        try:
            frequency_vector.append(float(INDEX[word][url]))
        except:
            frequency_vector.append(0)

    number_strings = ['{:.5f}'.format(x) if not isinstance(x, int) else str(int(x)) for x in frequency_vector]
    number_strings = ['{:.5f}'.format(x) if not '{:.6f}'.format(x) == "0.00000" else str(int(x)) for x in frequency_vector]
    string = url + "," + ",".join(number_strings) + "\n"
    f = open('clean_index.csv','a', encoding='utf-8')
    f.write(string) #Give your csv text here.
    ## Python will convert \n to os.linesep
    f.close()
    count += 1
    if count % 100 == 0: 
        print(count, " of ", len(urls), " urls processed.")












# 5 digits, 67 kb 
# 10 digits, 98 kb