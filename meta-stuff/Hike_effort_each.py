#find all the possible paths and the one requiring least effort between moves
grid =[[1,2,2],
       [3,8,2],
       [5,9,5]]

import heapq
hp = []
i,j = 0,0
seen = set()
seen.add((0,0))
row = len(grid)
col = len(grid[0])
eff = 0
res = 0
while (i,j) != (row-1, col-1):

    if i+1 != row and (i+1, j) not in seen:
       eff = abs(grid[i][j] - grid[i+1][j])
       heapq.heappush(hp, [eff, i+1, j])

    if i-1 >= 0 and (i-1, j) not in seen:
        eff = abs(grid[i][j] - grid[i-1][j])
        heapq.heappush(hp, [eff, i-1, j])

    if j+1 != col and (i, j+1) not in seen:
        eff = abs(grid[i][j] - grid[i][j+1])
        heapq.heappush(hp, [eff, i, j+1])

    if j-1 >= 0 and (i, j-1) not in seen:
        eff = abs(grid[i][j] - grid[i][j-1])
        heapq.heappush(hp, [eff, i, j-1])

    eff, p, q = heapq.heappop(hp)
    i,j = p,q
    res = max(eff, res)
    seen.add((i,j))

print(eff)
