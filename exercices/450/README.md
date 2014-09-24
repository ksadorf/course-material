# Caesar Cypher

Introduces: list, functions, operators.

Author(s): @mazieres

## Description

[Caesar cypher](https://en.wikipedia.org/wiki/Caesar_cipher) is a
method to hide information from being read by some other people,
that's called cryptography. [Caesar
cypher](https://en.wikipedia.org/wiki/Caesar_cipher) is antique
cryptographic method.

Think of one only letter such as `a` you would like to transmit to
someone, but you don't want other people to be able read it.

Now, think of the alphabet as an ordered list of letters:

```python
>>> from string import ascii_lowercase
>>> list(ascii_lowercase)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
```

Each letter has an index in this list. `a` is 1, `b` is 2, `j` is 10, etc...

The [Caesar cypher](https://en.wikipedia.org/wiki/Caesar_cipher) hide
information by using a *key* which is a positive number added to the
index of the original letter, the result being the index of the
encrypted letter.

`a` with `key == 2` gives `c`

If the key brings you to the end of the alphabet, you continue to
count from the begining, such as:

`a` with `key == 28` gives `c`

To decypher, or decrypt, the message, you apply the same procedure
moving backward on the alphabet.

## Instructions

You must provide the function `caesar_cypher(s, key, method)` where:

+ `s` is a string (letter, word, sentence, etc).
+ `key` is a positive integer, the key of the [caesar cypher](https://en.wikipedia.org/wiki/Caesar_cipher).
+ `method` which is either `forward` or `backward`, wether to cypher or decypher a message.

`caesar_cypher` should only transform uppercase and lowercase ascii
letters. Special characters, numbers and letters with accents should
not be transformed.

Your function shall not print but return the encoded/decoded string.

```python
>>> from solution import caesar_cypher, forward, backward
>>> caesar_cypher("a", 2, forward)
'c'
>>> caesar_cypher("c", 2, backward)
'a'
>>> caesar_cypher("Python is super disco !", 31, forward)
'Udymts nx xzujw inxht !'
>>> caesar_cypher("Udymts nx xzujw inxht !", 31, backward)
'Python is super disco !'
```

## Hints

forward and backward are actually global variable in your solution,
imported using the "from solution import ...".

## References
 - [list](https://docs.python.org/3/tutorial/introduction.html#lists)
 - [functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
 - [operators](https://docs.python.org/3.1/library/stdtypes.html#numeric-types-int-float-complex)
