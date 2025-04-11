from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def list_stack(self):
        print(self.stack)

    def add(self, value):
        self.stack.append(value)

    def remove(self):
        self.stack.pop()
    


class Queues:
    def __init__(self):
        self.queue = deque()

    def list_queue(self):
        print(self.queue)

    def add(self, value):
        self.queue.append(value)

    def decrease_queue(self):
        self.queue.popleft()





