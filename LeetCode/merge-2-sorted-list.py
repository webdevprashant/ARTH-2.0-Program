"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]"""

l1 = [1,2,4]
l2 = [1,3,4]

def mergesortedlist(list1, list2):
   m = list1 + list2
   m.sort()
   return m
   

a = mergesortedlist(l1,l2)
print(a)