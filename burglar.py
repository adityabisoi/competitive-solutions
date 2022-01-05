houses=[3,8,10,4,1,7]
def func(houses,n):
    if n==0:
        return houses[0]
    if n==1:
        return houses[1]
    return max(houses[n]+func(houses,n-2),func(houses,n-1))

print(func(houses,5))