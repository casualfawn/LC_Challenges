nums = [1,4,5,2,3]
k = 3

result = nums[0:k]
i = 1
while i < len(nums) - k +1:
    if nums[i] != result[0] and nums[i] > result[0]:
        result = nums[i:i+k]
        print('numsl, result0, result')
        print(nums[i], result[0], result)

    i +=1