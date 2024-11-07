class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self) -> str:
        values = []
        current_node = self.head
        while current_node :
            values.append(current_node.value)
            current_node = current_node.next
        return f"{' -> '.join(str(value) for value in values)}"
    
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None :
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def insert(self, position, values):
        if position < 0:
            position = self.length - abs(position) 
        if 0 <= position < self.length :
            if position == 0:
                self.prepend(values)
            elif position == self.length:
                self.append(values)
            else:
                new_node = Node(values)
                current_node = self.head
                for _ in range(position-1):
                    current_node = current_node.next
                new_node.next = current_node.next
                current_node.next = new_node  
                self.length += 1
        else:
            print("Invalid position")

    def get(self, index):
        if index < 0 :
            index = self.length - abs(index)
        if 0 > index or index >= self.length:
            return "Invalid Index"
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node
    
    def set_value(self, index, value):
        position = index
        if index < 0 :
            index = self.length - abs(index)
        if 0 > index or index >= self.length:
            return "Invalid Index"
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        current_node.value = value
        return f"the value at index  {position} is updated to {current_node.value}"

    
    def find(self, value):
        pointer = 0
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return f"The Value '{value}' found at position {pointer}"
                break
            current_node = current_node.next
            pointer += 1
        return f"The Value '{value}' not found"
        
    def pop_first(self):
        popped_node = self.head
        if self.head is None:
            return "Empty List"
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node.value
    
    def pop(self):
        if self.head is None:
            return "Empty List"
        current_node = self.head
        if current_node.next is None:
            self.head = None
            self.tail = None
            self.length -= 1
            return current_node.value
        while current_node.next.next:
            current_node = current_node.next
        poped_node = current_node.next
        current_node.next = None
        self.tail = current_node
        self.length -= 1
        return poped_node.value

    def remove(self, index):
        if index < 0:
            index = self.length - abs(index)
        if index < 0 or index >= self.length:
            return "Invalid Index"
        else:
            if index == 0:
                return self.pop_first()
            elif index == self.length - 1:
                return self.pop()
            else:
                prev_node = self.get(index - 1)
                popped_node = prev_node.next
                prev_node.next = popped_node.next
                popped_node.next = None
                self.length -= 1
                return popped_node
            
    def delete_all(self):
        if self.head :
            self.head = None
            self.tail = None
        else :
            return None
        
    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head
    
    def mid(self):
        if self.head is None :
            return "Emoty linked list"
        slow = self.head
        fast = self.head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        return slow

    def remove_dublicates(self):
        if self.length == 0 :
            return None
        my_set  = set()
        current_node = self.head
        my_set.add(current_node.value)
        while current_node.next :
            if current_node.next.value in my_set :
                current_node.next = current_node.next.next
                self.length -= 1
            else :
                my_set.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)   
linked_list.append(3)   
linked_list.append(4)   
linked_list.append(5)   
linked_list.append(6)                     
print(f" {linked_list} \n Head :{linked_list.head.value}  Tail : {linked_list.tail.value} Length: {linked_list.length}" )
print(f" {linked_list} \n Head :{linked_list.head.value}  Tail : {linked_list.tail.value} Length: {linked_list.length}" )

