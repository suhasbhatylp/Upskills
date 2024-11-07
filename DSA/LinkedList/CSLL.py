class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    # def __init(self, val):
    #     new_node = Node(val)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length  = 1

    def __str__(self):
        lst  = []
        temp_node = self.head
        while temp_node:
            lst.append(str(temp_node.value))
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        return "->".join(lst)

    def append(self, val):
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else :
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self.length += 1

    def prepend(self, val):
        new_node = Node(val)
        if self.head is None :
            self.head = new_node
            self.tail = new_node
            self.tail.next = new_node
        else :
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
        self.length += 1

    def insert(self, index, val):
        if index > self.length or index < 0 :
            return "Invalid Index"
        new_node = Node(val)
        if index > self.length :
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        elif index == 0 :
            if self.head is None :
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        else :
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
    
    def traversal(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
            if current_node == self.head :
                break
    
    def search(self, val):
        current_node = self.head
        for i in range(self.length):
            if current_node.value == val :
                return f'the value {val} is presented at the index of {i}'
            current_node = current_node.next
        return f"the value {val} not present in the CSLL"
    
    def get(self, index):
        input_index = index
        current_node = self.head
        if abs(index) >= self.length :
            return "index is out of range"
        if index < 0 :
            index = self.length + index
        for _ in range(index):
            current_node = current_node.next
        return current_node
    
    def set(self, index, value):
        if abs(index) >= self.length :
            return "index is out of range"
        if index < 0 :
            index += self.length
        temp_node = self.get(index)
        temp_node.value = value

    def pop_first(self):
        popped_node = self.head
        if self.head is None:
            return None
        if self.length == 1 :
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        poped_node = self.tail
        # temp_node = self.head
        if self.length == 0 :
            return None
        if self.length == 1 :
            self.head = None
            self.tail = None
        else :
            temp_node = self.get(-2)
            temp_node.next = self.head
            self.tail = temp_node
            poped_node.next = None
        self.length -= 1
        return poped_node
    
    def remove(self, val):
        removed_node = None
        curr_node = self.head
        if self.head is None :
            return None
        if self.length == 1 and self.head.value == val :
            self.head = None
            self.tail = None
            self.length -=1
            return True
        else :
            while curr_node and curr_node.next :
                if curr_node.next.value == val :
                    removed_node = curr_node.next
                    curr_node.next = curr_node.next.next
                    removed_node.next = None
                    if removed_node == self.tail:
                        self.tail = curr_node
                    elif removed_node == self.head :
                        self.head = curr_node.next
                    self.length -=1
                    return removed_node
                curr_node = curr_node.next
        if removed_node is None :
            return None

    def remove_index(self, index):
        prev_node = self.head
        if abs(index) >= self.length :
            return "index is out of range"
        if index < 0 :
            index += self.length
        if self.length ==0:
            return None
        if index == 0:
            removed_node = self.pop_first()
        elif  index ==  self.length - 1 :
            removed_node = self.pop()
        else :
            prev_node = self.get(index - 1)
            removed_node = prev_node.next
            prev_node.next = removed_node.next
            removed_node.next = None
            self.length -= 1
        return removed_node

    def delete_all(self):
        self.tail.next = None
        self.head = None
        self.tail = None
        self.lenght = 0
        




csll = CircularSinglyLinkedList()
csll.prepend(4)
csll.append(5)
csll.prepend(10)
csll.append(3)
csll.insert(2,1)
print(csll)
print(csll.head.value, csll.tail.value, csll.length)
csll.remove(10)
print(csll)
print(csll.head.value, csll.tail.value, csll.length)