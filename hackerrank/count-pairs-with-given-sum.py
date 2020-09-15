arr = [1, 5, 7, 1]
element = 6
c = 0
for i in range(len(arr)):
    difference = element-arr[i]
    for j in range(i+1, len(arr)):
        if arr[j] == difference:
            c += 1
print(c)
