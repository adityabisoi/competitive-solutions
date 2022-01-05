class BST:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_node(self,data):
        node=BST(data)
        if self.data==data:
            return
        elif data>self.data:
            if self.right:
                self.right.add_node(data)
            else:
                self.right=node
        else:
            if self.left:
                self.left.add_node(data)
            else:
                self.left=node

    def search(self,val):
        if self.data==val:
            return True
        elif val>self.data:
            if self.right:
                return self.right.search(val)
        else:
            if self.left:
                return self.left.search(val)
        return False

    def find_min(self):
        if self.left==None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right==None:
            return self.data
        return self.right.find_max()

    def in_order(self):
        el=[]
        if self.left:
            el+=self.left.in_order()
        el.append(self.data)
        if self.right:
            el+=self.right.in_order()
        return el

    def pre_order(self):
        el=[]
        el.append(self.data)
        if self.left:
            el+=self.left.in_order()
        if self.right:
            el+=self.right.in_order()
        return el

    def post_order(self):
        el=[]
        if self.left:
            el+=self.left.in_order()
        if self.right:
            el+=self.right.in_order()
        el.append(self.data)
        return el

def return_tree(arr):
    root=BST(arr[0])
    for i in range(1,len(arr)):
        root.add_node(arr[i])
    return root

arr=[5,8,2,4,1,6,9,10,15,18]
root=return_tree(arr)
# print(root.search(3))
# print(root.find_min())
# print(root.find_max())
print(root.in_order())