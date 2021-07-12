# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from max_area_island import Solution
from typing import List
from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# the real input will come with the pos value with indicates the
# revisited node in order to examine our solutions

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()

        
        while head:
            if head in visited:
                return True
            else:
                visited.add(head)
                head = head.next
        return False 



        


def list_to_linked_list(l):

    dummyHead = ListNode(0)
    curr = dummyHead
    for i in l:
        curr.next = ListNode(i)
        curr = curr.next



    return dummyHead.next # since we don;t need the head 0 , 
                            # all we need is the the liked list start from summyHead.next

