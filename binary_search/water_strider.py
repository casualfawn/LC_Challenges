
grid = [['.', '.', '.'],
        ['.', '@', '@'],
        ['.', '.', '.'],
        ['@', '.', '@'],
        ['@', '.', '@'],
        ['.', '.', '.']]

grid = [['.', '.', '.'],
        ['.', '@', '.'],
        ['.', '@', '.'],
        ['@', '.', '.'],
        ['@', '.', '@'],
        ['.', '.', '.']]


maze = grid


r = 0
c = 0
queue = [] # use a local variable, not a member
visited = {} # use a dict, key = coordinate-tuples, value = previous location
visited[(r, c)] = (-1, -1)
queue.append((r, c))
while len(queue) > 0: # don't use running as variable
    # no need to use current; just reuse r and c:
    r, c = queue.pop(0) # you can remove immediately from queue
    if (r,c) == (len(grid)-1,len(grid[0])-1):
        # build path from walking backwards through the visited information
        path = []
        while r != -1:
            path.append((r, c))
            r, c = visited[(r, c)]
        path.reverse()
    # avoid repetition of code: make a loop
    for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        new_r = r + dy
        new_c = c + dx
        if (0 <= new_r < len(maze) and
                0 <= new_c < len(maze[0]) and
                not (new_r, new_c) in visited and
                maze[new_r][new_c] != '@'):
            visited[(new_r, new_c)] = (r, c)
            queue.append((new_r, new_c))
path

