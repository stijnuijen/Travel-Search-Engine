import json
import csv

# this file splits the index up into equal parts: needs to be run N times, where N is the number of splits.

JSON_dir = "C:/Users/leonv/Documents/development/Master/Information_retrieval/clean_INDEX.json"
with open(JSON_dir) as f:
    INDEX = json.load(f)

# the remaining vocabulary 
words = sorted(list(INDEX.keys()))
print(1)
print("Length of words: ", len(words))

# cut in half for less memory:
def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

word1_2, word2_2 = split_list(words)
word1_4, word2_4 = split_list(word1_2)
word3_4, word4_4 = split_list(word2_2)

print(len(word1_2), len(word2_2))
print(len(word1_4),len(word2_4),len(word3_4),len(word4_4))

# change these for the current division
current_part = word4_4
part = "4_4"

sub_index = {}
for word in current_part:
     sub_index[word] = INDEX[word]

print("sub_index is of lenght: ", len(sub_index))

# export sub index 
with open( part + '_INDEX.json', 'w') as fp:
      json.dump(sub_index, fp)

# 1_4 done
# 2_4 done
# 3_4 done 
# 4_4 done