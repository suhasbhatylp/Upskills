class MultiStack:
    def __init__(self, stacksize) -> None:
        self.numberstacks = 3
        self.stacksize = stacksize
        self.custList = [0] * (self.stacksize * self.numberstacks)
        self.sizes = [0] * self.numberstacks

    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.stacksize :
            return True
        else :
            return False
        
    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0 :
            return True
        else :
            return False
        
    def indexTop(self, stacknum) :
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1
    
    def push(self, item, stacknum):
        if self.isFull(stacknum) :
            return 'The stack is already full'
        else :
            self.sizes[stacknum] += 1
            self.custList[self.indexTop(stacknum)] = item
    
    def pop(self, stacknum):
        if self.isEmpty(stacknum) :
            return 'The stack is empty'
        else:
            value = self.custList[self.indexTop(stacknum)]
            self.custList[self.indexTop(stacknum)] = 0
            return value
        
    def peek(self, stacknum):
        if self.isEmpty(stacknum) :
            return 'stack is empty'
        else :
            return self.custList[self.indexTop(stacknum)]

stack = MultiStack(6)
print(stack.custList,  stack.sizes)
print(stack.isFull(0))
print(stack.isEmpty(2))
stack.push(1,0)
stack.push(2,0)
stack.push(3,2)
print(stack.custList,  stack.sizes)
print(stack.peek(0))
        
        