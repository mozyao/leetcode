class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size=1000000
        self.hashset=[None]* self.size
        
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashvalue = key % self.size
        
        if self.hashset[hashvalue] != None and key in self.hashset[hashvalue]:
            return True
        return False
        

    def add(self, key: int) -> None:
        hashvalue = key % self.size
        
        if self.hashset[hashvalue] ==None:
            self.hashset[hashvalue]=[key]
        if self.contains(key) == False:
            self.hashset[hashvalue].append(key)
            
        
        

    def remove(self, key: int) -> None:
        hashvalue = key % self.size
        if self.contains(key):
            self.hashset[hashvalue].remove(key)
        
        
        


            
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)