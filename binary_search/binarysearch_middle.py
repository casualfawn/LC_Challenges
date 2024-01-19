nums = [2,7,11,15]
charmap = {}
for i in range(len(nums)):
    diff = target - nums[i]
    if diff not in charmap:
        charmap[nums[i]] = i
    elif diff in charmap:
        res = [charmap[diff], i]
