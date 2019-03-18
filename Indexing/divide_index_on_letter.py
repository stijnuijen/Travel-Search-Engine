import json

# this file divides the huge INDEX into one index per letter and one for other characters 
# and writes them to JSON files

# Load the INDEX
JSON_dir = ""
with open(JSON_dir) as f:
    INDEX = json.load(f)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


index_per_letter = {}

for letter in alphabet:
    index_per_letter[letter] = {}

index_per_letter["_"] = {}

for word, value in INDEX.items():
    if word[0] not in alphabet:
        index_per_letter["other"][word] = value
    else:
        index_per_letter[word[0]][word] = value

for key, value in index_per_letter.items():
    print(key, len(value))
    
    with open( key + '_INDEX.json', 'w') as fp:
      json.dump(value, fp)

