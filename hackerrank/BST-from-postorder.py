arr = [8, 12, 10, 16, 18, 32, 15]


def inorder(self):
    el = []
    if self.left:
        el += self.left.inorder()
    el.append(self.data)
    if self.right:
        el += self.right.inorder()
    return el


def function(arr, start, end):
    if start > end:
        return None
    else:
        root = Node(arr[end])
        i = end
        while(i >= start):
            if root.data > arr[i]:
                # i will point to the element from where right and left are to be divided
                break
            i = i-1
        root.right = function(arr, i+1, end-1)
        root.left = function(arr, start, i)
        return root

function(arr, 0, len(arr)-1)
