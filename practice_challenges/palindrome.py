
s = list('cbbd')
s = list("babad")
n = len(s)
left, right = 0, n-1
res = ''
res2 = list()
for i in range(len(s)-1):
    l = s[i]
    right = n-1
    while left < right:
        if l == s[right]:
            print(l)
            print(s[right])
            res += l
            #left +=1
            right -=1
            left+=1
        else:
            right -=1
    res2.append(res)
   # left +=1
#left +=1
print(res)
print(res2)
