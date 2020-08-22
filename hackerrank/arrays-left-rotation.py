# a,n=input().split()
# arr=list(map(int,input().split()))
# for _ in range(int(n)):
#     x=arr[0]
#     arr.pop(0)
#     arr.append(x)
# print(*arr)
a, n = map(int, input().strip().split(' '))
arr = list(map(int, input().split()))
print(*arr[n:]+arr[:n])
