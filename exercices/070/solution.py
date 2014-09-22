from itertools import permutations
import string
allTheLetters = string.ascii_lowercase

for u,v in permutations(allTheLetters,2):
	print(u+v)
