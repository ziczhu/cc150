def nthToLast(alist, k):
    p1 = p2 = alist.head
    for i in range(k):
        if p2 == None:
            return None
        else:
            p2 = p2.next
    while p2:
        p1 = p1.next
        p2 = p2.next
    return p1