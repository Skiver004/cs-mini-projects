class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        # Check if key exists and update
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # Otherwise append
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"{i}: {bucket}")

# Test collisions
if __name__ == "__main__":
    ht = HashTable(5)
    ht.insert("apple", 1)
    ht.insert("banana", 2)
    ht.insert("grape", 3)
    ht.insert("peach", 4)  # may collide
    ht.insert("melon", 5)  # may collide
    ht.display()
