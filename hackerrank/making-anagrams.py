str1 = list(input())
str2 = list(input())
c = []
for i in str1:
    if i in str2:
        str2.remove(i)
    else:
        c.append(i)
print(len(c)+len(str2))
