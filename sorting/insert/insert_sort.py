import unittest


class TestInsertSort(unittest.TestCase):
    def test_sort(self):
        array = [10, 11, 15, 16, 12, 2]
        insert_sort(array)
        expected = [2, 10, 11, 12, 15, 16]
        self.assertEqual(array, expected)

    def test_empty(self):
        array = []
        insert_sort(array)
        self.assertEqual(array, [])

    def test_one_item(self):
        array = [3]
        insert_sort(array)
        self.assertEqual(array, [3])

    def test_duplicates(self):
        array = [10, 11, 15, 15, 16, 12, 2]
        insert_sort(array)
        expected = [2, 10, 11, 12, 15, 15, 16]
        self.assertEqual(array, expected)

def insert_sort(array):
    n = len(array)
    if n in [0, 1]:
        return array
    for i in xrange(1, n):
        if array[i] < array[i - 1]:
            j = i - 1
            tmp = array[i]
            while array[j] > tmp:
                j -= 1
            del array[i]
            array.insert(j + 1, tmp)


if __name__ == '__main__':
    unittest.main()


