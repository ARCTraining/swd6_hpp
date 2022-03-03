## Profiling your code in Python (2)

In the previous session we discussed tools to profile CPU usage but there are also tools to measure memory usage on a line-by-line basis. This permits you to ask two main questions:

* Could less RAM be used by rewriting a function more efficiently?
* Could **more** RAM be used and CPU cycles saved by caching?

The `memory_profiler` tools works in a similar way to `line_profiler` but slows down execution time **a lot**. Somewhere between 10 and 100 times slower is usual. In practice, installing the `psutil` package normally speeds up `memory_profiler`.

### Installation

For Anaconda Python:

* `conda install memory_profiler`
* `conda install psutil`

Otherwise:

* `pip install memory_profiler`
* `pip install psutil`

### Usage

To use `memory_profiler` to profile the `julia.py` code (as this takes quite a while you might want to use the simplified version `julia_short.py` instead):

Add `@profile` decorators in front of the functions you want to profile. Then:

`python -m memory_profiler julia.py`

This should show an unexpected memory use in the `calculate_z_serial_purepython` function.

It might be useful then to visualise this memory change over time and plot the result. `memory_profiler` has a utility called `mprof` which can be used to sample memory usage and plot the results. Fortunately it is lightweight and barely affects the runtime.

To do this:

`mprof run julia.py`

This creates a statistics file that can be visualised using `mprof plot`.

#### Task:
What changes could be made to this code to reduce memory utilisation?
