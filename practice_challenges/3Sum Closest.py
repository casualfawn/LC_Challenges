
nums = [1,1,1,1]
sum(nums)
target = -100
#nums = [0,0,0]
#nums = [-1,2,1,-4]
seen = [[0,0,0]]
combos = [[0,0,0]]

target = -2
row = len(nums)
maxlen = 3
setnums = list()

nums = [4,0,5,-5,3,3,0,-4,-5]
nums.sort()
print(nums)
result, n = float('inf'), len(nums)
for i in range(n-2):
    s1 = nums[i] + nums[i+1] + nums[i+2]
    s2 = nums[i] + nums[n-2] + nums[n-1]
    candidates = [result, s1, s2]
    #print(candidates)
    result = min(candidates, key = lambda x:abs(x-target))
    if s1 <= target <= s2:
        left, right = i+1, n-1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            print(s)
            candidates = [result, s]
            if s == target:
                print(target)
                break
            elif s < target:
                left +=1
            else:
                right -=1
#print(result)

