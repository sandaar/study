import unittest


def sort(array):
    n = len(array)
    print id(array)
    if n in [0, 1]:
        return array
    max_item = (0, array[0])
    for i in xrange(0, n - 1):
        for j in xrange(0, n - 1 - i):
            if array[j] > max_item[1]:
                max_item = (j, array[j])
            print i, j, max_item
        
        tmp = array[n - 1]
        array[n - 1] = max_item[1]
        array[max_item[0]] = tmp
        print array
    return array

def test_one_item():
    array = [3]
    result = [3]
    sort(array)
    print('***\n\nTest sorting one item:\n{}'.format(array))
    return array == result

def test_empty_array():
    array = []
    result = []
    sort(array)
    print('***\n\nTest sorting empty array:\n{}'.format(array))
    return array == result

def test_sort_positive_integers():
    array = [3, 1, 4]
    print id(array)
    result = [1, 3, 4]
    array = sort(array)
    print('***\n\nTest sorting positive integers:\n{}'.format(array))
    return array == result

if __name__ == '__main__':
    print test_one_item()
    print test_empty_array()
    print test_sort_positive_integers()

