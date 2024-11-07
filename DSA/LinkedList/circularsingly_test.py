class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class CircularSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node :
            yield node
            if node.next == self.head :
                break
            node = node.next
           