# 3 Ways to Distance

Introduces: math, numpy.

## Description

You will calculate the distance between two points. More precisely the [euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance).

One can calculate the distance in two dimensions, ie. with two variables (like x and y) for each points.

![ED 2d](http://blogs.esri.com/esri/arcgis/files/2013/02/EuclideanDistanceGraphic_web.jpg)

Or in 3 dimensions:

![ED 3d](http://support.esri.com/fr/knowledgebase/techarticles/renderImage?ImageId=15802&ImageType=gif)

Or at N dimensions...

Look for more information on wikipedia : <https://en.wikipedia.org/wiki/Euclidean_distance>

## Instructions

You must provide a script called `solution.py` in which there is the following functions:

+ `euclidean(a, b)` where `a` and `b` are iterables containing the coordinates of a point in the euclidean space. The function should return the euclidean distance between points `a` and `b`. You should not use any module for this function.

+ `opt_euclidean(a, b)`. The same as `euclidean` but using the [math](https://docs.python.org/3.4/library/math.html) module.

+ `np_euclidean(a, b)`. The same as `euclidean` but using the [numpy](http://www.numpy.org/) module.

	You should import `numpy` like this:

	```python
	import numpy as np
	```
Such as:

```python
>>> from solution import *
>>> a = [2,3]
>>> b = [5,6]
>>> euclidean(a, b)
4.242640687119285
>>> opt_euclidean(a, b)
4.242640687119285
>>> np_euclidean(a, b)
4.2426406871192848
>>> euclidean(a,b) == opt_euclidean(a,b) == np_euclidean(a,b)
True
>>> a = [2,3,7,3,4,0,8,2,1]
>>> b = [5,3,0,7,8,6,9,4,5]
>>> euclidean(a, b)
12.12435565298214
```
## References
 - [math](https://docs.python.org/3.4/library/math.html)
 - [numpy](http://www.numpy.org/)
