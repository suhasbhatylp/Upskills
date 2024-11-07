class Node:
    def __init__(self, value, next = None, prev = None) -> None:
        self.value = value
        self.next = next
        self.prev = prev

class CircularDoublyLinkedList :
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        currentNode = self.head
        while currentNode :
            yield currentNode
            currentNode = currentNode.next
            if currentNode == self.head :
                break
    def __str__(self):
        result = ''
        currentNode = self.head
        while currentNode :
            result += str(currentNode.value)
            if currentNode.next == self.head :
                break
            else :
                result += ' <-> '
                currentNode = currentNode.next
        return result

    ''' Creation of circular singly linked list '''
    def createCDLL(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.prev = node
        node.next = node
        return 'Circular Doubly Linked List is created'
    
    def insert(self, value, index):
        if self.head is None :
            return None
        else :
            node = Node(value)
            if index == 0 :
                    node.next = self.head
                    node.prev = self.tail 
                    self.head.prev = node
                    self.head = node
                    self.tail.next = node
            elif index == -1 :
                node.next = self.head 
                node.prev = self.tail
                self.tail.next = node
                self.head.prev = node
                self.tail = node
            else :
                currentNode = self.head
                for _ in range(index -1):
                    currentNode = currentNode.next
                node.prev = currentNode
                node.next = currentNode.next
                currentNode.next.prev = node
                currentNode.next = node
    
    def traverse(self) :
        currentNode = self.head
        if currentNode is None :
            print( " Circular linked list is empty")
        else :
            while currentNode :
                print( currentNode.value)
                currentNode = currentNode.next
                if currentNode == self.head :
                    break

    def reverseTraverse(self):
        if self.head is None :
            return None
        else :
            currentNode = self.tail
            while currentNode :
                print(currentNode.value)
                currentNode = currentNode.prev
                if currentNode == self.tail :
                    break
    
    def findNode(self, value):
        if self.head is None :
            return None
        else :
            index = 0
            currentNode = self.head
            while currentNode :
                if currentNode.value == value :
                    return f'The value : {value} is at the location of {index} in CDLL'
                index +=1
                currentNode = currentNode.next
                if currentNode == self.head:
                    return f'The value : {value} is not present in the CDLL'
                
    def delete(self, index):
        if self.head is None :
            return None
        else :
            if index == 0 :
                if self.head == self.head.next :
                    self.head = None
                    self.tail = None
                else :
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head                
            elif index == -1 :
                if self.head == self.head.next :
                    self.head = None
                    self.tail = None
                else :
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else :
                currentNode = self.head 
                for _ in range(index -1):
                    currentNode = currentNode.next
                currentNode.next = currentNode.next.next
                currentNode.next.prev = currentNode

    def deleteDLL(self):
        self.head.next = self.head.prev = None
        self.head =   None






                


cdll = CircularDoublyLinkedList()
cdll.createCDLL(4)
# cdll.insert(0,0 )
# cdll.insert(1,1 )
# cdll.insert(2,2)
# cdll.insert(3,3)
# cdll.insert(5, -1)

print(cdll)

cdll.deleteDLL()
print(cdll)
# print(cdll.findNode(10))
# cdll.traverse()
# cdll.reverseTraverse()
print([ node.value for node in cdll ])
        