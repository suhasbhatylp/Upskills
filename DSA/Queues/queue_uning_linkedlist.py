class Node:
    def __init__(self, value = None,) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        currentNode = self.head 
        while currentNode :
            yield currentNode
            currentNode = currentNode.next

class Queue :
    def __init__(self) -> None:
        self.linkedList = LinkedList()

    def __str__(self) -> str:
        values = [ str(item.value) for item in self.linkedList]
        return ' '.join(values)
    
    def enQueue(self, value):
        node = Node(value)
        if self.linkedList.head is None :
            self.linkedList.head = node
            self.linkedList.tail = node
        else :
            self.linkedList.tail.next = node
            self.linkedList.tail = node
        
    def isEmpty(self):
        if self.linkedList.head is None :
            return True
        else :
            return False

    
    def deQueue(self):
        if self.isEmpty() :
            return "Queue is empty"
        else :
            tempNode = self.linkedList.head
            if self.linkedList == self.linkedList.tail :
                self.linkedList.head.head = None
                self.linkedList.tail = None
            else :
                self.linkedList.head = self.linkedList.head.next
            return tempNode.value
        
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else :
            return self.linkedList.head.value

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None


queue = Queue()
print(queue.isEmpty())
queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)
print(queue)
print(queue.peek())
print(queue.deQueue())
print(queue)
