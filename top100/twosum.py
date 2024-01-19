nums = [2,7,11,15]
target = 9
prevval = {}


for i in range(len(nums)):
    currdiff = target - nums[i]
    if currdiff not in prevval:
        prevval[nums[i]] = i
    elif currdiff in prevval:
        res = [prevval[currdiff], i]
