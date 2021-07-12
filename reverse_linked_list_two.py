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

    def reverseBetween(self, head: ListNode,left:int,right:int) -> ListNode:
        
        dummy_head_l = ListNode(0)
        l = dummy_head_l
        count_l=1
        while count_l<left:
            l.next=head
            l=l.next
            head=head.next
      


            count_l+=1

        dummy_head_mid  = ListNode(0)
        mid=dummy_head_mid

        count_mid = 1
        while count_mid<right-left+2:
            mid.next=head
            mid=mid.next
            head=head.next
            count_mid+=1


        mid.next=None
        reversed_mid =self.reverseList(dummy_head_mid.next)


        l.next = reversed_mid

        l_plus_reversed_mid =dummy_head_l.next
        dummy_chain = ListNode(0)
        chain=dummy_chain
        while l_plus_reversed_mid:
            chain.next=l_plus_reversed_mid
            chain=chain.next
            l_plus_reversed_mid= l_plus_reversed_mid.next

        while head:
            chain.next=head 
            head=head.next
            chain=chain.next
        
        return dummy_chain.next

        





def list_to_linked_list(l):

    dummyHead = ListNode(0)
    curr = dummyHead
    for i in l:
        curr.next = ListNode(i)
        curr = curr.next



    return dummyHead.next 

if __name__ == "__main__":
    x=Solution()
    a=list_to_linked_list([1,2,3,4,5,6,7,8])
    c= x.reverseBetween(a,3,5)
    while c:
        print(c.val)
        c=c.next

