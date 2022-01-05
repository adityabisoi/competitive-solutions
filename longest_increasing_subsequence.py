# Longest subsequence with elements in increasing order
def lcs(nums):
    l=[0]*len(nums)
    for i in range(len(nums)):
        max=0
        for j in range(i):
            if nums[j]<nums[i] and l[j]>max:
                max=l[j]
        l[i]=max+1
    return l


print(lcs([11,23,10,37,21,50,80]))