import argparse
import sys

# Step 1: construct a word list
with open('sowpods.txt') as f:
    read_data = f.readlines()
i = 0
for word in read_data:
    read_data[i] = word.lower().strip()
    i += 1

# Step 2: get the rack
parser = argparse.ArgumentParser()
parser.add_argument('rack', nargs='?')
args = parser.parse_args()
if len(sys.argv) == 1:
    print("Please supply some letters. Ex: 'python scrabble.py RSTLNEI'")
    exit()
rack = args.rack.lower()

# Step 3: find valid words
valid_words = []
for word in read_data:
    rack_dup = rack
    valid = True
    for char in word:
        if char in rack_dup:
            rack_dup = rack_dup.replace(char, "", 1)
        else:
            valid = False
    if valid:
        valid_words.append(word)

# Step 4: scoring
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}
valid_word_scores = {}
for word in valid_words:
    score = 0
    for char in word:
        score += scores[char]
    valid_word_scores[word] = score
sorted_scores = sorted(valid_word_scores.items(), key = lambda x: x[1], reverse = True)
for score in sorted_scores:
    print("%s,%s" % (str(score[1]), str(score[0])))