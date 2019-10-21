
class __HeapOperations():
    def __init__(self):
        self.heap = []

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _traverseDown(self, index, type):
        left = index*2+1
        right = index*2+2
        if type is 'max':
            largest = index
            if len(self.heap) > left and self.heap[largest] < self.heap[left]:
                largest = left
            if len(self.heap) > right and self.heap[largest] < self.heap[right]:
                largest = right
            if largest != index:
                self._swap(largest, index)
                self._traverseDown(largest, type)
        elif type is 'min':
            smallest = index
            if len(self.heap) > left and self.heap[smallest] > self.heap[left]:
                smallest = left
            if len(self.heap) > right and self.heap[smallest] > self.heap[right]:
                smallest = right
            if smallest != index:
                self._swap(smallest, index)
                self._traverseDown(smallest, type)


    def _traverseUp(self, index, type):
        if index == 0:
            pass
        else:
            parent = (index-1)//2
            if type is 'max':
                if self.heap[index] > self.heap[parent]:
                    self._swap(parent, index)
                    self._traverseUp(parent, type)
            elif type is 'min':
                if self.heap[index] < self.heap[parent]:
                    self._swap(parent, index)
                    self._traverseUp(parent, type)

class MaxHeap(__HeapOperations):
    def __init__(self, *elements):
        super().__init__()
        [self.push(elem) for elem in elements]
    def push(self, *elements):
        for element in elements:
            self.heap.append(element)
            index = len(self.heap)-1
            if not index:
                pass
            else:
                self._traverseUp(index, 'max')
        return self.heap

    def pop(self):
        if len(self.heap):
            self._swap(0, len(self.heap)-1)
            poppedElement = self.heap.pop()
            self._traverseDown(0, 'max')
            return poppedElement
        else:
            return None

    def peek(self):
        if self.heap:
            return self.heap #removee
        else:
            return "The heap is empty"

class MinHeap(__HeapOperations):
    def __init__(self, *elements):
        super().__init__()
        [self.push(elem) for elem in elements]

    def push(self, *elements):
        for element in elements:
            self.heap.append(element)
            index = len(self.heap)-1
            if not index:
                pass
            else:
                self._traverseUp(index, 'min')
        return self.heap

    def pop(self):
        if len(self.heap):
            self._swap(0, len(self.heap)-1)
            poppedElement = self.heap.pop()
            self._traverseDown(0, 'min')
            return poppedElement
        else:
            return None

    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return "The heap is empty."

