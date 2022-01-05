def zeros(arr):
    l=0
    r=len(arr)-1
    while l<r:
        if arr[l] == 0:
            r-=1
        l+=1
    l=len(arr)-1
    c=0
    for i in range(r+1):
        if arr[i]==0:
            c+=1
    if r+c>l:
        arr[l]=arr[r]
        l-=1
        r-=1
    while r>=0:
        arr[l]=arr[r]
        l-=1
        if arr[r]==0:
            arr[l]=arr[r]
            l-=1
        r-=1

print(zeros([1,0,2,0,0,0,5,0]))