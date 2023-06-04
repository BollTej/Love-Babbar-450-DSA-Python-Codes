nums = list(map(int,input().strip().split()))
max_sum = 0 
current_sum = 0 
start = end = 0
for i in range (len(nums)):
    if current_sum <= 0 :
        start = i 
        current_sum = nums[i]
    else :
        current_sum += nums[i]

    if current_sum > max_sum :
        max_sum = current_sum
        end = i
        
subarray = nums[start : end+1]
print(max_sum)
print(subarray)





