class Node:
    def __init__(self):
        self.value = ''			# the character associated with node, default value ('') is meaningless and will not be used
        self.isEnd = False		# whether this node is an end of a word in dictionary
        self.children = {}		# dictionary to hold child nodes in the form of {'a':Node1, 'f':Node2, ...}

class TrieObject:
    def __init__(self):
        self.root = Node()		# root is created at initialization

    # words can be added through this method
    # start from root
    # for each character in the word, examine the current node's children and if a node exist for this character proceed to that node
    # otherwise, create node
    # set isEnd as True at the end of the word
    def add(self, word):
        node = self.root

        for i in range(0, len(word)):
            c = word[i]
            if not c in node.children:
                newNode = Node()
                newNode.value = c
                node.children[c] = newNode
            
            if i==len(word)-1:
                node.children[c].isEnd = True
            
            node = node.children[c]
