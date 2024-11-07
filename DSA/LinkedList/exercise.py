from random import randint

class Node:
    def __init__(self, value = None) -> None:
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return str(self.value)

class CDSL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self) :
        currentNode = self.head
        while currentNode :
            yield currentNode
            currentNode = currentNode.next

    def __str__(self) -> str:
        values = [ str(node.value) for node in self]
        return ' <-> '.join(values)
    
    def __len__(self):
        len = 0 
        currentNode = self.head
        while currentNode :
            len += 1
            currentNode = currentNode.next
        return len
    
    def add(self, value):
        node = Node(value)
        if self.head is None :
            self.head = node
            self.tail = node
        else :
            node.prev = self.tail   
            self.tail.next = node
            self.tail = node

    
    def generate(self, n, minValue, maxValue):
        self.head = self.tail = None
        for i in range(n):
            self.add(randint(minValue, maxValue))


cdll = CDSL()
cdll.generate(10, 2, 10)
print(cdll)
print(len(cdll))