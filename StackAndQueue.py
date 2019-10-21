class Stack():
    def __init__(self):
        self._stack = []

    def push(self, element):
        self._stack.append(element)
        return self._stack

    def pop(self):
        return self._stack.pop()

    def peek(self):
        return self._stack[-1]

class Queue():
    def __init__(self):
        self._queue = []

    def enqueue(self, element):
        self._queue.append(element)
        return self._queue

    def dequeue(self):
        return self._queue.pop(0)

    def peek(self):
        return self._queue[0]
