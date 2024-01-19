grid = [[0,0,0],[0,1,0],[0,0,0]]

if grid[0][0] == 1 or grid[len(grid)-1][len(grid[0])-1]:
    res = -1
    #return res

if len(grid) == 2:
    res = 1
    #return res

row = len(grid)
col = len(grid[0])
hp = []
import heapq
seen = set()
seen.add((0,0))
res = list()
i,j = 0,0
maxeff = 0
while (i,j) != (row-1, col-1):

    if i+1 == len(grid)-1 and j+1 == len(grid[0])-1:
        ans = len(res)


    if i+1 < len(grid) and (i+1, j) not in seen:

        if grid[i+1][j] == 0:
            maxeff = 1

            heapq.heappush(hp, [maxeff, i+1, j])

    if i-1 >= 0 and (i-1, j) not in seen:

        if grid[i - 1][j] == 0:
            maxeff = 1

            heapq.heappush(hp, [maxeff, i - 1, j])

    if j + 1 < len(grid[0]) and (i , j+1) not in seen:

        if grid[i][j+1] == 0:
            maxeff = 1

            heapq.heappush(hp, [maxeff, i, j+1])

    if j-1 >= 0 and (i, j-1) not in seen:

        if grid[i][j-1] == 0:
            maxeff = 1
            heapq.heappush(hp, [maxeff, i, j - 1])

    if (i,j) == (row, col):
        maxeff +=1
        heapq.heappush(hp, [maxeff, i, j - 1])


    maxeff, p, q = heapq.heappop(hp)
    i,j = p,q
    seen.add((i,j))
    res.append(maxeff)
    #return res
#res = len(res)
    #return res