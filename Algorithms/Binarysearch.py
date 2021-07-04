arrayTest = [13,400,612,33,81,422,68,12,44,61,3,4,73,45,2232,34,63,6323,1242,15,41,5,6,21,8,1,9]

arrayTest.sort()

class ArrayStack:

    def __init__(self):
        self._S = []
        self._n = 0

    def __len__(self):
        return(self._n)

    def push(self,e):
        self._S.append(e)
        self._n += 1
        return
    
    def pop(self):
        if(self._n == 0):
            raise ValueError("Stack is empty")
        self._n -= 1
        return self._S.pop()
    
    def is_empty(self):
        return(self._n == 0)


#stack = ArrayStack()

#stack.push(1)
#print(stack.pop())
    
class DoublyLinkedBase:
    #Define nested class
    class Node:
        def __init__(self,element,next,prev):
            self.element = element
            self.next = next   
            self.prev = prev

    def __init__(self):
        self.size = 0
        self.header = self.Node(None,None,None)
        self.trailer = self.Node(None,None,None)

    def addNode(self,e,predessor,successor):
        newest = self.Node(e,predessor,successor)
        predessor.next = newest
        successor.prev = newest
        self.size += 1

    def deleteNode(self,node):
        predessor = node.prev
        successor = node.next
        predessor.next = successor
        successor.prev = predessor
        self.size -= 1
    
    def is_empty(self):
        return (self.size == 0)
    
    def __len__(self):
        return self.size
        

class LinkedStack:

    #Define nested class
    class Node:
        def __init__(self,element,next):
            self.element = element
            self.next = next

    def __init__(self):
        self.size = 0
        self.head = None
    
    def push(self,e):
        self.head = self.Node(e,self.head)
        self.size += 1

    def pop(self):
        if(self.head is None):
            raise ValueError("Linked Stack is empty")
        e = self.head.element
        self.head = self.head.next
        self.size -= 1
        return e

    def top(self):
        if(self.head is None):
            raise ValueError("Liked stack is empty")
        return self.head.element

    def is_empty(self):
        return (self.size == 0)

    def __len__(self):
        return self.size

    




def recursiveSearch(number, array):
    mid = len(array)/2
    print(array[mid])

    if(number > array[mid]):
        recursiveSearch(number, array[mid:len(array)])

    if(number < array[mid]):
        recursiveSearch(number, array[0:mid])

    if(number == array[mid]):
        print(mid)

    return

def reverseListRecursively(array,start,stop):
    if start < stop-1:
        arrayTest[start], arrayTest[stop-1] = arrayTest[stop-1], arrayTest[start]
        reverseListRecursively(arrayTest,start+1,stop-1)
    return

#recursiveSearch(61,arrayTest)
#reverseListRecursively(arrayTest,0,len(arrayTest))
#print(arrayTest)