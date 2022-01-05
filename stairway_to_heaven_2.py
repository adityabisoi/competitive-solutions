# Can take 1 or 2 steps
def stairway(nums,n):
    if n==1 or n==2 or n==3:
        return nums[0]
    return min((stairway(nums,n-1)+nums[n-2]),(stairway(nums,n-2)+nums[n-3]))

print(stairway([2,1,3,1,2],4))