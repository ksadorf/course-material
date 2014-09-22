from itertools import combinations
import string
allTheLetters = string.ascii_lowercase

for u,v in combinations(allTheLetters,2):
	print(u,v)
