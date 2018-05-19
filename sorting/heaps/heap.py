class MinHeap(object):
    def __init__(self):
        self.size = 0
        self.container = [None]

    def get_min(self):
        return self.container[1]

    def insert(self, item):
        self.container.append(item)
        self.size += 1
        self.heapify_up(self.size)

    def heapify_up(self, i):
        while i > 1 and self.container[i][2] < self.container[i // 2][2]:
            self.container[i], self.container[ i // 2] = self.container[i // 2], self.container[i]
            i //= 2

    def delete_min(self):
        if self.size == 0:
            return
        self.container[1] = self.container[self.size]
        self.size -= 1
        self.heapify_down(1)

    def gt_left_kid(self, i):
        if 2 * i <= self.size:
            return self.container[i] > self.container[2 * i]
        else:
            raise IndexError

    def gt_right_kid(self, i):
        if 2 * i + 1 <= self.size:
            return self.container[i] > self.container[2 * i + 1]
        else:
            raise IndexError

    def heapify_down(self, i):
        while self.has_kids(i):
            if not self.has_right_kid(i) and self.gt_left_kid(i):
                self.container[i], self.container[2 * i] = self.container[2 * i], self.container[2 * i]
                i *= 2
            elif self.has_right_kid(i):
                if  self.gt_left_kid(i) and not self.gt_right_kid(i):
                    self.container[i], self.container[2 * i] = self.container[2 * i], self.container[i]
                    i *= 2
                elif not self.gt_left_kid(i) and self.gt_right_kid(i):
                    self.container[i], self.container[2 * i + 1] = self.container[2 * i + 1], self.container[i]
                    i = 2 * i + 1
                elif self.gt_left_kid(i) and self.gt_right_kid(i):
                    if self.container[2 * i] <= self.container[2 * i + 1]:
                        self.container[i], self.container[2 * i] = self.container[2 * i], self.container[i]
                        i *= 2
                    else:
                        self.container[i], self.container[2 * i + 1] = self.container[2 * i + 1], self.container[i]
                        i = 2 * i + 1
                else:
                    return

    def has_kids(self, i):
        return 2 * i <= self.size

    def has_right_kid(self, i):
        return 2 * i + 1 <= self.size

    def print_family(self, i):
        if i > self.size or i < 1:
            raise IndexError
        print(self.container[i][2])
        if self.has_kids(i):
            print(self.container[2*i][2])
            if self.has_right_kid(i):
                print(self.container[2 * i + 1][2])

    def print_subtree(self, i):
        if i == 1:
            self.print_family(i)
        if self.has_kids(i):
            self.print_subtree(2 * i)
            if self.has_right_kid(i):
                self.print_subtree(2 * i + 1)

    def print_tree(self):
        self.print_subtree(1)

if __name__ == '__main__':
    heap = MinHeap()
    heap.insert((0, 0, 0))
    heap.insert((1, 0, 2))
    heap.insert((2, 0, 3))
    heap.insert((3, 0, 3))
    heap.insert((4, 0, 10))
    heap.insert((5, 0, 15))
    print('Initial tree')
    heap.print_tree()
    print(heap.container)
    print('Deleting min')
    heap.delete_min()
    print('Final tree')
    heap.print_tree()
    print(heap.container)
