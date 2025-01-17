class SimpleQueue:
    def __init__(self):
        self.elements = []

    def enqueue(self, value):
        self.elements.append(value)

    def is_empty(self):
        return len(self.elements) == 0

    def __len__(self):
        return len(self.elements)

    def dequeue(self):
        if not self.is_empty():
            return self.elements.pop(0)
        raise IndexError("dequeue from empty queue")

    def front(self):
        if not self.is_empty():
            return self.elements[0]
        raise IndexError("front from empty queue")


if __name__ == '__main__':
    queue = SimpleQueue()
    queue.enqueue(7)
    queue.enqueue(20)
    queue.enqueue(21)

    print(len(queue))
    print(queue.front())
    print(len(queue))
    print(queue.dequeue())
    print(len(queue))
