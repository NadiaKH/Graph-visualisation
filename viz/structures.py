class Stack:
    def __init__(self, size):
        self.index = 0
        self.storage = [None for x in range(size)]
        self.size = size

    def push(self, element):
        if self.index < self.size:
            self.storage[self.index] = element
            self.index += 1

    def pop(self):

        if self.index == 0:
            return None

        self.index -= 1
        return self.storage[self.index]

    def top(self):
        if self.index == 0:
            return None
        return self.storage[self.index - 1]

    def empty(self):
        return self.index == 0


class List:
    def __init__(self, size):
        self.storage = [None for i in range(size)]
        self.size = size
        self.index = 0

    def add(self, element):
        if self.index < self.size:
            self.storage[self.index] = element
            self.index += 1

    def __getitem__(self, index):
        if index < self.size:
            return self.storage[index]
        return None


class pushOrder:

    def __init__(self, size):
        self.order = List(size)
        self.stack = Stack(size)
        self.size = size

    def push(self, element):
        self.order.add(element)
        self.stack.push()

    def pop(self, element):
        return self.stack.pop()

    def size(self):
        return self.stack.size()

    def getOrder(self):
        return self.order

    def empty(self):
        return self.stack.empty()