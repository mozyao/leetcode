from max_area_island import Solution
from typing import List
from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        #recurision not working, need fix
        
        if len(lists)==1:
            print("empty list")
            return lists[0]
        else:
            l=len(lists)
            print(l,"the l is ")
            lists[0] =self.mergeTwoLists(lists[0],lists[1])
            if l==2:
                lists=[lists[0]]
            else:

                lists=[lists[0]]+lists[2:]


            self.mergeKLists(lists)
            
        
        
        
    def mergeTwoLists(self,l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy_head = ListNode()
        curr = dummy_head
        while l1 and l2:

            if l1.val <= l2.val:
                v=l1.val
                l1=l1.next
            else:
                v=l2.val
                l2=l2.next
            curr.next = ListNode(v)
            curr=curr.next

        if l1:

            curr.next=l1
        else:
            curr.next=l2
        return dummy_head.next

def list_to_linked_list(l):

    dummyHead = ListNode(0)
    curr = dummyHead
    for i in l:
        curr.next = ListNode(i)
        curr = curr.next



    return dummyHead.next # since we don;t need the head 0 , 
                            # all we need is the the liked list start from summyHead.next

if __name__=="__main__":
    x=Solution()

    lists=[]
    a=list_to_linked_list([1,4,5])
    b=list_to_linked_list([1,3,4])
    c=list_to_linked_list([2,6])
    lists.append(a)
    lists.append(b)
    lists.append(c)
    print(len(lists))
    t=x.mergeKLists(lists)
    while t:
        print(t.val)
        t=t.next


    


