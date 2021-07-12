# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(l):

    dummyHead = ListNode(0)
    curr = dummyHead
    for i in l:
        curr.next = ListNode(i)
        curr = curr.next



    return dummyHead.next # since we don;t need the head 0 , 
                            # all we need is the the liked list start from summyHead.next

def mergeTwoLists( l1: ListNode, l2: ListNode) -> ListNode:
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

 




def main():

    a = list_to_linked_list([1,2,4])
    
    b = list_to_linked_list([1,3,4])

    c=mergeTwoLists(a,b)

    while c:
        print(c.val)
        c=c.next

if __name__ == "__main__":
    main()



