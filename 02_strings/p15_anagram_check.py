"""
Problem 15: Anagram Check
---------------------------
Check if two strings are anagrams of each other.
(Same characters, different order. Ignore spaces and case.)

Input:  "listen", "silent"
Output: True
"""

# Write your solution below:

def Anagram(a,b):
    lista=[]
    listb=[]
    for i in a:
        lista.append(ord(i))
    for i in b:
        listb.append(ord(i))
    lista.sort()
    listb.sort()

    return (lista==listb)

Anagram("listen", "silent")