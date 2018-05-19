# Complete the function below.
def subsets(a, i, s, j, k):
    n = len(a)
    if i == n:
        if s[:j] == [] and k == 0:
            return False
        if sum(s[:j]) == k:
            #print(s[:j], k)
            return True
        return False
    if subsets(a, i + 1, s, j, k):
        return True
    s[j] = a[i]
    if subsets(a, i + 1, s, j + 1, k):
        return True
    return False
    
def check_if_sum_possible(arr, k):
    #print(type(arr), arr)
    #check_sum(arr, 0, k)
    n = len(arr)
    s = [None] * n
    return subsets(arr, 0, s, 0, k)


