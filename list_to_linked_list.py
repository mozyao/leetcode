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
                            # all we need is the the liked list start from dummyHead.next


    







def addTwoNumbers(l1, l2):
    dummyHead = ListNode(0) # only use as starting point to chain the whole linked list
    carry = 0
    curr = dummyHead
    
    while l1 or l2:
        if l1:
            l1_val= l1.val
        else:
            l1_val =0
            
        if l2:
            l2_val = l2.val
            
        else:
            l2_val = 0
            
        sum_ = l1_val + l2_val + carry
        
        
        curr.next = ListNode(sum_%10)
        curr = curr.next
        
        carry = sum_ //10
        
        if l1:
            
            l1=l1.next
        if l2:
            l2=l2.next
            
    if carry:
        curr.next = ListNode(carry)
        
        
    return dummyHead.next












def main():
    # l1=ListNode(2)
    # second_l1 = ListNode(4)
    # third_l1 = ListNode(3)

    # l1.next = second_l1
    # second_l1.next = third_l1 

    # l2=ListNode(5)
 

    # second_l2 = ListNode(6)
    # third_l2 = ListNode(4)

    # l2.next = second_l2
    # second_l2.next = third_l2 




    # ans = addTwoNumbers(l1,l2)


    z=list_to_linked_list([1,2,3])
    while z:
        print(z.val)
        z = z.next



    







if __name__ == "__main__":
    main()



