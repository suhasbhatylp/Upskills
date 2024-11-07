class Queue :
    def __init__(self, maxSize) -> None:
        self.maxSize = maxSize
        self.items = [None] * maxSize
        self.start = -1
        self.top = -1



    def __str__(self) -> str:
        values = [ str(items) for items in self.items if items is not None]
        return ' '.join(values)
    
    def isFull(self):
        if self.top +1 == self.start :
            return True
        elif self.start == 0 and self.top+1 == self.maxSize :
            return True
        else :
            return False
        
    def isEmpty(self):
        if self.top == -1 :
            return True
        else :
            return False
        
    def enQueue(self, value):
        if self.isFull():
            return "Queue is already Full!"
        else :
            if self.top + 1 == self.maxSize :
                self.top == 0
            else :
                self.top += 1
                if self.start == -1 :
                    self.start = 0
            self.items[self.top] = value

    def deQueue(self):
        if self.isEmpty() :
            return "Queue is empty "
        else :
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top :
                self.start = -1
                self.top = -1
            elif self.start +1 == self.maxSize :
                self.start = 0
            else :
                self.start += 1
            self.items[start] = None
            return firstElement
        
    def peek(self):
        if self.isEmpty() :
            return " Queue is empty"
        else :
            return self.items[self.start]
        
    def delete(self):
        self.items = self.maxSize * [None]
        self.start = -1
        self.top = -1


queue = Queue(6)
queue.enQueue(5)
queue.enQueue(3)
queue.enQueue(2)
queue.enQueue(1)
print(queue)
print('----------')
print(queue.deQueue())
print('----------')
print(queue.deQueue())
print('----------')
print(queue)
print('----------')
print(queue.peek())
print('----------')


    
