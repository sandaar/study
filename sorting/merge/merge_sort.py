import math
import unittest


class TestMergeSort(unittest.TestCase):
    def test_sort(self):
        array = [5, 4, 12, 1, 2, 3, 10]
        start = 0
        n = len(array)
        end = n - 1
        merge_sort(array, start, end)
        expected = [1, 2, 3, 4, 5, 10, 12]
        self.assertEqual(array, expected)



def merge(array, start, mid, end):
    left = array[start : mid + 1]
    right = array[mid+1 : end + 1]

    i = start
    j = mid + 1
    k = start
    while i <= mid and j <= end:
        try:
            if left[i] <= right[j]:
                array[k] = left[i]
        except IndexError:
            print start, mid, end
            print left, right, array
            print i, j, k
            raise
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    
    if i != mid + 1:
        array[k:end] = left[i:mid]
    elif j != end + 1:
        array[k:end] = right[j:end]



def merge_sort(array, start, end):
    if start == end or start == end + 1:
        return
    mid = start + int(math.floor(float(end) - float(start))) // 2
    merge_sort(array, start, mid)
    merge_sort(array, mid + 1, end)
    # TODO test mid - 1, mid, mid + 1
    merge(array, start, mid, end)


if __name__ == '__main__':
    unittest.main()
