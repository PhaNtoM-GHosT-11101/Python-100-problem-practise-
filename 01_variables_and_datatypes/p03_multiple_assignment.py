"""
Problem 3: Multiple Assignment
--------------------------------
Assign the values 1, 2, 3 to three variables x, y, z in a single line.
Then print their sum.

Output: 6
"""

# Write your solution below:

x,y,z = (input("Enter the 3 numbers separated via space: ").split()
)
print("sum = ",end=" ")
print(int(x)+int(y)+int(z))

