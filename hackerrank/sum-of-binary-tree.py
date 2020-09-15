# Python3 Program to print sum of all
# the elements of a binary tree

# Binary Tree Node

""" utility that allocates a new Node 
with the given key """


class newNode:

	# Construct to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# Function to find sum of all the element


def addBT(root):
	if (root == None):
		return 0
	return (root.key + addBT(root.left) +
         addBT(root.right))


# Driver Code
if __name__ == '__main__':
	root = newNode(1)
	root.left = newNode(2)
	root.right = newNode(3)
	root.left.left = newNode(4)
	root.left.right = newNode(5)
	root.right.left = newNode(6)
	root.right.right = newNode(7)
	root.right.left.right = newNode(8)

	sum = addBT(root)

	print("Sum of all the nodes is:", sum)

