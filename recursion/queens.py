import copy

def is_valid(array, end):
    for i in range(end):
        for j in range(i + 1, end):
            if abs(i - j) == abs(array[i] - array[j]):
                return False
    return True

def n_queens(array, i, result):
    n = len(array)
    if i == n:
        if is_valid(array, i):
            result.append(copy.deepcopy(array))
        return

    for j in range(i, n):
        array[i], array[j] = array[j], array[i]
        if is_valid(array, i):
            n_queens(array, i + 1, result)
        array[i], array[j] = array[j], array[i]

def print_grids(grids):
    for grid in grids:
        print('Grid start')
        for row in grid:
            print(row)
        print('Grid end\n')

if __name__ == '__main__':
    N = 4
    array = [i for i in range(N)]
    print(array)
    result = []
    n_queens(array, 0, result)
    print(result)

    output = []
    for r in result:
        grid = []
        for i in range(N):
            s = ['-'] * N
            s[r[i]] = 'q'
            grid.append(s)
        output.append(grid)
    print_grids(output)
