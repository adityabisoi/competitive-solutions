from collections import Counter
input()
str1 = input().split()
str2 = input().split()
if(Counter(str2)-Counter(str1) == {}):
    print("Yes")
else:
    print("No")
