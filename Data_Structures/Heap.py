class Heap:
    def __init__(self):
        self.size = 0
        self.heap = []

    def getParent(self,index):
        return index // 2

    def getLeftChild(self,index):
        return 2*index + 1
    
    def getRightChild(self,index):
        return 2*index + 2


class MinHeap(Heap):
    def __init__(self):
        super().__init__()

    def insert(self,val):
        self.heap.append(val)
        self.size += 1

        valIndex = self.size - 1
        parentIndex = self.getParent(valIndex)

        # While new val is smaller than its parent and it is not the root node
        while(valIndex != 0 and self.heap[valIndex] < self.heap[parentIndex]):
            self.heap[valIndex], self.heap[parentIndex] = self.heap[parentIndex], self.heap[valIndex] #swap values
            
            valIndex = parentIndex
            parentIndex = self.getParent(valIndex)

        return

    def pop(self):
        minVal = self.heap[0] #extract min
        self.heap[0] = self.heap.pop() #remove min element, swap with bottom-right most value (note: it's a different pop(), be careful)
        
        self.size -= 1

        #bubble this value down
        self.minHeapify(0)
        return minVal

    def minHeapify(self,index):

        leftChildIndex = self.getLeftChild(index)
        rightChildIndex = self.getRightChild(index)

        while((leftChildIndex < self.size and self.heap[index] > self.heap[leftChildIndex]) or (rightChildIndex < self.size and self.heap[index] > self.heap[rightChildIndex])):
            if(rightChildIndex >= self.size or (leftChildIndex < self.size and self.heap[leftChildIndex] < self.heap[rightChildIndex])): #swap with the lesser of the two
                self.heap[index], self.heap[leftChildIndex] = self.heap[leftChildIndex], self.heap[index]
                index = leftChildIndex
            else:
                self.heap[index], self.heap[rightChildIndex] = self.heap[rightChildIndex], self.heap[index]
                index = rightChildIndex
        
            leftChildIndex = self.getLeftChild(index)   
            rightChildIndex = self.getRightChild(index)

        return

class MaxHeap(Heap):
    def __init__(self):
        super().__init__()

    def insert(self,val):
        self.heap.append(val)
        self.size += 1

        valIndex = self.size - 1
        parentIndex = self.getParent(valIndex)

        # While new val is larger than its parent and it is not the root node
        while(valIndex != 0 and self.heap[valIndex] > self.heap[parentIndex]):
            self.heap[valIndex], self.heap[parentIndex] = self.heap[parentIndex], self.heap[valIndex] #swap values
            
            valIndex = parentIndex
            parentIndex = self.getParent(valIndex)

        return

    def pop(self):
        minVal = self.heap[0] #extract max
        self.heap[0] = self.heap.pop() #remove max element, swap with bottom-right most value (note: it's a different pop(), be careful)
        
        self.size -= 1

        #bubble this value down
        self.maxHeapify(0)
        return minVal

    def maxHeapify(self,index):

        leftChildIndex = self.getLeftChild(index)
        rightChildIndex = self.getRightChild(index)

        while((leftChildIndex < self.size and self.heap[index] < self.heap[leftChildIndex]) or (rightChildIndex < self.size and self.heap[index] < self.heap[rightChildIndex])):
            if(rightChildIndex >= self.size or (leftChildIndex < self.size and self.heap[leftChildIndex] > self.heap[rightChildIndex])): #swap with the greater of the two
                self.heap[index], self.heap[leftChildIndex] = self.heap[leftChildIndex], self.heap[index]
                index = leftChildIndex
            else:
                self.heap[index], self.heap[rightChildIndex] = self.heap[rightChildIndex], self.heap[index]
                index = rightChildIndex
        
            leftChildIndex = self.getLeftChild(index)   
            rightChildIndex = self.getRightChild(index)

        return




if __name__ == "__main__":
    #Create min heap
    minHeap = MinHeap()
    minHeap.insert(2)
    minHeap.insert(1)
    minHeap.insert(3)
    minHeap.insert(7)
    minHeap.insert(4)

    #Test cases
    assert minHeap.heap == [1,2,3,7,4]
    assert minHeap.pop() == 1
    assert minHeap.heap == [2,4,3,7]
    print("Passed Min Heap Test Cases")

    #Create max heap
    maxHeap = MaxHeap()
    maxHeap.insert(2)
    maxHeap.insert(1)
    maxHeap.insert(3)
    maxHeap.insert(7)
    maxHeap.insert(4)

    #Test cases
    assert maxHeap.heap == [7,4,3,2,1]
    assert maxHeap.pop() == 7
    assert maxHeap.heap == [4,2,3,1]
    print("Passed Max Heap Test Cases")

    
