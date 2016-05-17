##Using numba to make your code faster

Whereas Cython can be used to create and build a compiled C version of a module (or any chunk of Python code) as a separate build event, **numba** uses a process called **Just In Time** compilation (or **jit**) to compile the required part of a Python program as and when it is needed.

This is a very quick and easy process and just requires that **numba** is installed on the target computer. It is built on top of the LLVM compiler stack.

Consider this [pairwise distance](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.pairwise_distances.html) function:

**pairwise_pure.py:**
	
	import numpy as np
	
	def pairwise_python(X, D):
	    M = X.shape[0]
	    N = X.shape[1]
	    for i in range(M):
	        for j in range(M):
	            d = 0.0
	            for k in range(N):
	                tmp = X[i, k] - X[j, k]
	                d += tmp * tmp
	            D[i, j] = np.sqrt(d)
	            
	X = np.random.random((1000, 3))
	D = np.empty((1000,1000))

	pairwise_python(X, D)
	            
This is used in an example program in this directory `pairwise_pure.py`. 

####Exercise 1
Time how long this takes to execute and record the result.

###Using numba

Once numba is installed, it takes just three additional lines to interface the code with the LLVM compiler:

**pairwise_num.py**

	import numpy as np
	from numba import double
	from numba.decorators import jit
	
	@jit
	def pairwise_python(X, D):
	    M = X.shape[0]
	    N = X.shape[1]
	    for i in range(M):
	        for j in range(M):
	            d = 0.0
	            for k in range(N):
	                tmp = X[i, k] - X[j, k]
	                d += tmp * tmp
	            D[i, j] = np.sqrt(d)
	
	X = np.random.random((1000, 3))
	D = np.empty((1000,1000))
	
	pairwise_python(X, D)
	
#### Exercise 2
Time how long this `numba` version takes to execute and record the result. Does it differ from the pure python version in exercise 1?

### Comparing numba and Cython

#### Exercise 3
Use the principles from the earlier Cython exercises to create, build and compile a Cython version of this function.

Again, write a simple test program to use it and time how long it takes to generate the result.

How do the three versions compare?

#### Exercise 4
In the previous session, you built a Cythonised version of the `julia.py` code. This time create an optimised version using `numba` and compare the runtime of the two versions.