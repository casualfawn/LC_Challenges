class Solution:
    """
    Level0: []
    level1: [1]                  [2]              [3]
    level2: [1,2]    [1,3]       [2,1] [2,3]      [3,1] [3,2]
    level3: [1,2,3]  [1,3,2]     [2,1,3][2,3,1]   [3,1,2][3,2,1]



for right in len abcbbacb
level0:
    """
s = "abcacwxyz"
n = len(s)
maxLength = 0
charMap = {}
left = 0

for right in range(7):
    if s[right] not in charMap or charMap[s[right]] < left:
        charMap[s[right]] = right
       # print(charMap[s[right]])
       # print(right)
        maxLength = max(maxLength, right - left + 1)
        print(charMap)
    else:
        left = charMap[s[right]] + 1
        print('current left is:')
        print(left)
        print('current right is..')
        print(right)
        print(charMap[s[right]])
        charMap[s[right]] = right
        print(charMap)

print(maxLength)


# 0 :   s0 = a  not in charmap. charmap = 0
# 1 : s0 = b not in charmap     charmap = 0,1
# 2 : s0 = c in car map         charmap = 0,1,2
# 3 : s3 = a in car map  left = 0  charmap = 0,1,2  left = 3  charmap = 0,1,2,3


# tunnel sabotage > destroy special forces craft

# underground exploration depth 3 > intercept red guns

s = "abcacwxyz"
n = len(s)
maxLength = 0
charmap = {}
left = 0



for right in range(len(s)):
    if s[right] not in charmap:
        charmap[s[right]] = right
        maxLength = max(maxLength, right - left +1)
    else:
        charmap[s[right]] = right
        left = charmap[s[right]]


