class Stack: 
    def __init__(self): 
        self.stack = [] 
 
    # PUSH operation 
    def push(self, data): 
        self.stack.append(data) 
        print(f"Pushed: {data}") 
 
    # POP operation 
    def pop(self): 
        if not self.stack: 
            print("Stack Underflow") 
            return 
        removed = self.stack.pop() 
        print(f"Popped: {removed}") 
 
    # PEEK operation 
    def peek(self): 
        if not self.stack: 
            print("Stack is Empty") 
            return 
        print(f"Top element: {self.stack[-1]}")
    # DISPLAY stack 
    def display(self): 
        if not self.stack: 
            print("Stack is Empty") 
            return 
        print("Stack (Top → Bottom): ", end="") 
        for item in reversed(self.stack): 
            print(item, end="  ") 
        print() 
 
 
# Main Program 
s = Stack() 
s.push(10) 
s.push(20) 
s.push(30) 
s.display() 
 
s.pop() 
s.peek() 
s.display()
