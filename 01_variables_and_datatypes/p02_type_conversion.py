"""
Problem 2: Type Conversion
---------------------------
Take a float number as input, convert it to int, string, and bool.
Print each converted value along with its type.

Input:  3.7
Output:
  int   → 3   <class 'int'>
  str   → 3.7 <class 'str'>
  bool  → True <class 'bool'>
"""

# Write your solution below:
f_n= float(input("Enter a Floating number"))
print(type(f_n))
i = int(f_n)
s = str(f_n)
b = bool(f_n)

print(i,s,b)
