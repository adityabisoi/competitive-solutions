arr = [1, 3, 2, 5, 4]
n = len(arr)
mid = (n-1)//2
new = [None]*n
new[mid] = arr[0]
arr.sort()
j = 1
for i in range(1, mid+1):
    new[mid+i] = arr[j]
    j += 1
    new[mid-i] = arr[j]
    j += 1
print(new)
