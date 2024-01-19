class Solution(object):
    def isValidSudoku(self, board):
        dirs = [[1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2]]
        res = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                dot = '.'
                seen = []
                seen.append(board[i][j])
                for d in dirs:
                    box_moves = board[i + d[0]][j + d[1]]
                    seen.append(box_moves)
                    # print(seen)
                while dot in seen:
                    seen.remove(dot)
                if len(set(seen)) != len(seen):
                    res.append('not valid')
                    print(res)

        #res = []
        sud = board
        for i in range(len(sud)):
            columnn = ([row[i] for row in sud])
            while dot in columnn:
                columnn.remove(dot)
            if len(set(columnn)) != len(columnn):
                res.append('not valid')

        sud = board
        for num in sud:
            row = num
            dot = '.'
            while dot in row:
                row.remove('.')
            if len(set(row)) != len(row):
                res.append('not valid')

        if 'not valid' in res:
            return False
        else:
            return True