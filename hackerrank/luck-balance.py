def func(arr, k):
    sum = 0
    for i, j in arr:
        if j == 0:
            sum += i
        elif k > 0:
            sum += i
            k -= 1
        else:
            sum -= i
    print(sum)


n, k = map(int, input().split())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
arr.sort(reverse=True)
func(arr, k)
