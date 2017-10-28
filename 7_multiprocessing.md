### Using Multiprocessing ###

CPython (the regular Python written in C) doesn’t use multiple CPUs by default. This is partly due to Python’s being 
designed back in a single-core era, and partly because parallelising can actually be quite difficult to do efficiently. 

When used to parallelise a problem over a set of CPU cores you can expect up to an n-times (nx) speedup with n cores. 
If you have a quad-core machine and you can use all four cores for your task, it might run in a quarter of the original runtime.

Amdahl’s law affects this. The law tells us that if only a small part of your code can be 
parallelised, it doesn’t matter how many CPUs you throw at it; overall, it still won’t run much faster.

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

#### Estimating Pi Using the Monte Carlo Method
We can estimate pi by throwing thousands of imaginary darts into a “dartboard” rep‐ resented by a unit circle. 
The relationship between the number of darts falling inside the circle’s edge and outside it will allow us to approximate pi.
This is an ideal first problem as we can split the total workload evenly across a number of processes, each one running 
on a separate CPU. Each process will end at the same time as the workload for each is equal, so we can investigate the 
speedups available as we add new CPUs and *hyperthreads* to the problem.



