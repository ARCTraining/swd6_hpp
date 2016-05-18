## Profiling your code in Python (1)

### Initial thoughts
* Get it right first, then make it fast(er).
 
Profiling your code probably shouldn't be the first thing you should do. Well-written, testing code using an efficient algorithm should be the first (and second) steps). There is no point in optimising code that doesn't do what you want it to!

Lots of design decsions might cause code to run slowly, some possible causes might be:

1. Hitting memory limits 
2. Accidentally looping through arrays you're already looping through - for example calling a procedure inside a loop to find something, and then having that procedure loop through the array to find it.
3. Putting low-probability if-statements early in an if-else ladder
4. Using if-else ladders where a switch/case statement might be better
5. Calling procedures or using complex if-statements inside very large data loops
6. Making variables inside loops instead of outside them, so they keep getting recreated.
7. Reading and writing from the harddrive
8. Using inefficient objects (such as lists) when an array might be better

Two steps before profiling would be to ensure you're getting the right answers, and through the most efficient approach (make coarse adjustments before the fine-tuning). Then go ahead and profile to find bottlenecks. This of course may be an iterative process which informs the best approach/algorithm.

### Learning objectives
* Why do I need to profile my code?
* What impact can I expect on my code?
* How do I use `cProfile`?
* How do I use `line_profiler`?
* How do I interpret the results?
* How can I use these results to make my code run faster?
* 
### Getting ready

In this session, we will use two profiling tools:

* `cProfile`
* `line_profiler`
* 
The `line_profiler` module is not installed as part of the base Anaconda (or any other) Python installation. You will need to use the conda package manager to install this onto your computers.

At the command prompt, enter:

`conda install line_profiler`

If you are using a different Python distribution, the `line_profiler` package can be installed through `pip`:

`pip install line_profiler`

#### Why do I need to profile my code?

No matter how fast your computer is, some programs take too long to run. Eventually you become tired of taking tea breaks to fill the time; or you need to tackle a problem so large, you cannot imagine it finishing at all.

Making a program run more quickly can be daunting: the program might be large; it might have been written by someone else, or in a language you are unfamiliar with.

This is where profiling can help.

It shows what part of a program is occupying most of its execution time, directing you to where you need to focus attention and gain insight on how it might be done better. You can try out different ways of doing the same thing and measure how much faster or slower they are.

Just as importantly, profiling shows you what you do NOT need to execute more quickly. Optimising for speed takes effort to do and easily results in hard to read code that is difficult to understand or change. For that reason, it is important not to optimise code that does not need to be optimised.

#### What impact can I expect on my code?
* Running a profiler will have an effect on the code- it usually slows it down
* Once we have run the profiler, we get some information that might help us understand where it is spending its time

#### How do I use `cProfile`?
`cProfile` is Python's built in profiling tool. It links to CPython's virtual machine to profile every function it sees. It gives a large amount of information but for a corresponding overhead in the program run-time.

Let's take a simple example, a script to calculate the first `n` prime numbers (this is saved as `primes.py` in the `codes` directory). To profile this using `cProfile`:

`python -m cProfile -s cumulative primes.py`

The `-s cumulative` flag tells `cProfile` to sort by the cumulative time spent inside each function. It writes its results directly to screen:

```
Martins-MacBook-Air:codes martin$ python -m cProfile -s cumulative primes.py
         5 function calls in 0.019 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.019    0.019 {built-in method builtins.exec}
        1    0.000    0.000    0.019    0.019 primes.py:1(<module>)
        1    0.016    0.016    0.018    0.018 primes.py:1(primes)
        1    0.002    0.002    0.002    0.002 primes.py:22(<listcomp>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```
In this case, it doesn't give us a great deal of detail. It will though for larger and more structured codes. Writing to screen isn't always useful, more appropriate would be to write the results to a statistics file and then analyse this using Python or another tool:

`python -m cProfile -o profile.stats primes.py`

#### How do I use `line_profiler` ?
After you have installed the `line_profiler` module, to use it you need to add a decorator before each function you want the profiler to measure.

Let's take a simple example (again), the script to calculate the first `n` prime numbers (this is saved as `primes.py` in the `codes` directory):

