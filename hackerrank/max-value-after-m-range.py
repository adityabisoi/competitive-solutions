for _ in range(int(input())):
    n,m=map(int,input().split())
    arr = [0]*n
    for _ in range(m):
        a,b,k=map(int,input().split())
        for i in range(a,b+1):
            arr[i]+=k
    print(max(arr))
