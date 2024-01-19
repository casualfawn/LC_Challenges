grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

res = 0
dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
seen = set()
i,j = 0,0

def dfs(curx, cury):
    seen.add((curx, cury))
    for movx, movy in dirs:
        x,y = curx+movx, cury+movy
        if x in range(len(grid)) and y in range(len(grid)[0])  and grid[x][y] == '1' and (x,y) not in seen:
            dfs(x,y)


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '1' and (i,j) not in seen:
            res +=1
            dfs(i,j)