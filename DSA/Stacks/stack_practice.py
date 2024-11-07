# creation of the stack

# 1) Using is List
# 2) Using Linked List

# Using size limit

class Stack :
    def __init__(self) -> None:
        self.list = []

    def __str__(self) :
        values = [str(x) for x in self.list[::-1]]
        return "\n".join(values)
    
    def isEmpty(self):
        if self.list == [] :
            return True
        else : 
            return False
        
    def push(self, value):
        self
        self.list.append(value)
    
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.list[-1]
    
    def delete(self):
        self.list = None


myStack = Stack()
myStack.push(4)
myStack.push(5)
myStack.push(6)
myStack.push(7)
# print(myStack.isEmpty())
# print(myStack)
print(myStack,'\n')
print(myStack.pop(), ' popped')
print('after')
print(myStack,'\n')
print(myStack.peek())
myStack.delete()
print(myStack,'\n')