class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        grid = [[False] * 9 for _ in range(9)]

        for row_ele in range(9):
            for col_ele in range(9):
                if board[row_ele][col_ele] != '.':
                    num = ord(board[row_ele][col_ele]) - ord('1')
                    grid_ele = (row_ele//3)*3+(col_ele//3)
                    if row[row_ele][num] or column[col_ele][num] or grid[grid_ele][num]:
                        return False
                    row[row_ele][num] = column[col_ele][num] = grid[grid_ele][num] = True
        return True     