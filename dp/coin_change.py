def coin_change(a, d, count):
    count[0] += 1
    if a == 0:
        return 0
    if a < 0:
        return float('inf')
    return 1 + min([coin_change(a - di, d, count) for di in d])


def coin_change_dp(A, d):
    table = [float('inf')] * (A + 1)
    table[0] = 0

    for i in range(A + 1):
        if table[i] != float('inf'):
            for j in range(len(d)):
                candidate = i + d[j]
                if candidate <= A:
                    table[candidate] = min(table[candidate], table[i] + 1)
    print(table)
    #print_coins(table, A)
    print_coins_iterative(table, d)
    return table[A]

def print_coins(table, a):
    for i in range(len(d)):
        if a - d[i] <= 0:
            print(d[i])
            return
        if table[a - d[i]] == table[a] - 1:
            print_coins(table, a - d[i])
            print(d[i])

def print_coins_iterative(table, d):
    n = len(table)
    j = n - 1
    while j > 0:
        for i in range(len(d)):
            if table[j - d[i]] == table[j] - 1:
                print(d[i])
                j -= d[i]
                #print('table index', j)


if __name__ == '__main__':
    A = 8
    d = (2, 3, 5)
    count = [0]
    result_recurse = coin_change(A, d, count)
    print('Recursive. Minimum number of coins is {}\n# of recursive calls is {}\n'.format(
            result_recurse, count[0]))
    result_dp = coin_change_dp(A, d)
    print('DP. Minimum number of coins is', result_dp)
