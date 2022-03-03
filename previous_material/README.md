## High Performance Python

* What are the motivations for profiling and optimising code?
* The perceived problems with Python; interpreted vs. compiled languages
* The Python language vs. the Python environment: Python, CPython and PyPy

### First session 
* Profiling code- how to identify the 'problem areas' or potential slow-running areas in code
* Speeding up code 1: Ahead-Of-Time (AOT) compilation with Cython
* Speeding up code 2: Just-In-Time (JIT) compilation with numba
* Speeding up code 3: parallel programming with `multiprocessing` and moving code to clusters
* Speeding up code 4: An alternative Python- pypy


### Second session 
* Speeding up code 5: The benefits of numpy
* Performance differences between Python lists, arrays and Numpy arrays
* Introduction to Computer architecture: why caches, threads and processes are important
* The Python GIL (Global Interpreter Lock) and why this is important
* Design choices- choosing the right algorithm for the job (big O notation)
* Final thoughts and other ideas:
    * Why not just write it in C?
    * Use a specialist language to write native functions, eg. Chapel for parallel programming or Julia for general purpose performant code.

