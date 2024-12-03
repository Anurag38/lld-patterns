# A cache is a set of keys and values that is used to store the values of previous computations

# Functional requirements:
# 1. The cache should be able to store a value given a key
# 2. The cache should be able to read, delete, and update a value given a key
# 3. The cache should be able to evict a value given a key
# 4. The cache should be able to evict the least recently used value
# 5. The cache should be able to evict the least frequently used value

class Node:
    def __init__(self, key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):

        self.capacity = capacity
        self.cache = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def add_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add_front(node)
            return node.value
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.add_front(node)
        else:
            if len(self.cache) == self.capacity:
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]

            node = Node(key, value)
            self.cache[key] = value
            self.add_front(node)

