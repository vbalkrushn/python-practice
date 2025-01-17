class Stack:
    def __init__(self):
        self.elements = []

    def push(self, value):
        self.elements.append(value)

    def __len__(self):
        return len(self.elements)

    def is_empty(self):
        return len(self.elements) == 0

    def pop(self):
        if not self.is_empty():
            return self.elements.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.elements[-1]
        raise IndexError("peek from empty stack")


if __name__ == '__main__':
    stack = Stack()

    stack.push(21)
    stack.push(7)
    stack.push(20)

    # | 20 |
    # | 7 |
    # | 21 |

    print(stack.peek())
    print(len(stack))
    print(stack.pop())
    print(len(stack))
    print(stack.elements)
