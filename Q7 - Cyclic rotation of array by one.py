nums = list(map(int,input().strip().split()))
k = len(nums)
print(nums[k-1 : k] + nums[0 : k-1])

