height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def totalwatertrapped(heights):
    # create left and right pointers
    left = 0
    right = len(heights) - 1
    # create leftmax and rightmax variables
    leftmax = 0
    rightmax = 0
    # create total variable
    total = 0
    # while left < right
    while left < right:
        # if leftmax < rightmax
        if heights[left] < heights[right]:
            # if leftmax < left
            if heights[left] >= leftmax:
                # set leftmax to left
                leftmax = heights[left]
            # else
            else:
                # increment total by leftmax - left
                total += leftmax - heights[left]
            # increment left
            left += 1
        # else
        else:
            # if rightmax < right
            if heights[right] >= rightmax:
                # set rightmax to right
                rightmax = heights[right]
            # else
            else:
                # increment total by rightmax - right
                total += rightmax - heights[right]
            # decrement right
            right -= 1
    # return total
    return total
totalwatertrapped(height)

def totalwatertrapped(heights):
    # create left and right pointers
    left = 0
    right = len(heights) - 1
    # create leftmax and rightmax variables
    leftmax = 0
    rightmax = 0
    # create total variable
    total = 0
    for i in range(1,len(heights)-1):
        maxh = min(max(heights[left:i]), max(heights[i:right]))
        if maxh > heights[i]:
            total += maxh - heights[i]
    return total

print(totalwatertrapped(height))