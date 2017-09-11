import argparse
import sys

# Step 1: construct a word list
with open('sowpods.txt') as f:
    read_data = f.readlines()
i = 0
for word in read_data:
    read_data[i] = word.strip()
    i += 1

# Step 2: get the rack
parser = argparse.ArgumentParser()
parser.add_argument('rack', nargs='?')
args = parser.parse_args()
if len(sys.argv) == 1:
    print("Please supply some letters. Ex: 'python scrabble.py RSTLNEI'")
    exit()
rack = args.rack.lower()
print(rack)