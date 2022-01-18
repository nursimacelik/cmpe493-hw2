import string
import pickle
import json
from Trie import Node, TrieObject

# Document class is used for representing single news
class Document:
    def __init__(self, text):
        self.text = text					# stores all that is inside REUTERS tag corresponding to this document
        self.extract_fields()					# extracts TITLE and BODY from the text
        self.title = self.case_folding(self.title)
        self.body = self.case_folding(self.body)
        self.title = self.remove_punctuation(self.title)
        self.body = self.remove_punctuation(self.body)
        self.title = self.remove_stopwords(self.title)
        self.body = self.remove_stopwords(self.body)

    # extract documentId, title, and body fields from the text
    def extract_fields(self):
        idStart = self.text.find("NEWID")
        idEnd = self.text.find("\"", idStart+7)
        self.documentId = int(self.text[idStart + 7 : idEnd])

        titleStart = self.text.find("<TITLE>")
        titleEnd = self.text.find("</TITLE>")
        self.title = self.text[titleStart + 7 : titleEnd]

        bodyStart = self.text.find("<BODY>")
        bodyEnd = self.text.find("</BODY>")
        self.body = self.text[bodyStart + 6 : bodyEnd]

    # converts given text to lowercase
    def case_folding(self, text):
        return text.lower()

    # removes punctuation from given text using string.punctuation list 
    def remove_punctuation(self, text):
        result = ""
        for i in text:
            if i not in string.punctuation:
                result += i
        return result

    # removes stopwords from given text using stopWords array
    def remove_stopwords(self, text):
        result = ""
        for word in text.split():
            if word not in stopWords:
                result += word
                result += " "
        return result


# read stopWords
stopWords = open("stopwords.txt").read().split()

# initialize invertedIndex as dictionary
# each element is in the form of
# 'word': [documentId1, documentId2, ...]
invertedIndex = {}

for i in range(0,22):
    # construct file name
    filename = ""
    if i<10:
        filename = "./reuters21578/reuters21578/reut2-00" + str(i) + ".sgm"
    else:
        filename = "./reuters21578/reuters21578/reut2-0" + str(i) + ".sgm"

    # read file with latin-1 encoding
    with open(filename, encoding='ISO-8859-1') as file:
        f = file.read()

        # split according to REUTERS tag
        newsText = f.split("<REUTERS")
        for j in range(1,len(newsText)):

            # create Document out of text between two <REUTERS
            # preprocessing is done inside the __init__
            d = Document(newsText[j])

            # for every word in title, put the word in invertedIndex if it is not there
            # then append current document's id to the list corresponding to the word
            for k in d.title.split():
                if k not in invertedIndex:
                    invertedIndex[k] = []
                
                invertedIndex[k].append(d.documentId)

            # same procedure for body
            for k in d.body.split():
                if k not in invertedIndex:
                    invertedIndex[k] = []
                
                invertedIndex[k].append(d.documentId)


# get rid of repeating document ids
for word, lst in invertedIndex.items():
    invertedIndex[word] = list(set(lst))

# create a trie using TrieObject from Trie.py
trie = TrieObject()

# add all indexed words to trie
for word in invertedIndex.keys():
    trie.add(word)

# dump trie and invertedIndex

with open("trie.pickle", "wb") as outfile:
    pickle.dump(trie, outfile)

with open('inverted_index.json', 'w') as outfile:
    json.dump(invertedIndex, outfile)
