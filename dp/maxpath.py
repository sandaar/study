GRID = [
        [10, 5, 6],
        [1, 15, 2],
        [8, 3, 9],
        [11, 4, 7]
]
GRID2 = [
        [10, 2],
        [5, -1],
]

def print_grid(grid):
    print('Printing grid\n')
    n = len(grid)

    for i in range(n):
        print(grid[i])

    print('Finished printing grid\n')

def max_path(grid, r, c, n, m, recurse_count):
    recurse_count[0] += 1
    if r == n or c == m:
        return None
    #if r == n - 1 and c == m - 1:
    #    return grid[r][c]

    down = max_path(grid, r + 1, c, n, m, recurse_count)
    right = max_path(grid, r, c + 1, n, m, recurse_count)
    if down is None:
        if right is None:
            return grid[r][c]
        return grid[r][c] + right
    elif right is None:
        return grid[r][c] + down
    else:
        return grid[r][c] + max(down, right)
    #return grid[r][c] + max(
    #        max_path(grid, r + 1, c, n, m, recurse_count),
    #        max_path(grid, r, c + 1, n, m, recurse_count))

def max_path_memoize(grid, r, c, n, m, recurse_count, history):
    if (r, c) in history:
        return history[(r, c)]
    recurse_count[0] += 1
    if r == n or c == m:
        return 0
    if r == n - 1 and c == m - 1:
        history[(r, c)] = grid[r][c]
        return history[(r, c)]
    history[(r, c)] = grid[r][c] + max(
            max_path_memoize(grid, r + 1, c, n, m, recurse_count, history),
            max_path_memoize(grid, r, c + 1, n, m, recurse_count, history))
    return history[(r, c)]

def prepare_dp_table(grid):
    n = len(grid)
    m = len(grid[0])
    table = list()
    for i in range(n + 1):
        table.append(list())
        for _ in range(m):
            if i == n:
                table[i].append(0)
            else:
                table[i].append(None)
        table[i].append(0)
    return table

def max_path_dp(grid):
    n = len(grid)
    m = len(grid[0])
    table = prepare_dp_table(grid)

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            table[i][j] = grid[i][j] + max(table[i + 1][j], table[i][j + 1])
    print_grid(grid)
    print_grid(table)
    print_max_path(grid, table)
    return(table[0][0])

def print_max_path(grid, table):
    i, j = 0, 0
    n = len(grid)
    m = len(grid[0])
    while i < n and j < m:
        grid[i][j] = str(grid[i][j]) + '*'
        if table[i + 1][j] >= table[i][j + 1]:
            i += 1
        else:
            j += 1

    print_grid(grid)

if __name__ == '__main__':
    grid = GRID2
    n = len(grid)
    m = len(grid[0])
    recurse_count = [0]
    result = max_path(grid, 0, 0, n, m, recurse_count)
    print("Recursive max reward is {}.\nRecurse count {}".format(result, recurse_count))
    recurse_count_mem = [0]
    history = dict()
    result_mem = max_path_memoize(grid, 0, 0, n, m, recurse_count_mem, history)
    print("Recursive memoize max reward is {}.\nRecurse count {}".format(result_mem, recurse_count_mem))
    result_dp = max_path_dp(grid)
    print("DP max reward is", result_dp)
