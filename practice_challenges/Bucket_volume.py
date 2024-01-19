height = [1,8,6,2,5,4,7,3,7]


def maxArea(self, height):
    # max volume
    left, right = 0, len(height) - 1
    # height.sort()
    res = list()
    while left <= right:
        if height[left] <= height[right]:
            res.append(min(height[right], height[left]) * (right - left))
            left += 1
            # print(res)
        else:
            res.append(min(height[right], height[left]) * (right - left))
            right -= 1
    return max(res)





maxarea = 0
maxh = 0
left = 0
right = len(grid)-1
res = list()
while left <= right:
    maxw = right-left
    maxarea = min(grid[left], grid[right]) * maxw
    if grid[left] <= grid[right]:
        left +=1
    else:
        right -=1
    res.append(maxarea)
