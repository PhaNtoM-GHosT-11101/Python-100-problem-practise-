"""
Problem 6: Memory Identity
---------------------------
Create two variables a = 256 and b = 256.
Then create c = 1000 and d = 1000.
Use 'is' operator and id() to compare a,b and c,d.

Observe: Why does 'is' behave differently for large integers?
(This is about Python's integer caching.)
"""

# Write your solution below:
a=256
b=256
c=1000
d=1000
print(a is b)
print(id(a))
print(id(b))
print(id(a) is id(b))

print(c is d)
print(id(c))
print(id(d))
print(id(c) is id(d))