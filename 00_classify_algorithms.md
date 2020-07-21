# Classifying Algorithms

Big O notation is used in Computer Science to describe the performance or complexity of an algorithm. 
Big O specifically describes the worst-case scenario, and can be used to describe the execution 
time required or the space used (e.g. in memory or on disk) by an algorithm.

## O(1)
O(1) describes an algorithm that will always execute in the same 
time (or space) regardless of the size of the input data set.

## O(N)
O(N) describes an algorithm whose performance will grow linearly 
and in direct proportion to the size of the input data set. 

## O(N^2)
O(N^2) represents an algorithm whose performance is directly proportional to the square 
of the size of the input data set. 

This is common with algorithms that involve nested iterations 
over the data set. Deeper nested iterations will result in O(N^3), O(N^4) etc.

## O(2^N)
O(2^N) denotes an algorithm whose growth doubles with each addition to the input data set. 
The growth curve of an O(2N) function is exponential - starting off very shallow, then rising enormously. 
An example of an O(2^N) function is the recursive calculation of Fibonacci numbers.

## O(log N)
Let's use the classic **binary search** as an example.

It works by selecting the middle element of the data set, essentially the median, and compares it 
against a target value (the value being searched for). If the values match it will return success. 
If the target value is higher than the value of the probe element it will take the upper half of 
the data set and perform the same operation against it. Likewise, if the target value is lower than 
the value of the probe element it will perform the operation against the lower half. It will continue 
to halve the data set with each iteration until the value has been found or until it can no longer 
split the data set.

This type of algorithm is described as **O(log N)**. The iterative halving of data sets described in the 
binary search example produces a growth curve that peaks at the beginning and slowly flattens out 
as the size of the data sets increase e.g. an input data set containing 10 items takes one second 
to complete, a data set containing 100 items takes two seconds, and a data set containing 1000 items 
will take three seconds. Doubling the size of the input data set has little effect on its growth as 
after a single iteration of the algorithm the data set will be halved anyway. This makes algorithms 
like binary search extremely efficient when dealing with large data sets.
