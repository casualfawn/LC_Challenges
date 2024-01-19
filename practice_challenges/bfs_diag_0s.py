

grid = [[0,0,0],
        [1,1,0],
        [1,1,0],
        [1,0,0],
        [1,0,1],
        [1,0,0]]

res = 0
import heapq

hp = []
heapq.heappush(hp, [0,0,1])
grid[0][0] == 1

while hp:
    x,y,l = heapq.heappop(hp)

    for nx in [x-1, x, x+1]:
        for ny in [y-1,y,y+1]:
            if nx == len(grid) -1 and ny == len(grid[0]) -1:
                res = l

            if 0 <= nx and nx < len(grid) and 0 <= ny and ny < len(grid[0]):
                if grid[nx][ny] == 0:
                    heapq.heappush(hp, [nx, ny, l+1])
                    print(hp)
                    # Mark as visited
                    grid[nx][ny] = 1
