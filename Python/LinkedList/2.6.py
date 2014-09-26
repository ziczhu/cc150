def findBeginning(ls):
    slow = ls.head
    fast = ls.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.next:
        return None

    slow = ls.head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast