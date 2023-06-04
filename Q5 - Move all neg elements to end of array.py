def move(nums):
    n = len(nums)
    j = 0 
    for i in range(n):
        if nums[i] < 0 :
            nums[i],nums[j] = nums[j],nums[i]
            j = j + 1
    return nums
bk = [-2,-1,2,3,4,-2,-3]
result = move(bk)
print(result)
        




    




