with open('words', 'r') as f:
    s = 0
    for line in f:
        s += line.count('e')
print(s)
