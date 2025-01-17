class HashTable:
    def __init__(self, size=101):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, val):
        idx = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, val)
                return
        self.table[idx].append((key, val))

    def find(self, key):
        idx = self.hash_function(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None


if __name__ == "__main__":
    hashtable = HashTable()
    hashtable.insert('test', 21)
    hashtable.insert('test', 20)
    # hashtable.insert(2, 7)
    # hashtable.insert(3, 20)

    print(hashtable.find('test'))
    print(hashtable.find(1))
