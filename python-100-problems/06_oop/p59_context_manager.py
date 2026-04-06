"""
Problem 59: Context Manager (__enter__ / __exit__)
---------------------------------------------------
Create a Timer context manager that:
  - Records start time on __enter__
  - Prints elapsed time on __exit__
  - Also works as a decorator using contextlib

with Timer("Matrix multiply"):
    result = sum(i*i for i in range(1_000_000))
"""

# Write your solution below:


