import unittest


class TestQuicksort(unittest.TestCase):
    def test_empty(self):
        array = []
        n = len(array)
        start = 0
        end = n - 1
        result = quicksort(array, start, end)
        self.assertEqual(result, [])

    def test_median(self):
        array = [3, 3, 6, 11, 5, 7]
        n = len(array)
        start = 0
        end = n - 1
        result = choose_pivot(array, start, end)
        self.assertEqual(result, 2)

    def test_median_of_two(self):
        array = [3, 3, 6, 11, 5, 7]
        start = 1
        end = 2
        result = choose_pivot(array, start, end)
        self.assertEqual(result, 1)

    def test_median_of_two_same(self):
        array = [3, 3, 6, 6, 5, 7]
        start = 2
        end = 3
        result = choose_pivot(array, start, end)
        self.assertEqual(result, 2)

    def test_partition(self):
        array = [3, 3, 6, 6, 5, 7]
        n = len(array)
        start = 0
        end = n - 1
        p_index = choose_pivot(array, start, end)
        partition(array, start, end, p_index)
        expected = [3, 3, 6, 5, 6, 7]
        self.assertEqual(array, expected)

    def test_partition_index(self):
        array = [3, 3, 6, 6, 5, 7]
        n = len(array)
        start = 0
        end = n - 1
        p_index = choose_pivot(array, start, end)
        new_p_index = partition(array, start, end, p_index)
        expected = 4
        self.assertEqual(new_p_index, 4)

    def test_partition_two(self):
        array = [3, 3, 6, 11, 5, 7]
        start = 3
        end = 4
        p_index = choose_pivot(array, start, end)
        partition(array, start, end, p_index)
        expected = [3, 3, 6, 5, 11, 7]
        self.assertEqual(array, expected)

    def test_quicksort(self):
        array = [3, 3, 6, 11, 5, 7]
        n = len(array)
        start = 0
        end = n - 1
        quicksort(array, start, end)
        expected = [3, 3, 5, 6, 7, 11]
        self.assertEqual(array, expected)


def quicksort(array, start, end):
    if start == end or start == end + 1:
        return []
    p_index = choose_pivot(array, start, end)
    new_p_index = partition(array, start, end, p_index)
    quicksort(array, start, new_p_index - 1)
    quicksort(array, new_p_index + 1, end)

def choose_pivot(array, start, end):
    middle = start + (end - start) // 2
    median_list = [(array[start], start), (array[middle], middle), (array[end], end)]
    median_list.sort(key=lambda x: x[0])
    return median_list[1][1]

def partition(array, start, end, p_index):
    array[p_index], array[end] = array[end], array[p_index]
    p_value = array[end]

    i = start
    for curr in xrange(start, end):
        if array[curr] <= p_value:
            array[curr], array[i] = array[i], array[curr]
            i += 1

    array[end], array[i] = array[i], array[end]
    return i


if __name__ == '__main__':
    unittest.main()