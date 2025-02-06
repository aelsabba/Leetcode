class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1

        self.remove(self.cache[key])
        self.add(self.cache[key])

        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)

        newNode = Node(key, value)
        self.add(newNode)
        self.cache[key] = newNode

        if len(self.cache) > self.capacity:
            node_to_remove = self.head.next
            self.remove(node_to_remove)
            del self.cache[node_to_remove.key]

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        backup_node = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        node.prev = backup_node
        backup_node.next = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)