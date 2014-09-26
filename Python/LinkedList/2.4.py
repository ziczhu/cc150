def partition(ls, x):
    before = linkedList()
    beforeStart = before.head
    after = linkedList()
    afterStart = after.head
    curr = ls.head

    while curr:
        nextNode = curr.next
        val = curr.getData()
        if val < x:
            curr.setNext(beforeStart)
            beforeStart = curr
        else:
            curr.setNext(afterStart)
            afterStart = curr
        curr = nextNode

    if not beforeStart:
        return after

    newList = linkedList()
    newList.head = beforeStart
    while beforeStart.next:
        beforeStart = beforeStart.next
    beforeStart.setNext(afterStart)

    return newList