``` python
def primes(n):
    if n==2:
        return [2]
    elif n<2:
        return []

    s=range(3,n+1,2)
    mroot = n ** 0.5
    half=(n+1)//2-1
    i=0
    m=3

    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]

primes(100)
```

To profile the `primes` function, we need to add the `@profile` decorator before the function:

``` python
@profile
def primes (n):
    ...
```
A decorator is a way of 'wrapping' a function so as to give it some additional capabilities. In this case, we are adding the ability to be profiled to the primes function.

Here, the `@profile` decorator tells the profiler to profile this function. If you have multiple functions in your script then add the `@profile` decorator in front of each of them.

Save the file (as `primes.py`)

So before we run the profiler, let's take a look at the code and see where we think it is going to spend it's time.
* On what lines will this script spend most of its time?
* What about cumulatively?

To profile this `primes.py` script we now need to run the profiler and tell it to profile our decorated code.

`kernprof -l -v primes.py`

Here:
`kernprof` is the profiler script
The `-l` argument tells the profiler to recognise the `@profile` decorator and profile your code.
The `-v` argument tells the profiler to display timing information when the script has finished running.

If we do this, we should get an output on screeen that looks something like this:

```
Wrote profile results to primes.py.lprof
Timer unit: 1e-06 s

Total time: 0.000121 s
File: primes.py
Function: primes at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           @profile
     2                                           def primes(n):
     3         1            2      2.0      1.7      if n==2:
     4                                                   return [2]
     5         1            1      1.0      0.8      elif n<2:
     6                                                   return []
     7                                           
     8         1            9      9.0      7.4      s=list(range(3,n+1,2))
     9         1           11     11.0      9.1      mroot = n ** 0.5
    10         1            1      1.0      0.8      half=(n+1)//2-1
    11         1            1      1.0      0.8      i=0
    12         1            1      1.0      0.8      m=3
    13                                           
    14         5            5      1.0      4.1      while m <= mroot:
    15         4            2      0.5      1.7          if s[i]:
    16         3            3      1.0      2.5              j=(m*m-3)//2
    17         3            2      0.7      1.7              s[j]=0
    18        31           22      0.7     18.2              while j<half:
    19        28           19      0.7     15.7                  s[j]=0
    20        28           21      0.8     17.4                  j+=m
    21         4            4      1.0      3.3          i=i+1
    22         4            3      0.8      2.5          m=2*i+3
    23         1           14     14.0     11.6      return [2]+[x for x in s if x]
 ```


#### Simple improvement example

There are many ways to improve the efficiency of the code. Let's cover one simple step which will improve the performance of the square root function. On line 9 in the code, we see that square root of n is executed by the built-in power function:

``` python
mroot = n ** 0.5
```

From the information provided by the profiler we see that this line of code consumes a not insignificant proportion of CPU time. We can replace this computation with the `sqrt()` function from the `math` library to see what effect it has on performance.

``` python
import math

..

mroot = math.sqrt(n)
```

##### Task 1: 
Replace the square root computation with the `sqrt()` function from the `math` library and compare the results from the previous profiler run.


##### Task 2:
1. Write two programs that each use a different method for calculating pi OR write one program that uses two methods.
2. Profile each method
3. Determine a metric for efficiency
4. Determine which method for pi is the most efficient in your example.

An example python script is given in `profiling_pi.py` in the `codes` directory.

##### Task 3:
Use both `cProfile` and `line_profiler` to profile the example code `julia.py` (it generates a plot of the Julia set). It is a CPU-bound program.

Attempt to determine where the code spends most of its time. Are there any optimisations you can suggest to improve run-time?

##### Task 4: Visualising profiling runs
`snakeviz` is a visulaisation tool for the output files created by `cProfile`. It can be installed by either:

* `conda install snakeviz` (if you are using Anaconda Python)
* `pip install snakeviz`

More details are at the [Snakeviz](https://jiffyclub.github.io/snakeviz/) website.

Create profile files for two or three of your codes using `cProfile` and follow the instructions to visualise using `snakeviz`. Is this more useful than the text/ table based visualisation tools?
