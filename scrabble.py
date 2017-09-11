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
valid_words = list()
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