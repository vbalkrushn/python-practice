class DynamicArray:
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = [None] * self.capacity

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if not 0 <= index < self.n:
            return IndexError("Item out of bounds!")
        return self.A[index]

    def get(self, index):
        return self.__getitem__(index)

    def _resize(self, new_cap):
        B = [None] * new_cap
        for k in range(self.n):
            B[k] = self.A[k]
        self.capacity = new_cap
        self.A = B

    def append(self, element):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        self.A[self.n] = element
        self.n += 1

    def remove(self, element):
        C = [None] * self.capacity
        for k in range(self.n):
            if element != self.A[k]:
                C = self.A[k]
            else:
                self.n -= 1
        self.A = C


if __name__ == '__main__':
    my_array = DynamicArray()
    my_array.append(21)
    my_array.append(7)
    my_array.append(20)
    my_array.append(4)

    print(my_array.get(2))

    my_array.remove(5)

    print(my_array.__len__())