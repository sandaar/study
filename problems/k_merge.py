class MinHeap(object):
    def __init__(self):
        self.size = 0
        self.container = list()

    def get_min(self):
        if size > 0:
            return self.container[0]
        else:
            return None
    
    def heapify_up(self, i):
        #print(i)
        #print(self.container)
        #print(self.container[i][2], self.container[ i // 2 ][2])
        while i // 2 >= 0 and self.container[i][2] < self.container[ i // 2][2]:
            #print('Inside')
            #print(self.container[i][2], self.container[ i // 2][2])
            self.container[i], self.container[ i // 2]  = self.container[i // 2], self.container[i]
            i //= 2
    
    def is_leaf(self, i):
        if 2 * i >= self.size:
            return True
        else:
            return False
      
    def heapify_down(self, i):
        left_kid, right_kid = None
        if 2 * i < self.size:
            left_kid = self.container[2 * i]
            if 2 * i + 1 < self.size:
                right_kid = self.container[2 * i + 1]
        else:
            return
        
        while i < self.size and ((left_kid and self.container[i][2] > left_kid[2]) or (right_kid and self.container[i][2] > right_kid[2])):
            if ((left_kid and self.container[i][2] > left_kid[2]) and (right_kid and self.container[i][2] > right_kid[2])):
                if left_kid[2] <= right_kid[2]:
                    self.container[i], left_kid = left_kid, self.container[i]
                    i = 2 * i
                else:
                    self.container[i], right_kid = right_kid, self.container[i]
                    i = 2 * i + 1
            elif (left_kid and self.container[i][2] > left_kid[2]):
                self.container[i], left_kid = left_kid, self.container[i]
                i = 2 * i
            else:
                self.container[i], right_kid = right_kid, self.container[i]
                i = 2 * i + 1
                
            left_kid, right_kid = None
            if 2 * i < self.size:
                left_kid = self.container[2 * i]
                if 2 * i + 1 < self.size:
                    right_kid = self.container[2 * i + 1]
            else:
                return
                
    def insert(self, data):
        self.container.append(data)
        self.heapify_up(self.size)
        self.size += 1
    
    def delete_min(self):
        self.container[0] = self.container[self.size - 1]
        self.size -= 1
        self.heapify_down(0)
        
            
            
def print_arrays(arrays):
    for array in arrays:
        print(array)

def mergeArrays(arr):
    k = len(arr)
    if k in [0, 1]:
        return arr
    result = []
    #print_arrays(arr)
    pointers = [0] * k
    heads = [None] * k
    
    heap = MinHeap()
    for i in range(k):
        heap.insert((i, 0, arr[i][0]))
    print(heap.container)
    
    print(heap.is_leaf(0))
    print(heap.is_leaf(1))
    print(heap.is_leaf(2))
    #heap.delete_min()
    #print(heap.container)
    
    
    for i in range(k):
        heads[i] = arr[i][0]
    
    #print(heads) 
    empty = [None] * k
    j = 0
    out = False
    while not out:
        if heads == [None] * k:
            out = True
        #print('While')
        #print('Heads %s', heads)
        #print('Pointers %s', pointers)
        for i in range(k):
            if heads[i]:
                min_item = heads[i]
        for i in range(k):
            if heads[i] == None:
                pass
            elif heads[i] <= min_item:
                min_item = heads[i]
        #print('min %s', min_item)
        for i in range(k):
            if heads[i] == None:
                pass
            elif heads[i] <= min_item:
                min_item = heads[i]
                pointers[i] += 1
                try:
                    heads[i] = arr[i][pointers[i]]
                except IndexError:
                    heads[i] = None
                result.append(min_item)
                break
        #j += 1
    #print('End of while')
    
    #print(pointers)
    #print(heads)
    #print(min_item)
    return result
    
    
    

