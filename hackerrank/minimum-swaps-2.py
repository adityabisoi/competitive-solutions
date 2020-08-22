def sort(x, arr):
    c = 0
    i=0
    while(i<x):
        if arr[i]==i+1:
            i+=1
            break
        arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
        c+=1
    return c

print(sort(int(input()), list(map(int, input().split()))))
