import copy

def wildcard(array, i, result):
    print("Before ", i, array)
    if i == len(array):
        result.append(''.join(array))
        return
    if array[i] == '?':
        array[i] = '0'
        wildcard(array, i + 1, result)
        array[i] = '1'
        wildcard(array, i + 1, result)
        array[i] = '?' # why?
    else:
        wildcard(array, i + 1, result)
    print("After ", i, array, '\n\n')
        


if __name__ == '__main__':
    p = '1?0?'
    result = []
    wildcard(list(p), 0, result)
    print(result)
