
class DynamicArray:
    def __init__(self, capacity=8):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.count = 0

    def append(self, value):
        if self.count >= self.capacity:
            self.resize()

        self.storage[self.count] = value
        self.count += 1

    def insert(self, index, value):
        if self.count >= self.capacity:
            self.resize()

        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]

        self.storage[index] = value
        self.count += 1
        return value

    def resize(self):
        # double our capacity
        self.capacity = self.capacity * 2

        # make a new array that new size
        new_array = [None] * self.capacity

        # copy everything from the old array
        for idx in range(self.count):
            new_array[idx] = self.storage[idx]

        # use this new array as our storage
        self.storage = new_array
