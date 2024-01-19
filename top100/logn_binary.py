nums = [5,5,7,8,8,8,10]
target = 8
def findtargets(x, y):
    l = 0
    r = len(nums) - 1
    m = l + ((r - l) // 2)
    i = -1
    res = list()
    finres = list()
    while l < r:
        if nums[m] != target:
            m = ((r - l) // 2) + l
            if m < target:
                l = m + 1
            if m > target:
                r = m - 1
        elif nums[m] == target:
            i += 1
            l = m - i
            r = m + i
            if nums[l] == target:
                res.append(l)
            if nums[r] == target:
                res.append(r)
            if nums[l] != target and nums[r] != target:
                res.append(m)
                l = r
                finres.append(min(res))
                finres.append(max(res))
    return finres

res = findtargets(nums, target)
