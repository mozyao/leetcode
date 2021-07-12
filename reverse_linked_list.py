class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
    
        curr = None
        while head:
            
            temp=head.next

            head.next = curr
            curr=head
            head=temp
        return curr

def list_to_linked_list(l):

    dummyHead = ListNode(0)
    curr = dummyHead
    for i in l:
        curr.next = ListNode(i)
        curr = curr.next



    return dummyHead.next 

if __name__ == "__main__":
    x=Solution()
    a=list_to_linked_list([1,4,5])
    c= x.reverseList(a)
    while c:
        print(c.val)
        c=c.next


