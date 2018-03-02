class Stack:
    def __init__(self):
        self.values = []
        self.top = -1
    
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def push(self, x):
        self.values.append(x)
        self.top += 1

    def pop(self):
        if self.is_empty():
            raise Exception('underflow')
        else:
            self.top -= 1
            return self.values[self.top+1]

if __name__ == "__main__":
    my_stack = Stack()
    print("Stack is empty is ", my_stack.is_empty())
    my_stack.push(1)
    print("Added 1 to stack. Popping stack. Value is ", my_stack.pop())
    print("Stack should be empty.  Popping should throw error")
    try:
        my_stack.pop()
    except Exception:
        print("Yay it threw an Exception!")
