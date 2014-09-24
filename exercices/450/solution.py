from string import ascii_lowercase, ascii_uppercase
import operator

backward = operator.sub
forward = operator.add


def caesar_cypher(s, k, mod):
    res = list(s)
    for place, i in enumerate(res):
        base = ord('a') if i in ascii_lowercase else ord('A')
        if i in ascii_uppercase or i in ascii_lowercase:
            ascii = mod(ord(i) - base, k) % 26
            res[place] = chr(ascii + base)
    return "".join(res)
