nums1 = [1,3]
nums2 = [2,4]

nums = nums1 + nums2
nums.sort()
nums

m = ((len(nums)-1)//2)
if len(nums) %2 != 0:
    res = nums[m]
if len(nums) %2 == 0:
    res = (nums[m] + nums[m+1]) / 2