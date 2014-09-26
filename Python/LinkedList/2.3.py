def deleteNode(node):
    if not node or not node.next:
        return False
    nextNode = node.next
    node.setData(nextNode.getData())
    node.next = nextNode.next
    return True