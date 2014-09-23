from multi import *


d = []
with open('digit', 'r') as f:
    d = [int(i) for i in f.read()]
print(max([mul(d[i:i + 13]) for i in range(0, len(d) - 13)]))
