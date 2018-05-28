def  makeChange(C,  intDenominations):
    d = intDenominations
    table = [float('inf')] * (C + 1)
    table[0] = 0
    for i in range(C):
        for j in range(len(d)):
            tmp = i + d[j]
            if tmp <= C:
                table[tmp] = min(table[tmp], table[i] + 1)
    path = list()
    paths = dict()
    print_path(C, d, table, path, paths)
    for path in paths:
        print(','.join([str(c) for c in path]))
    
def print_path(C, d, table, path, paths):
    # cur = C
    # result = list()
    # while cur > 0:
    #     min_coins = table[cur - d[0]] 
    #     min_d = d[0]
    #     for j in range(len(d)):
    #         if table[cur - d[j]] < min_coins:
    #             min_coins = table[cur - d[j]]
    #             min_d = d[j]
    #     cur -= min_d
    #     result.append(min_d)
    # return result
    #print(path)
    if C == 0:
        path.sort()
        if tuple(path) not in paths:
            paths[tuple(path)] = True
        return
    min_coins = table[C - d[0]] 
    min_d = d[0]
    for j in range(len(d)):
        if table[C - d[j]] < min_coins:
            min_coins = table[C - d[j]]
            min_d = d[j]
    for j in range(len(d)):
        if table[C - d[j]] == min_coins:
            path.append(d[j])
            print_path(C - d[j], d, table, path, paths)
            path = list()

