nums = '2'
nums = [s for s in nums]
res = ''
charmap = {}
for s in nums:
    if s in charmap:
        charmap[s] += 1
    else:
        charmap[s] = 1

for key, val in charmap.items():
    res += str(val)
    res += str(key)

print(res)



s = '1'
n = 4
for _ in range(n - 1):
    print('_')
    print(_)
   # print(_)
    let, temp, count = s[0], '', 0
    for l in s:
        print(l)
        if let == l:
            count += 1
            print(count)
        else:
            print(temp)
            temp += str(count) + let
            let = l
            count = 1
    temp += str(count) + let
    s = temp
temp
