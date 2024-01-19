nums1 = [1,3]
nums2 = [2,4]


if nums2:
    for i in nums2:
        nums1.append(i)
        nums1.sort()

if len(nums1) %2 == 0:
    m = ((len(nums1) - 1) //2)
    mr = m +1
    med = (nums1[m] + nums1[mr]) / 2
elif len(nums1) %2 != 0:
    m = ((len(nums1) - 1)//2)
    med = nums1[m]
