from collections import Counter
pairs = 0
input()
for i in Counter(list(map(int, input().split()))).values():
    pairs += (i//2)
print(pairs)
