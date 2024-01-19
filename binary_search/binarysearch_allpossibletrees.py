nums = [2,7,11,15]
target = 9

l = 0
r = len(nums)-1
valmap = {}
res = list()

while l < r:
    m = ((r-1) // 2) + l
    valmap[m] = target - nums[m]
    if nums[m] > target:
        r-=1

    if target - nums[m] in valmap:
        res.append(nums[m])
        res.append(valmap[nums[m]])


