#!/usr/bin/python
import string


allTheLetters = string.ascii_lowercase
for i in allTheLetters[::-1]:
	if i in 'aeiou':
		print(i.upper(),end="")
	else:
		print(i,end="")

print()
