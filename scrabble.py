with open('sowpods.txt') as f:
    read_data = f.readlines()
i = 0
for word in read_data:
    read_data[i] = word.strip()
    i += 1
print(read_data)