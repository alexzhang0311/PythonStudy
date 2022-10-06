'''
链表是一种线性数据结构，不需要一整块连续的存储空间，通过指针将零散内存连起来使用
链表中的每个内存块被称为链表的结点，每个结点记录上/下一个结点的地址以及当前结点的数据
特点：
1. 插入，删除效率高,复杂度O(1)
2. 随机查找效率低，只能遍历，复杂度O(n)
3. 消耗空间大

缺点：
1. 内存消耗大，用于存储结点指针信息
2. 频繁插入，删除操作，会导致频繁的内存申请，释放，容易造成内存碎片，导致频繁的GC

列表缺点：
1. 数组必须占用连续整块的内存空间，如果数组过大，则会导致内存不足
2. 扩容需要新申请空间，需要把原数组复制到新空间中
'''

##链表结点##
class ListNode:
    def __init__(self, x):
        ###链表结点值###
        self.val = x 
        ###链表结点指针###
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # sentinel node as pseudo-head
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        # index steps needed 
        # to move from sentinel node to wanted index
        for _ in range(index + 1):
            curr = curr.next
        return curr.val
            

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # If index is greater than the length, 
        # the node will not be inserted.
        if index > self.size:
            return
        
        # [so weird] If index is negative, 
        # the node will be inserted at the head of the list.
        if index < 0:
            index = 0
        
        self.size += 1
        # find predecessor of the node to be added
        pred = self.head
        for _ in range(index):
            #从第一个结点循环到index的上一个结点
            pred = pred.next 
            
        # node to be added
        to_add = ListNode(val)
        # insertion itself
        to_add.next = pred.next #当前结点的指针指向，之前上一个结点的指针指向的结点
        pred.next = to_add #上一个结点的指针指向当前结点
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return
        
        self.size -= 1
        # find predecessor of the node to be deleted
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        # delete pred.next 
        pred.next = pred.next.next

    def getprev(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        # index steps needed 
        # to move from sentinel node to wanted index
        for _ in range(index):
            curr = curr.next
        return curr.val
    
    def getnext(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        # index steps needed 
        # to move from sentinel node to wanted index
        for _ in range(index + 2):
            curr = curr.next
        return curr.val



###自己写的###
class ListNode():
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self):
        self.node = ListNode(0)
        self.size = 0
    def get(self,index):
        if index + 1 > self.size:
            return -1
        
        cur = self.node
        for _ in range(index+1):
            cur = cur.next
        return cur.val
    

    def addAtIndex(self,index,val):

        if index <= 0:
            cur = self.node
            print('头部结点')
            to_add = ListNode(val)
            to_add.next = cur.next
            cur.next = to_add
            self.size += 1
        else:
            if index == self.size:
                print('尾部结点')
                cur = self.node
                for _ in range(index):
                    cur =  cur.next
                to_add = ListNode(val)
                cur.next = to_add
                self.size += 1
            elif index < self.size:
                print('中间结点')
                cur = self.node
                for _ in range(index):
                    cur =  cur.next
            
                to_add = ListNode(val)
                to_add.next = cur.next
                cur.next = to_add

                self.size += 1

        
        if index > self.size:
            return -1

    def deleteAtIndex(self,index):
        cur = self.node
        if index + 1 <= self.size:
            for _ in range(index):
                cur = cur.next
            cur.next = cur.next.next
            self.size -= 1
        
    
    def addAtHead(self,val):
        self.addAtIndex(0, val)
    
    def addAtTail(self,val):
        self.addAtIndex(self.size, val)
