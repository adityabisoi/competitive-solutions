class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, val):
        firstNode = Node(val)
        if self.head is None:
            self.head = firstNode
        else:
            i = self.head
            self.head = firstNode
            self.head.next = i

    def insert_at_last(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            i = self.head
            while(i.next != None):
                i = i.next
            i.next = newNode

    def print_list(self):
        if self.head is None:
            print("Cannot print, linked list is empty")
        else:
            p = self.head
            while(p != None):
                print(p.val, sep=' ')
                p = p.next

    def returnHead(self):
        return self.head
    
def reverseList(head):
    if head.next==None:
        return head 
    else:
        currHead=head
        nextHead = reverseList(head.next)
        nextHead.next=currHead
        return currHead

myList = SinglyLinkedList()
myList.insert_at_last(1)
myList.insert_at_last(2)
myList.insert_at_last(3)
myList.insert_at_last(4)
# myList.insert_at_last(5)
head=myList.returnHead()
myList.print_list()
print('=======')
print(reverseList(head))
