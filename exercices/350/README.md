# bencode / bdecode

Introduces: bytes.

Author(s): Julien Palard

## Instructions

Expose two functions `encode` and `decode`.

 + `encode` take one `dict` as a parameter and return a `byte`.
 + `decode` take a `bytes` as a parameter and return a `dict`.

You have to follow the `bencode` encoding and decoding algorithm, see
[Wikipedia bencode page](http://en.wikipedia.org/wiki/Bencode).

## Hints

You may code other `helper` functions in your module,
functions to help `encode` and `decode` in their work. You also can
store module variables and use them, like in exercice 450, but only
for you to use.
## References
 - [bytes](https://docs.python.org/3.1/reference/lexical_analysis.html#strings)
