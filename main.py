class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 
 
class LinkedList: 
    def __init__(self): 
        self.head = None 
 
    # Insert at beginning 
    def insert_begin(self, data): 
        new_node = Node(data) 
        new_node.next = self.head 
        self.head = new_node 
 
    # Insert at end 
    def insert_end(self, data): 
        new_node = Node(data) 
        if self.head is None: 
            self.head = new_node 
            return 
        temp = self.head 
        while temp.next: 
            temp = temp.next 
        temp.next = new_node 
 
    # Insert at position (1-based index) 
    def insert_position(self, data, pos): 
        new_node = Node(data) 
        if pos == 1: 
            self.insert_begin(data) 
            return 
        temp = self.head 
        for _ in range(pos - 2): 
            if temp is None: 
                print("Position out of range") 
                return 
            temp = temp.next 
        new_node.next = temp.next 
        temp.next = new_node 
 
    # Delete a node 
    def delete_node(self, key): 
        temp = self.head 
 
        # If head is the node to delete 
        if temp is not None and temp.data == key: 
            self.head = temp.next 
            return
        
        prev = None 
        while temp is not None and temp.data != key: 
            prev = temp 
            temp = temp.next 
 
 
        if temp is None: 
            print("Node not found") 
            return 
 
        prev.next = temp.next 
 
    # Display the list 
    def display(self): 
        temp = self.head 
        while temp: 
            print(temp.data, end=" → ") 
            temp = temp.next 
        print("NULL") 
 
 
# Main Program 
ll = LinkedList() 
ll.insert_begin(30) 
ll.insert_end(40) 
ll.insert_position(35, 2) 
ll.display() 
 
ll.delete_node(35) 
ll.display() 
