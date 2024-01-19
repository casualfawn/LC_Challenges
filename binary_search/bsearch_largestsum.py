nums = [7,2,5,10,8]
col = len(nums)

l = max(nums)
r = sum(nums)
res = r


def cansplit(maxres):
    subarr = 0
    currsum = 0
    for n in nums:
        currsum += n
        if currsum > maxres:
            subarr += 1
            currsum = n
    return subarr +1 <= m



while l <= r:
    m = l + (r-1) // 2
    if cansplit(m):
        res = m
        r = m - 1
    else:
        l = m+1

