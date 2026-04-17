"""
Problem 14: Title Case Without Built-in
-----------------------------------------
Convert a string to title case WITHOUT using .title() method.
Capitalize the first letter of each word manually.

Input:  "nit agartala is great"
Output: "Nit Agartala Is Great"
"""

# Write your solution below:
def title(inp):
    a = inp.split(" ")
    print(a)
    b=''
    for i in a:
        i=i[0].capitalize()
        print(i)

        
    for i in a:
        b=b+i
    print(b)
    

title("nit agartala is great")

