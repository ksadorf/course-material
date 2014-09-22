from itertools import product
import string
allTheLetters = string.ascii_lowercase

for u, v in product(allTheLetters, allTheLetters):
    print(u+v)
