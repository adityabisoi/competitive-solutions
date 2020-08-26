input()
arr = list(map(int, input().split()))
arr.sort()
min = 10**10
for i in range(len(arr)-1):
    if arr[i+1]-arr[i] < min:
        min = arr[i+1]-arr[i]
print(min)
