
class DynamicArray:
    def __init__(self, capacity=8):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.count = 0

    def append(self, value):
        if self.count >= self.capacity:
            # TODO go and resize
            print("ERROR: already full")
            return value

        self.storage[self.count] = value
        self.count += 1

    def insert(self, index, value):
        if self.count >= self.capacity:
            # TODO go and resize
            print("ERROR: already full")
            return value

        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]
        self.storage[index] = value
        self.count += 1
        return value

    def resize(self):
        pass
