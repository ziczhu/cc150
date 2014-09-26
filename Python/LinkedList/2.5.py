def addLists(listOne, listTwo, carry):
    first = listOne.head
    second = listTwo.head
    if not first and not second and not carry:
        return None

    result = linkedList()

    value = carry
    if first and first.data:
        value += first.data
    if second and second.data:
        value += second.data

    result.head = Node(value % 10)

    nextFirst = linkedList()
    nextSecond = linkedList()

    nextFirst.head = first.next if first else None
    nextSecond.head = second.next if second else None
    newCarry = value // 10

    more = addLists(nextFirst, nextSecond, newCarry)
    if more:
        result.head.setNext(more.head)

    return result