from collections import deque


class Animal:
    order = None

    def __init__(self, name):
        self.name = name

    def setOrder(self, order):
        self.order = order

    def getOrder(self):
        return self.order

    def isOlderThan(self, animal):
        if isinstance(animal, Animal):
            return animal.getOrder() - self.getOrder()


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class AnimalQueue:
    dogs = deque()
    cats = deque()
    order = 0

    def enqueue(self, animal):

        if isinstance(animal, Dog):
            self.dogs.append(animal)
        elif isinstance(animal, Cat):
            self.cats.append(animal)
        animal.setOrder(self.order)
        self.order += 1

    def dequeueAny(self):

        if not self.dogs:
            self.dequeueCats()
        elif not self.cats:
            self.dequeueDogs()
        else:
            dog = self.dogs[0]
            cat = self.cats[0]
            if dog.isOlderThan(cat):
                return self.dogs.popleft()
            else:
                return self.cats.popleft()

    def dequeueDogs(self):
        return self.dogs.popleft()

    def dequeueCats(self):
        return self.cats.popleft()
