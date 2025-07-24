class HashTable:
    # Constructor
    def __init__(self, capacity=10):
        # Define how many "buckets" we can have in the table
        self.capacity = capacity
        # Creates an empty list based on the capacity
        self.table = [[] for _ in range(capacity)]

    # This is a private method that computes the hash for any key
    def _hash(self, key):
        # Returns large number and computes where to map it in table
        return hash(key) % self.capacity
    
    def put(self, key, value):
        index = self._hash(key)
        # This is a check to see if the exists and to update it.
        # looking through the bucket at the index
        # If the key already exists, update it to pair[1] to avoid duplication
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        
        # Otherwise, add a new key-value pair
        self.table[index].append([key, value])
    
    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        # If the key is not found
        return None 
    
    def remove(self, key):
        index = self._hash(key)
        # Gets both the index and value
        # Matches, to then remove the item using del
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        # If the key is not found
        return False
    
    def keys(self):
        keys_List = []
        for bucket in self.table:
            for pair in bucket:
                keys_List.append(pair[0])
        return keys_List
    
    def __str__(self):
        return str(self.table)
    
myHash = HashTable()
myHash.put("name", "Alice")
myHash.put("age", 30)
myHash.put("city", "New York")
print(myHash.keys())