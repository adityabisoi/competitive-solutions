class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node

        else:
            i = self.head
            while(i.next != None):
                i = i.next
            i.next = node

    def length(self):
        i = self.head
        c = 0
        while(i != None):
            c += 1
            i = i.next
        return c

    def get_node(self, pos):
        i = self.head
        c = self.length()
        while(i != None):
            if pos == c:
                return i.data
            c -= 1
            i = i.next
        return c


ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
ll.add(6)
ll.add(7)
ll.add(8)
ll.add(9)
ll.add(10)
print(ll.get_node(2))
