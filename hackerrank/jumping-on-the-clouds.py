n = int(input())
c = list(map(int, input().split()))
c.append(0)
count = 0
i = 0
while (i < n-1):
    i += (c[i+2] == 0) + 1
    count += 1
print(count)
