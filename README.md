# Introduction to Information Retrieval - Homework 2

Program to get a word from the user and list all the document ids that contains the query word within the Reuters dataset. Put a star at the end to do prefix search.

Trie and inverted index is used.

Example:
```
> python3 prep.py

> python3 query.py
Enter your query: book
13482
43473
...

> python3 query.py
Enter your query: book*
13482
15388
43473
...
```
