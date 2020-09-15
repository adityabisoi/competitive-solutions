# Python3 program to convert a tree
# into its sum tree

# root defintion
class root:

	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

# Convert a given tree to a tree where
# every root contains sum of values of
# roots in left and right subtrees
# in the original tree


def toSumTree(root):

	# Base case
	if(root == None):
		return 0

	# Store the old value
	old_val = root.data

	# Recursively call for left and
	# right subtrees and store the sum as
	# new value of this root
	root.data = toSumTree(root.left) + \
            toSumTree(root.right)

	# Return the sum of values of roots
	# in left and right subtrees and
	# old_value of this root
	return root.data + old_val

# A utility function to print
# inorder traversal of a Binary Tree


def printInorder(root):
	if (root == None):
		return
	printInorder(root.left)
	print(root.data, end=" ")
	printInorder(root.right)

# Utility function to create a new Binary Tree root


def newroot(data):
	temp = root(0)
	temp.data = data
	temp.left = None
	temp.right = None

	return temp


# Driver Code
if __name__ == "__main__":
	root = None
	x = 0

	# Constructing tree given in the above figure
	root = newroot(10)
	root.left = newroot(-2)
	root.right = newroot(6)
	root.left.left = newroot(8)
	root.left.right = newroot(-4)
	root.right.left = newroot(7)
	root.right.right = newroot(5)

	toSumTree(root)

	# Print inorder traversal of the converted
	# tree to test result of toSumTree()
	print("Inorder Traversal of the resultant tree is: ")
	printInorder(root)

