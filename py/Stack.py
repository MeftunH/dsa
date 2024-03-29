class Stack:
    def __init__(self):
        self.stack = []

    # Add an element
    def push(self, item):
        self.stack.append(item)

    # Remove an element
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    # Display the stack
    def display(self):
        return self.stack