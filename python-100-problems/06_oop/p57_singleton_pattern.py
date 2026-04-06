"""
Problem 57: Singleton Design Pattern
--------------------------------------
Implement a Singleton class (only one instance allowed).
Use it to create a Logger class that appends to a shared log list.

logger1 = Logger()
logger2 = Logger()
print(logger1 is logger2)  → True

logger1.log("Starting app")
logger2.log("Connecting DB")
print(logger1.get_logs())  → both logs visible
"""

# Write your solution below:


