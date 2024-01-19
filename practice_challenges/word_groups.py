groups = [1,2,2]
w = ['bab', 'dab', 'cab']
groups = [1,2,2]
charmap = {}
res = ''
for i in range(len(w)-1):
    num = w[i]
    curr_g = groups[i]
    nex_g = groups[i+1]
    for j in range(len(num)):
        if num[j] in charmap and groups[i] != groups[i+1]:
            res += num[j]
            charmap[num[j]] = j
        else:
            charmap[num[j]] = j
temp = []
for key, values in charmap.items():
    if values != 0:
        temp.append(values)
