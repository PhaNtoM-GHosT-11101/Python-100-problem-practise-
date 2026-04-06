"""
Problem 12: Palindrome Check
------------------------------
Check if a given string is a palindrome (reads same forwards and backwards).
Ignore spaces and case.

Input:  "A man a plan a canal Panama"
Output: True
"""

# Write your solution below:
def isPalindrome(string):
    return string.lower().replace(" ","")==string.lower().replace(" ","")[::-1]

    



string = 'A man a plan a canal Panama'

print(isPalindrome(string))


