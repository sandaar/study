import unittest
import logging
import sys

logger = logging.getLogger(__name__)
logger.level = logging.INFO
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)


class TestBubbleSort(unittest.TestCase):
    def test_empty_array(self):
        array = []
        bubble_sort(array)
        self.assertEqual(array, [])

    def test_one_item(self):
        array = [5]
        bubble_sort(array)
        self.assertEqual(array, [5])

    def test_many_items(self):
        array = [16, 4, 8, 3, 0, 10]
        bubble_sort(array)
        expected = [0, 3, 4, 8, 10, 16]
        self.assertEqual(array, expected)

    def test_presorted(self):
        array = [0, 3, 4, 8, 10, 16]
        bubble_sort(array)
        expected = [0, 3, 4, 8, 10, 16]
        self.assertEqual(array, expected)

    def test_odd(self):
        array = [16, 4, 8, 3, 0, 10, 9]
        bubble_sort(array)
        expected = [0, 3, 4, 8, 9, 10, 16]
        self.assertEqual(array, expected)


def bubble_sort(array):
    ''' at any given loop iteration following is true:
            i is number of sorted elements 
            n - 1 - i is start index for sorted part of the array 
            j is index of an element that will be compared to right neighbor
    '''
    n = len(array)
    logger.debug("Start bubble sort\n%s", array)
    for i in xrange(0, n):
        logger.debug("i = %s", i)
        for j in xrange(0, n - 1 - i):
            logger.debug("j = %s", j)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            logger.debug(array)

if __name__ == '__main__':
    unittest.main()
