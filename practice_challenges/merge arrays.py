nums = [1,1,2,1]
charmap = {}
res = 0
numres = []
for i in range(len(nums)):
    if nums[i] not in charmap:
        res +=1
        charmap[nums[i]] = i
        numres.append(nums[i])
return numres