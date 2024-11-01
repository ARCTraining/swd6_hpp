# Summary

In this workshop, we covered:

```{admonition} 1. Understand how to profile Python code and identify bottlenecks

- [x] _Measure the time of cells, functions, and programs to find bottlenecks e.g., using [`timeit`](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-timeit) and [`line_profiler`](https://github.com/pyutils/line_profiler)._
- [x] _Visualise the profiled code e.g., using [`SnakeViz`](https://jiffyclub.github.io/snakeviz/) and [`pyinstrument`](https://github.com/joerick/pyinstrument/)._
- [x] _Log profiling information e.g., using [`Eliot`](https://eliot.readthedocs.io/en/stable/index.html)._
- [x] _Consider how fast the code could go e.g., Big O notation._

```


```{admonition} 2. Understand how to choose the most appropriate data structure, algorithm, and libraries for a problem

- [x] _Make use of the built-in functions e.g, use `len` rather than counting the items in an object in a loop._
- [x] _Use appropriate data structures e.g., append to lists rather than concatenating, use dictionaries as fast to search look-ups, cache results in dictionaries or tuples to reduce repeated calculations._
- [x] _Make use of the standard library (optimised in C) e.g., the `math` module._
- [x] _See whether there is an algorithm or library that already optimally solves your problem e.g., faster sorting algorithms_.

```


```{admonition} 3. Improve the execution time of Python code using:  

- [x] Vectorisation
    - [x] _Take advantage of broadcasting for different shaped arrays._
    - [x] _Use vectorised functions where you can e.g., [NumPy ufuncs](https://numpy.org/doc/stable/reference/ufuncs.html)._
- [x] Compilers
    - [x] _Speed up numerical functions with the [Numba](http://numba.pydata.org/) `@njit` (nopython) compiler._

```
