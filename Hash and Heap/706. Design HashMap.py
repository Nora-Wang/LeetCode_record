Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.



key和value被当作一组pair放在hash表中,当key值被映射到hash表的同一位置时,会发生conflict,这时为解决冲突会有两种方法open hashing和close hashing.
一般来说open hashing更简单,而且更好用.因此,这道题目其实就是写一个open hashing.

open hashing其实就是当发生conflict时,将统一index的pairs以链表的方式进行存储;
即不同key值通过hash function后得到的相同hash[index]以linkedlist的方式存储很多pairs[keys, values] # 因为在遇到相同key时，会renew value，因此用list更好，tuple不好改数据


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 1000这个值是由题目Note里的信息计算得出;后续的取模即实现hash function的功能
        self.capacity = 1000
        self.list = [None] * self.capacity

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        valid_key = key % self.capacity
        
        # linkedlist not exist
        if not self.list[valid_key]:
            self.list[valid_key] = ListNode([key, value])
            return
        
        # find the tail of the linkedlist
        head = curt = self.list[valid_key]
        while curt:
            # if key has already exist -> renew value
            if curt.val[0] == key:
                curt.val[1] = value
                return
            
            if not curt.next:
                curt.next = ListNode([key, value])
                return
            
            curt = curt.next
            
        return

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        valid_key = key % self.capacity
        
        # linkedlist not exist
        if not self.list[valid_key]:
            return -1
        
        # find key in the linkedlist
        curt = self.list[valid_key]
        while curt:
            if curt.val[0] == key:
                return curt.val[1]
            curt = curt.next
        
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        valid_key = key % self.capacity
        
        # find key's position in the linkedlist -> prev node for the key node; key node = curt
        dummy = prev = ListNode()
        curt = dummy.next = self.list[valid_key]
        while curt:
            # find key
            if curt.val[0] == key:
                break
            prev = curt
            curt = curt.next
        
        # key not exist in linkedlist
        if not curt:
            return
        
        # delete key node
        prev.next = curt.next
        self.list[valid_key] = dummy.next
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)





# 1/19/21
# 尽量 从key 得到一个固定且无规律的整数
# key = 'abc' = (a * 33^2 + b * 33^1 + c * 33^0) % hash_size -> index
# why 33: 取值都是一样的，只是取得特别小的话（如1，2）冲突会很多，从经验得到31和33是最好的（magic number）

# open hashing: [linkedList]，每次通过key得到index，然后将对应value放在linkedList的头部
# close hashing: 要是当前位置index被占了，则将原有数据往后挪（依次挪到空位处），再把当前数据放入index处 
#                close hashing不好的点：一旦发生冲突，可能需要挪动的数据很多，不好处理
class ListNode:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = None

class HashMap:
    def __init__(self) -> None:
        self.capacity = 1000
        self.list = [0] * self.capacity
    
    def put(self, key, value):
        index = self.get_index(key)
        
        if self.list[index] == 0:
            self.list[index] = ListNode(key, value)
            return
        
        head = self.list[index]
        while head:
            if head.key == key:
                head.val = value
                return
            head = head.next
        
        new_node = ListNode(key, value)
        new_node.next = head
        self.list[index] = new_node
            
    def get(self, key):
        index = self.get_index(key)

        if self.list[index] == 0:
            return -1

        head = self.list[index]
        while head:
            if head.key == key:
                return head.val
            head = head.next
        
        return -1

    def remove(self, key):
        index = self.get_index(key)

        if self.list[index] == 0:
            return
        
        dummy = prev = ListNode(None, None)
        head = self.list[index]
        while head:
            if head.key == key:
                prev.next = head.next
                break
            prev = head
            head = head.next
        
        self.list[index] = dummy.next
        return

    def get_index(self, key):
        index = 0
        for c in key:
            index = index * 33 + ord(c)
            index %= self.capacity
        return index

    
        
