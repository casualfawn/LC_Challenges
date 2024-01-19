height = [1,8,6,12,1,2,3,4,5,4,15,3,7]

res = list()
l = 0
r = len(height)-1
maxv = max(height)
while l < r:
    maxv = min(height[l], height[r]) * (r - l)
    res.append(maxv)
    if height[l] < height[r]:
        l +=1
    elif height[l] > height[r]:
        r -=1
