def sortStack(stack):
    sortedStack = []
    while stack:
        s = stack.pop()
        while sortedStack and s < sortedStack[-1]:
            stack.append(sortedStack.pop())
        sortedStack.append(s)
    return sortedStack