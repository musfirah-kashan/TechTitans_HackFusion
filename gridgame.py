def new_grid(grid):
    for row in grid:
        print(" ".join(str(no) for no in row))
def empty_grid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None
def valid_grid(grid, row, col, no):
    if no in grid[row]:
        return False
    for i in range(9):
        if grid[i][col] == no:
            return False
    r = (row // 3) * 3
    c = (col // 3) * 3
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            if grid[i][j] == no:
                return False
    return True
def modify_grid(grid):
    empty = empty_grid(grid)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if valid_grid(grid, row, col, num):
            grid[row][col] = num
            if modify_grid(grid):
                return True
            grid[row][col] = 0
    return False
grid_game = [
    [5, 3, 0, 0, 6, 0, 0, 0, 0],[6, 0, 0, 1, 9, 5, 0, 0, 0],[0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 7, 0, 0, 0, 3],[4, 0, 0, 8, 0, 3, 0, 0, 1],[7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],[0, 0, 0, 4, 1, 9, 0, 0, 5],[0, 0, 0, 0, 8, 0, 0, 7, 9]
]
if modify_grid(grid_game):
    new_grid(grid_game)
else:
    print("Error")    

