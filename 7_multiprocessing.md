### Using Multiprocessing ###

CPython (the regular Python written in C) doesn’t use multiple CPUs by default. This is partly due to Python’s being 
designed back in a single-core era, and partly because parallelising can actually be quite difficult to do efficiently. 

When used to parallelise a problem over a set of CPU cores you can expect up to an n-times (nx) speedup with n cores. 
If you have a quad-core machine and you can use all four cores for your task, it might run in a quarter of the original runtime.

Amdahl’s law affects this. The law tells us that if only a small part of your code can be 
parallelised, it doesn’t matter how many CPUs you throw at it; overall, it still won’t run much faster.

#### Parallel Programming Approaches
* Embarassingly Parallel
* Multicore
* Multinode (MPI, which we won't discuss here...)

#### Embarassingly Parallel
Embarassing because embarrassingly easy to make this run in parallel.

**Embarassingly parallel** is where each unit of computation is completely independent of the others. For instance, if you're batch processing a set of images and you only care about one image at a time.

This is the easiest case to deal with. Perhaps you have a bunch of files to process? Or you need to run a model across a range of a range of parameters, and each run is independent? We can run one job per computer, or perhaps a couple per computer (but isolated from one other) to get the speed we need.

*Embarassingly Parallel in Python* 

Simplest: Just run multiple Python instances at the same time (e.g. one per dataset).

```
python my_code.py data_1.dat &
python my_code.py data_2.dat &
python my_code.py data_3.dat &
python my_code.py data_4.dat &
```

This is the easiest approach -- just run multiple copies of your program at once with different inputs. The operating system will distribute these over the multiple cores of your computer, but keep in mind that if you create more instances than cores in your computer (typically 2-4) you mightn't see an additional speedup. Memory also has to be shared between the different processes.

Embarassingly parallel includes not just running multiple jobs on the same computer, but also across multiple computers. We'll talk about how to do this on a supercomputer later.

(The '&' in the above example is unix for 'run in background'... we could achieve the same thing by running in multiple terminal tabs, for instance.)

Little More Advanced: Use the Python multiprocessing library.

Multiprocessing creates seperate processes, each with it's own copy of the Python interpreter, so there is also a communications
overhead with these processes communicating with each other.

The main components of `multiprocessing` are:

**Process**
A forked copy of the current process; this creates a new process identifier and the task runs as an independent child process in the operating system. You can start and query the state of the Process and provide it with a target method to run.

**Pool**
Wraps the Process or threading.Thread API into a convenient pool of workers that share a chunk of work and return an aggregated result.

**Queue**
A FIFO queue allowing multiple producers and consumers.

**Pipe**
A uni- or bidirectional communication channel between two processes.

**Manager**
A high-level managed interface to share Python objects between processes.

**ctypes**
Allows sharing of primitive datatypes (e.g., integers, floats, and bytes) between processes after they have forked.

```
from multiprocessing import Pool

def process_file(filename):
    data = open(filename).read()
    output = my_analysis(data)
    open('output.dat', 'w').write(output)

pool = Pool(processes=8)
input_files = ['data_1.dat', '...', 'data_8.dat']
pool.map(process_file, input_files)
```

This code will spin up 8 processes, run my_analysis on each and save the results.

**Multicore**
Multicore is the next step up. This is where your program shares the load across the different cores (or CPUs) within your computer. Typically a program will only run on one core at a time, but by splitting it up into different processes or threads we can share the load. Your desktop computer probably has at least four cores, and a heavy-duty server might have 12 or more (even up to 64 or more in some specialised circumstances).
Communication is all within the same computer and so communication is fast, and data can be readily shared between processes through memory.

Let's use multiprocessing again

```
from multiprocessing import Pool

def process_file(filename):
    data = open(filename).read()
    return my_analysis(data) # Return single datapoint

pool = Pool(processes=8)
input_files = ['data_1.dat', '...', 'data_8.dat']

# This line runs in parallel, returning an array from each process**
intermediate_results = pool.map(process_file, input_files) 

# This line integrates results, which is a serial process
# (unlike embarassingly parallel)
final_result = my_summary_analysis(intermediate_results)
```

#### Estimating Pi Using the Monte Carlo Method
We can estimate pi by throwing thousands of imaginary darts into a “dartboard” represented by a unit circle. 
The relationship between the number of darts falling inside the circle’s edge and outside it will allow us to approximate pi.
This is an ideal first problem as we can split the total workload evenly across a number of processes, each one running 
on a separate CPU. Each process will end at the same time as the workload for each is equal, so we can investigate the 
speedups available as we add new CPUs and *hyperthreads* to the problem.



