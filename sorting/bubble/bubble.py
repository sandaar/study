import unittest

class TestBubbleSort(unittest.TestCase):
    def test_empty_array(self):
        array = []
        result = bubble_sort(array)
        self.assertEqual(result, array)

    def test_one_item(self):
        array = [5]
        result = bubble_sort(array)
        self.assertEqual(result, array)

    def test_many_items(self):
        array = [16, 4, 8, 3, 0, 10]
        result = bubble_sort(array)
        expected_result = [0, 3, 4, 8, 10, 16]
        self.assertEqual(result, expected_result)

    def test_prebubble_sorted(self):
        array = [0, 3, 4, 8, 10, 16]
        result = bubble_sort(array)
        expected_result = [0, 3, 4, 8, 10, 16]
        self.assertEqual(result, expected_result)


def bubble_sort(array):
    n = len(array)
    if n in [0, 1]:
        return array
    if n in [0, 1]:
        return array
    for i in xrange(0, n):
        min_index = 0
        min_item = array[0]
        for j in xrange(0, n - i):
            if array[j] <= min_item:
                min_index = j
                min_item =  array[j]
        array.append(array[min_index])
        del array[min_index]
#        print "index {}, value {}".format(min_index, min_item)
#        print array
    return array

if __name__ == '__main__':
    unittest.main()
