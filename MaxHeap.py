
class MaxHeap():
    def __init__(self):
        self.heap = []

    def __swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def __traverseDown(self, index):
        left = index*2+1
        right = index*2+2
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(largest, index)
            self.__traverseDown(largest)

    def __traverseUp(self, index):
        if index == 0:
            pass
        else:
            parent = (index-1)//2
            if self.heap[index] > self.heap[parent]:
                self.__swap(parent, index)
                self.__traverseUp(parent)


    def push(self, element):
        self.heap.append(element)
        index = self.heap.index(element)
        if not index:
            return 1
        else:
            self.__traverseUp(index)

    def pop(self):
        self.__swap(0, len(self.heap)-1)
        poppedElement = self.heap.pop()
        self.__traverseDown(0)
        print(poppedElement)

    def peek(self):
        if self.heap:
            print(self.heap[0])
        else:
            print("No elements in the heap")
