n, q = map(int, input().split())
arr = [0]*(n+1)
while(q > 0):
    a, b, k = map(int, input().split())
    arr[a-1] += k
    arr[b] -= k
    q -= 1
sum = 0
c = 0
for i in arr:
    c += i
    if c > sum:
        sum = c
print(sum)
