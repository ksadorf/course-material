# calculator1

Introduces: argv, import, len, list, for, enumerate.

Author(s): Antoine Angot

## Instructions

Write a program named `solution.py` that do basic calculations.
You need to be able to get basic operators such as +, - , *, / and %.
Input will integer numbers.

Your program will give a usage message if you don't give the three parameters.

For every other errors like if an operand is not an integer, you'll
print an `input error`.

## Example

```bash
oa@localhost$ ./solution.py 1 + 1
2
oa@localhost$ ./solution.py
usage: python3 ./solution.py a_number (an_operator +-*/%^) a_number
oa@localhost$ ./solution.py 1 / 0
input error
oa@localhost$
```

## Advice

(**SHELL (OSX, Linux...)**) To input a asterix to a python script you must type '\*', such as:

```bash
mbp|110-$ python solution.py 3 / 5
0.6
mbp|110-$ python solution.py 3 + 5
8
mbp|110-$ python solution.py 3 - 5
-2
mbp|110-$ python solution.py 3 * 5
usage: python3 ./solution.py a_number (an_operator +-*/%^) a_number
mbp|110-$ python solution.py 3 \* 5
15
```

(**WINDOWS**) The same apply for Git Bash (the terminal) on windows for `*`. Moreover, `/` must be passed as `//`.
Such as:

![110 erratum](https://hackinscience.github.io/img/110_erratum.png)

## References
 - [argv](https://docs.python.org/3.4/library/sys.html)
 - [import](https://docs.python.org/3/reference/simple_stmts.html#import)
 - [len](https://docs.python.org/3/library/functions.html#len)
 - [list](https://docs.python.org/3/tutorial/introduction.html#lists)
 - [for](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
 - [enumerate](https://docs.python.org/3.4/library/functions.html#enumerate)
