def domino(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return domino(n-1)+domino(n-2)

print(domino(5))