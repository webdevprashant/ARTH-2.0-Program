"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

rn=0
def checkpalindromeornot(value):
    while value != 0:
        global rn
        digit = value % 10
        rn = rn*10 + digit
        value //= 10
    if rn == no:
       print("True")
       print(rn, no)
    else:
       print("False")
       print(rn, no)

no = int(input("Enter number to check palindrome or not : "))
checkpalindromeornot(no)