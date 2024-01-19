
nums = nums1 + nums2
left = 0
right = len(nums) - 1
nums.sort()

nums = nums1 + nums2
nums.sort()

left = 0
right = len(nums) - 1
while left < right:
    middle = (left + right) // 2
    if (middle % 2) != 0 and (len(nums) % 2 == 0):
        right = middle + 1
        left = middle
        print((nums[left] + nums[right]) / 2)
    else:
        print(nums[middle])





