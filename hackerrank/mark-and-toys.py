a, b = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
c = 0
for i in arr:
    if i <= b:
        c += 1
        b -= i
print(c)
