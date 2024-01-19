nums = [2,1,5,3]
target = 4
valmap = {}

for i in range(len(nums)):
    curdiff = target - nums[i]
    if curdiff not in valmap:
        valmap[nums[i]] = i
    elif curdiff in valmap:
        res = [valmap[curdiff], i]