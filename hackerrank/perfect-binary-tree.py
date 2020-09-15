# Python3 program to check whether a
# given Binary Tree is Perfect or not

# Helper class that allocates a new
# node with the given key and None
# left and right pointer.
class newNode:
	def __init__(self, k):
		self.key = k
		self.right = self.left = None

# Returns depth of leftmost leaf.


def findADepth(node):
	d = 0
	while (node != None):
		d += 1
		node = node.left
	return d

# This function tests if a binary tree
# is perfect or not. It basically checks
# for two things :
# 1) All leaves are at same level
# 2) All internal nodes have two children


def isPerfectRec(root, d, level=0):

	# An empty tree is perfect
	if (root == None):
		return True

	# If leaf node, then its depth must
	# be same as depth of all other leaves.
	if (root.left == None and root.right == None):
		return (d == level + 1)

	# If internal node and one child is empty
	if (root.left == None or root.right == None):
		return False

	# Left and right subtrees must be perfect.
	return (isPerfectRec(root.left, d, level + 1) and
         isPerfectRec(root.right, d, level + 1))

# Wrapper over isPerfectRec()


def isPerfect(root):
	d = findADepth(root)
	return isPerfectRec(root, d)


# Driver Code
if __name__ == '__main__':
	root = None
	root = newNode(10)
	root.left = newNode(20)
	root.right = newNode(30)

	root.left.left = newNode(40)
	root.left.right = newNode(50)
	root.right.left = newNode(60)
	root.right.right = newNode(70)

	if (isPerfect(root)):
		print("Yes")
	else:
		print("No")
