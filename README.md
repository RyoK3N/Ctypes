\documentclass{article}
\usepackage{listings}
\usepackage{hyperref}
\begin{document}

\title{Countdowns: A Python-C Performance Comparison}
\author{}
\date{}
\maketitle

This project demonstrates the difference in execution speed between a Python function and a C function compiled as a shared library, using Python's \texttt{ctypes} to call C functions. The C function executes much faster, showing the performance benefits of low-level languages like C for computation-heavy tasks.

\section*{Files}

\begin{itemize}
\item \texttt{countdowns.py}: Python script that calls a C function and compares the execution time between the C and Python implementations of a countdown function.
\item \texttt{countdowns.c}: C implementation of the countdown function.
\end{itemize}

\section*{Requirements}

\begin{itemize}
\item GCC (to compile the C code)
\item Python 3
\item \texttt{ctypes} library (available in Python standard library)
\end{itemize}

\section*{Usage}

\subsection*{1. Compile the C Code}

First, compile the \texttt{countdowns.c} file into a shared library (\texttt{.so} file):

\begin{lstlisting}[language=bash]
gcc -shared -o libcountdown.so -fPIC countdowns.c
\end{lstlisting}

\subsection*{2. Run the Python Script}

Once the shared library is created, run the \texttt{countdowns.py} script:

\begin{lstlisting}[language=bash]
python3 countdowns.py
\end{lstlisting}

\subsection*{3. Enter an Input}

The Python script will prompt you to enter an arbitrary integer value to test the countdown function. For example:

\begin{lstlisting}[language=bash]
Enter an arbitrary integer value to test the program: 1000000
\end{lstlisting}

The script will then call the C function and Python function, timing their execution and printing the results.

\section*{Example Output}

After entering an integer, you should see output similar to the following:

\begin{verbatim}
This took 0.000012 seconds to compile in C

Time of execution in C: 0.001234567

Time of execution in Python: 0.123456789

This simple program helps to understand why compiling on a low-level language like C improves the execution speed of Python programs.
\end{verbatim}

\section*{Explanation}

\begin{itemize}
\item \textbf{C Implementation}: The countdown function written in C is compiled and called from Python using \texttt{ctypes}. The execution is timed using \texttt{clock()} from \texttt{<time.h>} in C.
\item \textbf{Python Implementation}: A similar countdown function is written in Python, and its execution is timed using the \texttt{time} module.
\item \textbf{Performance Comparison}: The script highlights the performance improvement when using C for computation-intensive tasks by comparing the time taken by the Python and C functions to execute the same countdown operation.
\end{itemize}

\section*{Conclusion}

This project shows how you can leverage the power of low-level languages like C to boost the performance of Python applications. Compiling the code in C allows significant speedup, especially in scenarios involving heavy computation.

\end{document}
