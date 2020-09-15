# Python 3 program to Print all elements
# in sorted order from row and column
# wise sorted matrix
import sys

INF = sys.maxsize
N = 4

# A utility function to youngify a Young
# Tableau. This is different from standard
# youngify. It assumes that the value at
# mat[0][0] is infinite.


def youngify(mat, i, j):

	# Find the values at down and
	# right sides of mat[i][j]
	downVal = mat[i + 1][j] if (i + 1 < N) else INF
	rightVal = mat[i][j + 1] if (j + 1 < N) else INF

	# If mat[i][j] is the down right
	# corner element, return
	if (downVal == INF and rightVal == INF):
		return

	# Move the smaller of two values
	# (downVal and rightVal) to mat[i][j]
	# and recur for smaller value
	if (downVal < rightVal):
		mat[i][j] = downVal
		mat[i + 1][j] = INF
		youngify(mat, i + 1, j)

	else:
		mat[i][j] = rightVal
		mat[i][j + 1] = INF
		youngify(mat, i, j + 1)

# A utility function to extract minimum
# element from Young tableau


def extractMin(mat):

	ret = mat[0][0]
	mat[0][0] = INF
	youngify(mat, 0, 0)
	return ret

# This function uses extractMin() to
# print elements in sorted order


def printSorted(mat):

	print("Elements of matrix in sorted order n")
	i = 0
	while i < N * N:
		print(extractMin(mat), end=" ")
		i += 1


# Driver Code
if __name__ == "__main__":

	mat = [[10, 20, 30, 40],
            [15, 25, 35, 45],
            [27, 29, 37, 48],
            [32, 33, 39, 50]]
	printSorted(mat)
