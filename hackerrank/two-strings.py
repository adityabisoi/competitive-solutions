# for _ in range(int(input())):
#     ar=[]
#     x = input()
#     y = input()
#     for i in x:
#         ar.append(i in y)
#     if(any(ar)):
#         print('YES')
#     else:
#         print('NO')

for _ in range(int(input())):
    x = set(input())
    y = set(input())
    print('YES' if x & y else 'NO')
