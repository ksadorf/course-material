from collections import Counter


with open('words', 'r') as f:
    line = f.read()
    length = len(line)
    c = Counter(line)

for k in c:
    if k != '\n':
        print("{}: {:.2f}".format(k, c[k] / length))
