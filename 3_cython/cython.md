## Using Cython to make your code faster

Both Cython and Numba work by creating a *compiled* version of part of your code that is then called by the main program. As compiled code usually executes must more quickly than interpreted code, this is an easy gain to improve the execution time of your code.

### Which should I use?

I just need a quick way to improve speed: Use **numba**

I need to distribute my code to other people: Use **Cython**

I need to write faster code that uses numpy arrays: Use **numba**

I need to use advanced Python features: Use **Cython**

### How do I use Cython?

Basically, Cython is regular Python but (if we do it properly) with C data types defined. We write **type annotated code**.

Let's start with a simple example. In a suitable directory (this `cython` one is good), create a file called `helloworld.pyx`:

	print ("Hello World")
	
Now we need to create a file `setup.py` which instructs Python how to create the C version of the `helloworld.pyx` file:

	from distutils.core import setup
	from Cython.Build import cythonize
	
	setup(
	    ext_modules = cythonize("helloworld.pyx")
	)
	
We now need to use this to build the Cython (compiled Python) version of `helloworld.pyx`:

	python setup.py build_ext --inplace
	
This will create a file called `helloworld.so` (`so` means a shared object file) on a Linux machine or a Mac and a `.pyd` file on a Windows machine.

To use this file, start the Python interpreter and import as a Python module:

	>>> import helloworld
	Hello World 
	
The two step setup process can be complicated. If the module you want to create does not include any complex C, you can use the `pyximport` module to build and load `.pyx` files automatically on import without having to write a `setup.py`.


####Exercise 1:
From the official Python documentation, a simple fibonacci function is defined as:

	def fib(n):
	    """Print the Fibonacci series up to n."""
	    a, b = 0, 1
	    while b < n:
	        print b,
	        a, b = b, a + b
	        
Create a simple program that uses this function to print the Fibonacci numbers up to 2000, eg:

	print (fib.fib(2000))

Time how long it takes to execute.
	        
#### Exercise 2:
Follow the steps from the simple `helloworld` exercise above to:

* create a `fib.pyx` file containing just this function definition
* create a `setup.py` file
* build it
* and now use this new module in a test program
* time how long the new program takes to execute
* is there a difference between this Cython version and the version in exercise 1?

### Defining C data types

In the previous example, `primes.pyx`:

	def primes(int kmax):
	    cdef int n, k, i
	    cdef int p[1000]
	    result = []
	    if kmax > 1000:
	        kmax = 1000
	    k = 0
	    n = 2
	    while k < kmax:
	        i = 0
	        while i < k and n % p[i] != 0:
	            i = i + 1
	        if i == k:
	            p[k] = n
	            k = k + 1
	            result.append(n)
	        n = n + 1
	    return result
	    
We have a normal looking function definition **except** for the lines:

	def primes(int kmax):

`kmax` is declared to be of type `int` . This means that the object passed will be converted to a C integer (or a `TypeError.` will be raised if it can’t be).	

and

	cdef int n, k, i
	cdef int p[1000]
	
The `cdef` statement is used to define some local C variables that are then used later in the function. This is to ensure that the most efficient data types are used throughout.

Suitable C data typ

#### Exercise 3

Use the same process as in exercise 3 to compile,  build and test a module containing the `primes` function from `primes.py`, ie.

* create a `primes.pyx` file containing just this function definition
* create a `setup.py` file
* build it
* use this new module in a test program
* time how long the new program takes to execute

#### Exercise 4

After profiling the `julia.py` code, you should have a good idea of a target function to Cythonise. Using the same process as before, type annotate an appropriate function then compile, build and test the module.

Suitable C data types to consider are:

* `int` for a standard integer
* `unsigned int` for an integer than can only be positive
* `double complex` for double-precision complex numbers

Time how long the program takes to run and compare it with the regular version.


