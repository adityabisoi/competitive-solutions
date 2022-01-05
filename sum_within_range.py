nums=[1,-2,3,10,-8,0]

def func(nums,i,j):
    for x in range(1,len(nums)):
        nums[x]=nums[x]+nums[x-1]
    if i==0:
        return nums[j]
    return nums[j]-nums[i-1]

print(func(nums,0,4))