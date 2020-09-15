# Python3 program to find a sorted subsequence
# of size 3 using constant space

# Function to fund a sorted subsequence of size 3


def find3Numbers(arr, n):

	# Initializing small and large(second smaller)
	# by INT_MAX
	small = +2147483647
	large = +2147483647

	for i in range(n):

		# Update small for smallest value of array
		if (arr[i] <= small):
			small = arr[i]

		# Update large for second smallest value of
		# array after occurrence of small
		elif (arr[i] <= large):
			large = arr[i]

		# If we reach here, we found 3 numbers in
		# increasing order : small, large and arr[i]
		else:
			break

	if (i == n):

		print("No such triplet found")
		return

	# last and second last will be same, but
	# first element can be updated retrieving
	# first element by looping upto i
	for j in range(i + 1):

		if (arr[j] < large):

			small = arr[j]
			break

	print(small, " ", large, " ", arr[i])
	return


# Driver program
arr = [5, 7, 4, 8]
n = len(arr)
find3Numbers(arr, n)
