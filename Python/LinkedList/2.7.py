def isParlindrome(ls):
    fast = ls.head
    slow = ls.head
    stack = []

    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        top = stack.pop()
        if slow.data != top:
            return False
        else:
            slow = slow.next
    return True