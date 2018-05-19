def print_subsets(a, i, s, j):
    n = len(a)
    if i == n:
        print(s[:j])
        return
    print_subsets(a, i + 1, s, j)
    s[j] = a[i]
    print_subsets(a, i + 1, s, j + 1)

def print_subsets_less_1000(a, i, s, j):
    n = len(a)
    if i == n:
        if sum(s[:j]) < 1000:
            print(s[:j])
            return
        else:
            return
    if sum(s[:j]) < 1000:
        print_subsets_less_1000(a, i + 1, s, j)
    s[j] = a[i]
    if sum(s[:j]) < 1000:
        print_subsets_less_1000(a, i + 1, s, j + 1)

def print_subsets_greater_1000(a, i, s, j):
    n = len(a)
    if i == n:
        if sum(s[:j]) > 1000:
            print(s[:j])
            return
        else:
            return
    print_subsets_greater_1000(a, i + 1, s, j)
    s[j] = a[i]
    print_subsets_greater_1000(a, i + 1, s, j + 1)


if __name__ == '__main__':
    #a = ['t', 'a', 'c', 'o']
    #n = len(a)
    #s = [None] * n 
    #print_subsets(a, 0, s, 0)
    a = [999, 990, 3]
    n = len(a)
    s = [None] * n 
    #print_subsets_less_1000(a, 0, s, 0)
    print_subsets_greater_1000(a, 0, s, 0)
