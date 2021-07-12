# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
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
            

def list_to_linked_list(l):
    dummyHead = ListNode(0)
    linked_list=dummyHead

    for i in l:
        linked_list.next=ListNode(i)
        linked_list=linked_list.next
    return dummyHead.next


if __name__ == "__main__":
    x=Solution()
    num1= list_to_linked_list([1,2,3,4])
    num2 = list_to_linked_list([9,3,5,3,4,5])

    ans= x.addTwoNumbers(num1,num2)

    while ans:
        print(ans.val)
        ans=ans.next
