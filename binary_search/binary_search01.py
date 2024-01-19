
def searchInsert(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if target > nums[middle]:
            left = middle + 1
            # print(left)
        elif target < nums[middle]:
            right = middle - 1
        else:
            return middle
    return middle