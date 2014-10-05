class StackWithMin:

    def __init__(self):
        self.values = []
        self.minValues = []

    def isEmpty(self):
        return self.values == []

    def push(self, value):
        if self.isEmpty() or value <= self.min():
            self.minValues.append(value)
        self.values.append(value)

    def pop(self):
        try:
            value = self.values.pop()
            if value == self.min():
                self.minValues.pop()
        except IndexError:
            value = None
        return value

    def peek(self):
        try:
            value = self.values[-1]
        except IndexError:
            value = None
        return value

    def size(self):
        return len(self.values)

    def min(self):
        try:
            minValue = self.minValues[-1]
        except IndexError:
            minValue = None
        return minValue
