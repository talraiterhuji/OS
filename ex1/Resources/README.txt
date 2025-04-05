talraiter, liorshapira
Tal Raiter (208997908), Lior Shapira (315465765)
EX: 1

FILES:
memory_latency.cpp – Main program logic and measurements.
memory_latency.h – Type definitions and function declarations.
measure.cpp – Random access latency measurement implementation.
measure.h – Declaration for measure_latency.
plot_example.py – Script for plotting the results.
memory_latency_results.csv – Output data from the program.
results.png – Generated plot image.
lscpu.png – Screenshot of the CPU info (required for submission).

REMARKS:

ANSWERS:

Assignment 1

When the program is executed with exactly one argument,
it begins by creating a directory named Welcome.
It then creates and opens three files within that directory:
Welcome, To, and OS-2024, each with write permissions and truncation if the file
already exists. The program writes the following messages to the files:
Welcome/Welcome:
"liorshapira\nIf you haven't read the instructions yet, read them now!"
Welcome/To:
"Start exercises early!"
Welcome/OS-2024:
"Good luck!"
After writing the messages, it closes all the files,
deletes them using unlink(), and removes the Welcome directory using rmdir().
Finally, the program terminates successfully with exit code 0.

When the program is executed with a number of arguments not equal to one,
it begins by duplicating the file associated with file descriptor 2 (standard error)
using the dup(2) system call. It then checks the access modes and flags of the
 new descriptor using fcntl, which confirms that it is opened in read-write mode.
 Following this setup, the program writes an error message to the duplicated descriptor:
"Error. The program should receive a single argument. Exiting."
Interestingly, this message is immediately followed by a "Success"
message. Finally, the program terminates by calling exit_group(0),
exiting with status code 0.

Assignment 2
Results Discussion

# What patterns do we observe?
We can see that random access latency increases as the array size grows,
especially when it crosses cache boundaries (L1, L2, L3). In contrast,
sequential access latency stays almost constant and very low,
regardless of array size.

# Do the results meet expectations?
Yes – the trends match what we expected:
Random access starts fast, then slows down at the L1, L2, and L3 cache sizes.
Sequential access remains fast because of how modern CPUs handle memory access
(cache lines and prefetching).

# Why is sequential access faster than random access?
Sequential access benefits from:
Cache lines: Each memory load brings a whole block (usually 64 bytes),
so many values are read at once.
Prefetching: The CPU can guess that we're accessing memory in order and loads
the next blocks in advance.
Random access doesn’t help the CPU predict anything – each access may go to
a completely different memory area, so there are more cache misses and longer delays.

# How do cache levels affect latency?
When the array fits in L1 cache, access is very fast (≈1 ns).
Once it no longer fits, the CPU has to go to L2 (slower),
then L3, and finally RAM (much slower). Each step adds more latency.
This is why we see “jumps” in the random access curve near the cache sizes.




