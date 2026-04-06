"""
Problem 5: Check Variable Type
--------------------------------
Create one variable of each type: int, float, str, bool, list, dict.
Use isinstance() to verify each one and print True/False for each.

Expected Output (6 lines of True):
  True
  True
  ...
"""

# Write your solution below:

a,b,c,d,e,f = 1,1.0,"1",True,[1],{"a":1}

print(isinstance(a,int))
print(isinstance(b,float))
print(isinstance(c,str))
print(isinstance(d,bool))
print(isinstance(e,list))
print(isinstance(f,dict))