"""This handles all the common heap operations. This class should not be called from outside"""
class __HeapOperations():
    #This initializes the _heap variable to empty list"""
    def __init__(self):
        self._heap = []  #Used _heap coz this variable should not be used outside this class and derived classes

    #This method swaps the elements. Used when in need to swap parent and child
    def _swap(self, index1, index2):
        self._heap[index1], self._heap[index2] = self._heap[index2], self._heap[index1]

    #This method traverses down to rearrange the elements
    def _traverseDown(self, index, type):
        left = index*2+1
        right = index*2+2
        if type == 'max':
            largest = index
            if len(self._heap) > left and self._heap[largest] < self._heap[left]:
                largest = left
            if len(self._heap) > right and self._heap[largest] < self._heap[right]:
                largest = right
            if largest != index:
                self._swap(largest, index)
                self._traverseDown(largest, type)
        elif type == 'min':
            smallest = index
            if len(self._heap) > left and self._heap[smallest] > self._heap[left]:
                smallest = left
            if len(self._heap) > right and self._heap[smallest] > self._heap[right]:
                smallest = right
            if smallest != index:
                self._swap(smallest, index)
                self._traverseDown(smallest, type)

    # This method traverses up to rearrange the elements
    def _traverseUp(self, index, type):
        if index == 0:
            pass
        else:
            parent = (index-1)//2
            if type == 'max':
                if self._heap[index] > self._heap[parent]:
                    self._swap(parent, index)
                    self._traverseUp(parent, type)
            elif type == 'min':
                if self._heap[index] < self._heap[parent]:
                    self._swap(parent, index)
                    self._traverseUp(parent, type)

"""Class for to create MaxHeap"""
class MaxHeap(__HeapOperations):
    def __init__(self, *elements):
        super().__init__()
        [self.push(elem) for elem in elements]

    # This function pushes the given element/elements to the heap and rearranges the heap
    def push(self, *elements):
        for element in elements:
            self._heap.append(element)
            index = len(self._heap)-1
            if not index:
                pass
            else:
                self._traverseUp(index, 'max')
        return self._heap

    # This function pops the first element from the heap and rearranges the heap
    def pop(self):
        if len(self._heap):
            self._swap(0, len(self._heap)-1)
            poppedElement = self._heap.pop()
            self._traverseDown(0, 'max')
            return poppedElement
        else:
            return None

    # This returns the first element of the heap
    def peek(self):
        if self._heap:
            return self._heap #removee
        else:
            return "The _heap is empty"

"""Class to create the MinHeap"""
class MinHeap(__HeapOperations):
    def __init__(self, *elements):
        super().__init__()
        [self.push(elem) for elem in elements]

    # This function pushes the given element/elements to the heap and rearranges the heap
    def push(self, *elements):
        for element in elements:
            self._heap.append(element)
            index = len(self._heap)-1
            if not index:
                pass
            else:
                self._traverseUp(index, 'min')
        return self._heap

    # This function pops the first element from the heap and rearranges the heap
    def pop(self):
        if len(self._heap):
            self._swap(0, len(self._heap)-1)
            poppedElement = self._heap.pop()
            self._traverseDown(0, 'min')
            return poppedElement
        else:
            return None

    # This returns the first element of the heap
    def peek(self):
        if self._heap:
            return self._heap[0]
        else:
            return "The _heap is empty."

a = MaxHeap(1,4,7)
a.push(3,8)
print(a._heap)
