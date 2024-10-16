# Countdowns: A Python-C Performance Comparison

This project demonstrates the difference in execution speed between a Python function and a C function compiled as a shared library, using Python's `ctypes` to call C functions. The C function executes much faster, showing the performance benefits of low-level languages like C for computation-heavy tasks.

## Files

- `countdowns.py`: Python script that calls a C function and compares the execution time between the C and Python implementations of a countdown function.
- `countdowns.c`: C implementation of the countdown function.

## Requirements

- GCC (to compile the C code)
- Python 3
- `ctypes` library (available in Python standard library)

## Usage

### 1. Compile the C Code

First, compile the `countdowns.c` file into a shared library (`.so` file):

```bash
gcc -shared -o libcountdown.so -fPIC countdowns.c
```

### 2. Run the Python Script

Once the shared library is created, run the `countdowns.py` script:

```bash
python3 countdowns.py
```

### 3. Enter an Input

The Python script will prompt you to enter an arbitrary integer value to test the countdown function. For example:

```
Enter an arbitary integer value to test the program = 10000000
```

The script will then call the C function and Python function, timing their execution and printing the results.

## Example Output

After entering an integer, you should see output similar to the following:

```
This took 0.000005 seconds to compile in C 
This took 0.000004 seconds to compile in C 
Time of execution in C 0.00023603439331054688
Time of execution in python 0.40343809127807617

This simple program helps to understand why compiling on a low level language like C improves the execution speed of python programs
```

## Explanation

- **C Implementation**: The countdown function written in C is compiled and called from Python using `ctypes`. The execution is timed using `clock()` from `<time.h>` in C.
- **Python Implementation**: A similar countdown function is written in Python, and its execution is timed using the `time` module.
- **Performance Comparison**: The script highlights the performance improvement when using C for computation-intensive tasks by comparing the time taken by the Python and C functions to execute the same countdown operation.

## Conclusion

This project shows how you can leverage the power of low-level languages like C to boost the performance of Python applications. Compiling the code in C allows significant speedup, especially in scenarios involving heavy computation.
