# Queue without limit using list
class Queue:
    def __init__(self) :
        self.queue = list()

    def __str__(self) -> str:
        values = [str(value) for value in self.queue]
        return ' '.join(values)

    def isEmpty(self):
        if self.queue == [] :
            return True
        else :
            return False
        
    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.isEmpty():
            return None
        else :
            return self.queue.pop(0)
        
    def peek(self):
        return self.queue[0]
    
    def delete(self):
        self.queue = []
    
my_queue = Queue()
print(my_queue.isEmpty())
print('-------------')
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4) 
my_queue.enqueue(5)

print(my_queue)
print('-------------')
print(my_queue.dequeue())
print('-------------')
print(my_queue.peek())


