class Node:
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        tempNode = self.head
        while tempNode :
            yield tempNode
            tempNode = tempNode.next
    
    def __str__(self):
        result = ''
        temp_node = self.head
        while temp_node :
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node  :
                result += ' <--> '
        return result


    
    def createDLL(self, value) :
        node = Node(value)
        node.prev = None
        node.next = None
        self.head = self.tail = node
        return "Doubly linked list is created"
    
    def insert(self, value, index):
        node = Node(value)
        if index == 0 :
            if self.head:
                node.next = self.head
                self.head.prev = node
                self.head = node
            else :
                node.prev = None
                node.next = None
                self.head = self.tail = node
        elif index == -1 :
            if self.head :
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            else :
                node.prev = None
                node.next = None
                self.head = self.tail = node
        else :
            temp_node = self.head
            while (index - 1) :
                temp_node = temp_node.next
                index -= 1
            node.next = temp_node.next
            temp_node.next.prev = node
            temp_node.next = node
            node.prev = temp_node

    def traverse(self):
        if self.head:
            tempNode = self.head
            while tempNode :
                print(tempNode.value)
                tempNode = tempNode.next
        else :
            print("linked list is empty")

    def reverse(self):
        tempNode = self.head
        while tempNode:
            tempNode.prev, tempNode.next = tempNode.next, tempNode.prev
            tempNode = tempNode.prev
        self.head, self.tail = self.tail, self.head


    def reverse_traversal(self):
        if self.head :
            current_node  = self.tail
            while current_node :
                print(current_node.value)
                current_node = current_node.prev
        else :
            print('linked list is empty')

    def findNode(self, value):
        if self.head :            
            index = 0
            currentNode = self.head
            while currentNode :
                if currentNode.value == value :
                    return f'The value : {value} is located at index {index} .'
                currentNode = currentNode.next
                index += 1
            return f'The value : {value} is not present in the linked list .'
        else : 
            return ' The linked list is empty'
        
    def  delete(self, index):
        if self.head  is None :
            return 'Linked List is empty'
        else :
            if index == 0 :
                if self.head.next :
                    self.head = self.head.next
                    self.head.prev = None
                else :
                    self.head = self.tail = None
            elif index == -1 :
                if self.head.next :
                    self.tail = self.tail.prev
                    self.tail.next =  None
                else : 
                    self.head = self.tail = None
            else :
                currentNode = self.head
                for _ in range(index - 1):
                    currentNode = currentNode.next
                currentNode.next = currentNode.next.next
                currentNode.next.prev = currentNode

    def delDLL(self):
        self.head = None
        self.tail = None


dll = DoublyLinkedList()

print(dll.createDLL(3))
dll.insert(1, 0)
dll.insert(4, -1)
dll.insert(2, 1)

# dll.delDLL()

print(dll)
dll.delete(2)
print(dll)
dll.traverse()
print(dll)
dll.reverse()
print(dll)
dll.reverse_traversal()



# print(dll.findNode(1))
print([ node.value for node in dll])

     
