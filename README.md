# scrabble-cheater
Scrabble cheater in Python<br />
http://wiki.openhatch.org/Scrabble_challenge

## Project
Write a Scrabble cheater from scratch.

## Goals
- practice breaking down a problem and solving it in Python from scratch
- practice command line argument parsing
- practice reading from files
- practice working with dictionaries and for loops

## Problem Statement
Write a Python script that takes a Scrabble rack as a command-line argument and prints all valid Scrabble words that can be constructed from that rack, along with their Scrabble scores, sorted by score. An example invocation and output:

```
[[Media:]]
$ python scrabble.py ZAEFIEE
17 feeze
17 feaze
16 faze
15 fiz
15 fez
12 zee
12 zea
11 za
6 fie
6 fee
6 fae
5 if
5 fe
5 fa
5 ef
2 ee
2 ea
2 ai
2 ae
```

## Resources
- http://courses.cms.caltech.edu/cs11/material/advjava/lab1/sowpods.zip contains all words in the official SOWPODS word list, one word per line.
- Here is a dictionary containing all letters and their Scrabble values:

```
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
```
