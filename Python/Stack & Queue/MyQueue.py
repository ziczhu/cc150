class MyQueue:
    def __init__(self):
        self.stackNewest = []
        self.stackOldest = []

    def size(self):
        return len(self.stackNewest + self.stackOldest)

    def shiftStacks(self):
        if not self.stackOldest:
            while self.stackNewest:
                self.stackOldest.append(self.stackNewest.pop())

    def add(self, value):
        self.stackNewest.append(value)

    def peek(self):
        self.shiftStacks()
        return self.stackOldest[-1]

    def remove(self):
        self.shiftStacks()
        return self.stackOldest.pop()
