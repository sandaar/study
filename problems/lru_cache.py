class LinkedListNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

class LinkedList(object):
    def __init__(self):
        self.head = self.tail = None
        
    def initiate(self, key, value):
        node = LinkedListNode(key, value)
        self.head = self.tail = node
        return node
        
    def append(self, key, value):
        node = LinkedListNode(key, value)
        self.tail.next = node
        self.tail = node
        return node

    def promote(self, node):
        if self.head == self.tail or node == self.tail:
            pass
        if node.previous and node.next:
            node.previous.next = node.next
            node.next.previous = node.previous
            self.tail.next = node
            self.tail = node
        elif node == self.head:
            self.head.next.previous = None
            self.head = self.head.next

    def delete_head(self):
        self.head = head.next
        head.previous = None
        
        
            
class Cache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.container = dict()
        self.linked_list = LinkedList()

    def size(self):
        return len(self.container)
        
    def evict():
        self.linked_list.delete_head()
        self.container.pop(node.key)
        
    def set(self, key, value):
        if self.size == self.capacity:
            self.evict()
        if self.size == 0:
            node = self.linked_list.initiate(key, value)
            self.container[key] = node
        elif not self.container.get(key, None):
            node = self.linked_list.append(key, value)
            self.container[key] = node
        else:
            node = self.container[key]
            node.value = value
            self.linked_list.promote(node)
            
    def get(self, key):
        node = self.container.get(key, None)
        if node:
            return node.value
        else:
            return -1
        
    
    
        
def implement_LRU_cache(capacity, query_type, key, value):
    n = len(query_type)
    cache = Cache(capacity)
    
    for i in range(n):
         if query_type[i] == 1:
             cache.set(key[i], value[i])
            
    print(cache.container)
    result = [ cache.get(key[i]) for i in range(n) if query_type[i] == 0]
    #result = None
    return result

