class Node:
    def __init__(self, value = None, next = None) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __iter__(self):
        currentNode = self.head
        while currentNode :
            yield currentNode
            currentNode = currentNode.next



class Stack :
    def __init__(self) -> None:
        self.linkedList = LinkedList()

    def __str__(self):
        values = [ str(x.value) for x in self.linkedList]
        return '\n'.join(values)

    
    def isEmpty(self) :
        if self.linkedList.head :
            return False
        else :
            return True
    
    def push(self, value) :
        node = Node(value)
        node.next = self.linkedList.head
        self.linkedList.head = node
    
    def pop(self):
        if self.isEmpty():
            return None
        else :
            nodeValue = self.linkedList.head.value
            self.linkedList.head = self.linkedList.head.next
            return nodeValue
        
    def peek(self):
        if self.isEmpty():
            return None
        else :
           return (self.linkedList.head.value)
  
    def delete(self):
        self.linkedList.head = None



stack = Stack()
print(stack.isEmpty())
print('--------')
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)
print(stack)
print('--------')
print(stack.pop())
print('--------')
print(stack)
