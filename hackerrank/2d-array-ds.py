a = []
b = []
for _ in range(6):
    a.append(list(map(int, input().split())))
for i in range(4):
    for j in range(4):
        b.append(a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1]
                 [j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2])
print(max(b))
