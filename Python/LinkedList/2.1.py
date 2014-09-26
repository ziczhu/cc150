class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def getNext(self):
        return self.next

    def setNext(self, nextNode):
        self.next = nextNode


class linkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        temp = Node(val)
        temp.setNext(self.head)
        self.head = temp

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def has(self, val):
        current = self.head
        found = False
        count = 0
        while current != None and not found:
            if current.getData() == val:
                found = True
            else:
                current = current.getNext()
                count += 1
        return found

    def remove(self, val):
        current = self.head
        pre = None
        found = False

        while not found:
            if current.getData() == val:
                found = True
            else:
                pre = current
                current = current.getNext()
            if pre == None:
                self.head = current.getNext()
            else:
                self.head = pre.setNext(current.getNext())

    def deleteDups(self):
        elems = {}
        current = self.head
        pre = None
        while current != None:
            key = current.getData()
            if key in elems:
                pre.next = current.next
            else:
                elems[key] = True
                pre = current
            current = current.next