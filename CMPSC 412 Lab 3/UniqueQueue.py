# Create a queue from stacks.

import Stack


class UniqueQueue:

    def __init__(self):
        self.stack1 = Stack.Stack()
        self.stack2 = Stack.Stack()

    # This will only need to keep track of 1 stack.
    def isEmpty(self):
        if self.stack1 == []:
            return True
        else:
            return False

    # This will return the size of the main stack.
    def size(self):
        return self.stack1.size()

    # This simply adds an element to the main stack
    # and functions like a normal queue data structure.
    def enqueue(self, inputData):
        self.stack1.push(inputData)

    # This makes use of the other stack and uses that to
    # relay the data of the main stack onto it. This allows
    # it to find the last element in the stack and pop it
    # allowing simulating a normal queue data structure.
    # The main stack then has the data put back into it.
    def dequeue(self):
        if self.stack1 == 0:
            return 0
        else:
            for i in range(self.stack1.size()):
                # Pushs the data from main stack to stack 2.
                self.stack2.push(self.stack1.pop())
        tempOutput = self.stack2.pop()
        for j in range(self.stack2.size()):
            # Pushs the data back to the main stack with
            # the queue operation now complete.
            self.stack1.push(self.stack2.pop())
        return tempOutput

    def __str__(self):
        return str(self.stack1.items)


uniqueQueue1 = UniqueQueue()
uniqueQueue1.enqueue(10)
uniqueQueue1.enqueue(100)
uniqueQueue1.enqueue(250)
uniqueQueue1.enqueue(140)
uniqueQueue1.enqueue(190)
print(uniqueQueue1)
uniqueQueue1.dequeue()
uniqueQueue1.dequeue()
uniqueQueue1.dequeue()
uniqueQueue1.dequeue()
print(uniqueQueue1)
