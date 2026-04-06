"""
Problem 13: Count Vowels
--------------------------
Count the number of vowels (a, e, i, o, u) in a given string.
Case-insensitive.

Input:  "Computational Mathematics"
Output: 9
"""

# Write your solution below:
def countVowels(inp):
    inp = inp.lower()
    count = 0 
    for i in inp:
        if i in ('a', 'e', 'i', 'o', 'u'):
            count+=1
    return count
inp = "Computational Mathematics"
print(countVowels(inp))