# Re-using code from practice Jupyter Notebooks
class DoubleNode:

    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node):
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def get_head_key(self):
        return self.head.key

    def get_tail_key(self):
        return self.tail.key

    def move_recent_to_front(self, node):
        if node.key == self.head.key:
            return
        if node.next is None:
            node.prev.next = None
            self.tail = node.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head
            self.head.prev = node
            node.prev = None
            self.head = node

    def remove_tail(self):
        node = self.tail
        self.tail = node.prev
        self.tail.next = None
        node.next = None
        node.prev = None


class LRU_Cache(object):

    def __init__(self, capacity):

        self.capacity = capacity
        self.rate_of_usage = DoublyLinkedList()
        self.cache = dict()

    def get(self, key):
        node = self.cache.get(key)

        if node is None:

            return "NOT PRESENT!!!"

        self.rate_of_usage.move_recent_to_front(node)
        return node.value

    def set(self, key, value):
        if self.capacity == 0:
            print("Cache capacity is zero, cannot add new elements!")
            return
        node = self.cache.get(key)

        if node:
            node.value = value
            self.rate_of_usage.move_recent_to_front(node)
            return

        if len(self.cache) == self.capacity:
            tail_key = self.rate_of_usage.get_tail_key()
            self.rate_of_usage.remove_tail()
            del self.cache[tail_key]
        new_node = DoubleNode(key, value)
        self.cache[key] = new_node
        self.rate_of_usage.insert_node(new_node)


print("========== TEST 1 ==========")

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns NOT PRESENT!!! because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))  # returns NOT PRESENT!!! because the cache reached it's capacity and 3 was the least
# recently used entry

print("========== TEST 2 ==========")

test_cache = LRU_Cache(3)

test_cache.set(1, 1)
test_cache.set(2, 2)
test_cache.set(3, 3)

print(test_cache.get(1))  
print(test_cache.get(2))
print(test_cache.get(9))  


print(test_cache.get(3))  


print("========== TEST 3 ==========")
test_2_cache = LRU_Cache(0)
test_2_cache.set(1, 1)
