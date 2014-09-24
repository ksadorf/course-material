# Optimization 101

Introduces: math, numpy, timeit, functions, lambda.

## Description

See exercise 260 for more info on [euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) and necessary functions to complete the exercise.

In this exercise you will benchmark (ie. compare) the performance of the different versions of the functions for calculating euclidean distance that we have implemented in the exercise 260.

## Instructions

You must provide a script called `solution.py` in which the function `benchmark(funcs, a, b)` returns a dictionnary where keys are the function names and their values the time it took to execute the given function ten times measured in seconds as a float number.

`funcs` is a list of the function to be tested, which are the one of the exercise 260 (`euclidean(a, b)` ; `opt_euclidean(a, b)` ; `np_euclidean(a, b)`)

`a` and `b` are the coordinates of the two points between which the distance must be measured. We assume that `a` and `b` are of the type `numpy.ndarray`.

Less formally the function `benchmark` you must provide will test every function passed in `funcs`, execute them ten times each with the parameters `a` and `b`, and return their respective score in a dictionnary. Such as:

```python
>>> from solution import *
>>> a = np.random.randint(100, size=100)
>>> b = np.random.randint(100, size=100)
>>> funcs = [euclidean, opt_euclidean, np_euclidean]
>>> benchs = benchmark(funcs, a, b)
>>> print(benchs)
{'opt_euclidean': 0.009175331972073764, 'euclidean': 0.02502306899987161, 'np_euclidean': 0.002547977026551962}
```

## Advice

+ You should initialize the variables `a` and `b` like this to test your function `benchmark`, using [numpy.random](http://docs.scipy.org/doc/numpy/reference/routines.random.html):

	```python
	>>> a = np.random.randint(100, size=100)
	>>> b = np.random.randint(100, size=100)
	```

	This generates a numpy list (called *array*) of 100 numbers between 0 and 100.

+ To measure time of execution, have a look at the module [timeit](https://docs.python.org/2/library/timeit.html)

## References
 - [math](https://docs.python.org/3.4/library/math.html)
 - [numpy](http://www.numpy.org/)
 - [timeit](https://docs.python.org/3.4/library/timeit.html)
 - [functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
 - [lambda](https://docs.python.org/2/tutorial/controlflow.html#lambda-expressions)
