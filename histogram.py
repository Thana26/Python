word="thana"
dict={}
for keys in word:
    dict[keys]=dict.get(keys,0)+1
print("histogram of frequency of characters in given word:\n",str(dict))
