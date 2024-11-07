class Stack :
    def __init__(self, maxSize) -> None:
        self.list = list()
        self.maxSize = maxSize
    
    def __str__(self) :
        values = [str(x) for x in self.list[::-1]]
        return "\n".join(values)
    
    def isEmpty(self):
        if self.list == [] :
            return True
        else :
            return False
    def isFull(self):
        if len(self.list) == self.maxSize :
            return True
        else :
            return False
    
    def push(self, value):
        if self.isFull() :
            return "Stack is already full"
        else :
            self.list.append(value)
            return f'The value : {value} is inserted..'
        
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


my_stack = Stack(3)
print(my_stack.isEmpty())
print(my_stack.push(6))
print(my_stack.push(5))
print(my_stack.push(4))
print(my_stack.isFull())