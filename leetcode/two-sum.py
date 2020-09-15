nums = [3,3]
target = 6
dict = {}
for i, j in enumerate(nums):
    diff = target-j
    if diff in dict:
        print(dict[diff], i)
    else:
        dict[j] = i
