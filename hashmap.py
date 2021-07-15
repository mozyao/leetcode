class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
        







class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.hashset=[None]* 1000
        
        

            
    

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashvalue = key % 1000
        
        if self.hashset[hashvalue] ==None:
            
            self.hashset[hashvalue]=Node((key,value))
        else :
            head= self.hashset[hashvalue]
            while head:
                k,v = head.data 
                if k==key:
                    head.data = (key,value)
                    return 
                if head.next==None:
                    break
                else:
                    head = head.next
            head.next= Node((key,value))
                    
        
                
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashvalue = key%1000
        if self.hashset[hashvalue]==None:
            return -1
        head = self.hashset[hashvalue]
        
        while head:
            k,v = head.data 
            if k==key:
                return v
            
            head = head.next
        return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        
        
        hashvalue=key% 1000
        if self.hashset[hashvalue]==None:
            return
        head = self.hashset[hashvalue]
        dummy_head = Node(0)
        curr = dummy_head
        while head:
            k,v = head.data
            if k==key:
                head=head.next
            curr.next=head
            curr= curr.next
            if head != None:
                
                head = head.next
            
        self.hashset[hashvalue]=dummy_head.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)