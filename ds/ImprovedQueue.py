class ImprovedQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def is_empty(self):
        return not self.in_stack and not self.out_stack

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)

    def enqueue(self, value):
        self.in_stack.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]


if __name__ == '__main__':
    queue = ImprovedQueue()
    queue.enqueue(7)
    queue.enqueue(20)
    queue.enqueue(21)

    print(len(queue))
    print(queue.front())
    print(len(queue))
    print(queue.dequeue())
    print(len(queue))
