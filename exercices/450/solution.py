from string import ascii_lowercase, ascii_uppercase


backward = 'backward'
forward = 'forward'


def caesar_cypher(s, k, mod):
    base = ord('a')
    for i in s:
        if i in ascii_uppercase:
            base = ord('A')
        if i in ascii_uppercase or i in ascii_lowercase:
            if mod == "forward":
                dec = (ord(i) + k - base) % 26 + base
                print(chr(dec), end="")
            elif mod == "backward":
                dec = (ord(i) - k + 26 - base) % 26 + base
                print(chr(dec), end="")
        else:
            print(i, end="")
    print()
