class Node:
    def __init__(self, value = 0, next = None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        string = str(self.value)
        if self.next :
            string += ' , ' + str(self.next)
        return string

class Stack :
    def __init__(self) -> None:
        self.top = None
        self.minNode = None

    def  min(self):
        if self.minNode is None :
            return None
        else :
            return self.minNode.value
    
    def push(self, item):
        if self.minNode and (self.minNode.value < item) :
            self.minNode = Node(value = self.minNode.value, next = self.minNode)
        else :
            self.minNode = Node(value = item, next= self.minNode)
        self.top = Node(value = item, next = self.top)

    def pop(self):
        if self.minNode is None :
            return None
        self.minNode = self.minNode.next
        item = self.top.value
        self.top = self.top.next
        return item

minStack = Stack()
minStack.push(10)
print(minStack.min(), '\n')
minStack.push(4)
print(minStack.min(), '\n')
minStack.push(6)
print(minStack.min(), '\n')
minStack.pop()
print(minStack.min(), '\n')
minStack.pop()
print(minStack.min(), '\n')
minStack.pop()
print(minStack.min(), '\n')
