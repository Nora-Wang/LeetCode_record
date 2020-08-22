Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
addAtTail(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
 

Example:

Input: 
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1]]
Output:  
[null,null,null,null,2,null,3]

Explanation:
MyLinkedList linkedList = new MyLinkedList(); // Initialize empty LinkedList
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3
 

Constraints:

0 <= index,val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail,  addAtIndex and deleteAtIndex.



# 08/22/2020
# 这种方法虽然时间复杂度更高，但个人觉得更match linkedlist的概念
# 因为对于linkedlist来说，并没有len() function，所以也不存在self.size；如果要知道整个linkedlist的长度，必须要用O(n)的时间遍历一遍
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
    
    # time: O(n)
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # match index
        count = 0
        
        # cannot change self.head -> create a new pointer to self.head
        curt = self.head
        while curt:
            if count == index:
                return curt.val
            
            curt = curt.next
            count += 1
        
        return -1
    
    # time: O(1)
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_head = ListNode(val, self.head)
        self.head = new_head
    
    # time: O(n)
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        tail = self.head
        while tail.next:
            tail = tail.next
            
        new_tail = ListNode(val)
        tail.next = new_tail
    
    # time: O(n)
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # utilize the index to find the information
        # prev.next = curt node = index node
        # count match the index -> varify whether the index node exist in the linkedlist
        # maybe the index == 0 -> set dummy
        prev, curt, count, dummy = self.find_index_node(index)
        
        # index node not exist in the linkedlist
        if count != index:
            return
        
        # add node
        new_node = ListNode(val)
        prev.next = new_node
        new_node.next = curt
        self.head = dummy.next
        
    # time: O(n)
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        prev, curt, count, dummy = self.find_index_node(index)
        
        # 1. index not find
        # 2. index == len(linkedlist) -> no node need to be delete
        # valide index range: [0, len(linkedlist)]
        if count != index or not curt:
            return
        
        prev.next = curt.next
        self.head = dummy.next
    
    # time: O(n)
    def find_index_node(self, index: int):
        curt = self.head
        count = 0
        dummy = ListNode(None, self.head)
        prev = dummy
        
        while curt:
            if count == index:
                break
            
            prev = curt
            curt = curt.next
            count += 1
        
        return prev, curt, count, dummy


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)





# prev version
在add和delete的时候,将index=0的情况都corner case处理一下

code:
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #直接用head,不用dummy
        self.head = None
        #用size记录长度,便于后续对index进行范围判断
        self.size = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        #index的取值范围:0~length - 1
        if index < 0 or index >= self.size:
            return -1
        
        curt = self.head
        
        for _ in range(index):
            curt = curt.next
            
        return curt.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        #直接是在index为0的地方add new_node
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        #直接是在index为self.size的地方add new_node
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        #这里要注意,index可以==self.size,即在末尾加值
        if index > self.size:
            return
        
        #这个很tricky
        if index < 0:
            index = 0
        
        new_node = ListNode(val)
        
        #为0的情况 corner case一下
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return
        
        curt = self.head
        for _ in range(index - 1):
            curt = curt.next
            
        new_node.next = curt.next
        curt.next = new_node
        
        self.size += 1
            
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        
        #index为0的情况corner case一下
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        
        curt = self.head
        for _ in range(index - 1):
            curt = curt.next
            
        curt.next = curt.next.next
        
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
