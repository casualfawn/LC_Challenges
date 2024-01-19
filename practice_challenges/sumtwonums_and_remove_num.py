
'''
P A Y
  P
A L I
  S
H I R
  I
N G

'''


### sum of two numbers == target
        res = []
        n = len(nums)
        for i in range(len(nums)):
            fn = nums[i]
            test = nums.copy()
            test.remove(fn)
            print(test)
            for j in range(len(test)):
                if fn + test[j] == target:
                   res.append(i)
        res = list(res)
        res = set(res)


nums = [3,2,2,3]
val = 3
def removeElement(nums, val):
    res = []
    res2 = 0
    nums = sorted(nums)
    for i in range(len(nums)):
        if nums[i] != val:
            res.append(nums[i])
            res2 += 1
    return res2, res

removeElement(nums, val)





