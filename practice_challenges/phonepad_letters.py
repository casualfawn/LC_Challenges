
charmap = {2: 'abc', 3:'defg', 4:'ghi', 5:'jkl', 6: 'mno', 7:'pqrs', 8:'tuv', 9: 'wxyz'}
digits = '23'
digits = [int(c) for c in digits]

charset = {}
for i in range(len(digits)):
    if digits[i] in charmap:
        charset[digits[i]] = charmap[digits[i]]

keys, values = zip(*charset.items())
result = [dict(zip(keys, p)) for p in itertools.product(*values)]
resfinal = [''] * len(result)

res = []
for c in result:
    for d in c:
        res.append(c[d])

res2 = []
n = len(digits)
for i in range(0, len(res), n):
    res2.append(res[i+n])






resfinal = []
i = 0
for c in result:
    for value in c:
        print(value)
        resfinal[i] = c[value]
        i+=1

resfinal

res = []
res2 = []
res2 = list(itertools.product(keyslist))

for sets in res2:
    res.append(itertools.product(sets))

keyslist = list(charset.values())
for sets in res:


i = 0
#get each first letter
for let in first:
# set how far for each first letter:
    for letters in next1:
        while i < len(res)/len(next1):
            res[i] += let
            res[i] += letters

            i+=1


res1 = 'a'


res = [''] * len(next1)

row = 0
down = 1
for let in first:
    res1 = let

res = [''] * len(next1)
for i in range(len(first)):
    for j in range(len(next1)):
        res[i] += first[i]
        res[i] += next1[i]


i = 0
while i < len(next1):
    res[row] += next1[i]
    if row == 0:
        down = 1
    if row == len(next1)-1:
        down = -1
    row += down
    i +=1

        res[i] += res1
        res[i] += next[i]

res