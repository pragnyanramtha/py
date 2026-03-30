class Queue: 
    def __init__(self): 
        self.queue = [] 
 
    # ENQUEUE operation 
    def enqueue(self, data): 
        self.queue.append(data) 
        print(f"Enqueued: {data}") 
 
    # DEQUEUE operation 
    def dequeue(self): 
        if not self.queue: 
            print("Queue Underflow") 
            return 
        removed = self.queue.pop(0) 
        print(f"Dequeued: {removed}") 
 
    # FRONT element 
    def front(self): 
        if not self.queue: 
            print("Queue is Empty") 
            return 
        print(f"Front element: {self.queue[0]}")

    # DISPLAY queue 
    def display(self): 
        if not self.queue: 
            print("Queue is Empty") 
 
            return 
        print("Queue (Front → Rear): ", end="") 
        for item in self.queue: 
            print(item, end="  ") 
        print() 
 
 
# Main Program 
q = Queue() 
q.enqueue(10) 
q.enqueue(20) 
q.enqueue(30) 
q.display() 
 
q.dequeue() 
q.front() 
q.display() 
 
 
