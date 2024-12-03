# A cache is a set of keys and values that is used to store the values of previous computations

# Functional requirements:
# 1. The cache should be able to store a value given a key
# 2. The cache should be able to read, delete, and update a value given a key
# 3. The cache should be able to evict a value given a key
# 4. The cache should be able to evict the least recently used value
# 5. The cache should be able to evict the least frequently used value

class Node:
    def __init__(self, key,value):
        # Initialize node with key-value pair and null pointers
        self.key = key
        self.value = value
        self.next = None  # Points to next node in doubly linked list
        self.prev = None  # Points to previous node in doubly linked list


class LRUCache:
    def __init__(self, capacity: int):
        # Initialize cache with given capacity
        self.capacity = capacity
        self.cache = {}  # HashMap to store key-node pairs

        # Create dummy head and tail nodes
        self.head = Node(0,0)  # Dummy head node
        self.tail = Node(0,0)  # Dummy tail node
        self.head.next = self.tail  # Link head to tail
        self.tail.prev = self.head  # Link tail to head

    def remove(self, node):
        # Remove node from doubly linked list
        prev, nxt = node.prev, node.next
        prev.next = nxt  # Skip over node being removed
        nxt.prev = prev  # Link back to previous node

    def add_front(self, node):
        # Add node to front of list (most recently used)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node  # Link existing front node back
        self.head.next = node  # Set new node as front

    def get(self, key):
        # Get value for key and mark as recently used
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)  # Remove from current position
            self.add_front(node)  # Move to front (most recently used)
            return node.value
        return -1  # Key not found

    def put(self, key, value):
        # Add or update key-value pair
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.add_front(node)
        else:
            # Add new key
            if len(self.cache) == self.capacity:
                # Remove least recently used item
                lru = self.tail.prev  # Get LRU node
                self.remove(lru)  # Remove from linked list
                del self.cache[lru.key]  # Remove from hash map

            # Add new node
            node = Node(key, value)
            self.cache[key] = value
            self.add_front(node)
