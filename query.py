import json
import pickle
from Trie import Node, TrieObject

def dfs(node, word):
    if node.isEnd:
        queryWords.append(word)
    for i in node.children:
        dfs(node.children[i], word+i)

def searchTrie():
    s = query[:-1]
    node = trie.root
    for i in range(0, len(s)):
        c = s[i]
        if c not in node.children:
            return
        node = node.children[c]

    dfs(node, s)


# get the query from the user
query = input("Enter your query: ")

# load trie and invertedIndex

with open("trie.pickle","rb") as infile:
    trie = pickle.load(infile)

with open("inverted_index.json", "r") as infile:
    invertedIndex = json.load(infile)

# determine queryWords
# if there is star at the end, search trie to find all words starting with that prefix
# if not, only the query word will be used
queryWords = []
if query[-1] == '*':
    searchTrie()
else:
    queryWords = [query]

# look up invertedIndex for each element in queryWords
# collect all document ids in which these word exist
result = set()
for word in queryWords:
    for docId in invertedIndex[word]:
        result.add(docId)

# print resulting document ids in ascending order
print(sorted(result)) 

