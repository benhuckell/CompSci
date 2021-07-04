from Node import DoubleNode

class DoublyLinkedList:

    def __init__(self, head = None):
        self.head = head
        self.tail = head

        self.size = 0 if head is None else 1
    
    def __len__(self):
        return self.size

    '''
    Runtime: O(1)
    '''
    def appendright(self, newData):
        newNode = DoubleNode(newData)

        if(self.head):
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        
        else:
            self.head = newNode
            self.tail = newNode

        self.size += 1

    '''
    Runtime: O(1)
    '''
    def appendleft(self, newData):
        newNode = DoubleNode(newData)

        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        self.size += 1

        if(self.tail is None):
            self.tail = newNode

    '''
    Runtime: Search time + O(1)
    '''
    def insertAfter(self, valToFind, newData):
        newNode = DoubleNode(newData)

        current = self.head

        while(current):
            if(current.val == valToFind):
                prevNext = current.next
                current.next = newNode
                newNode.prev = current
                newNode.next = prevNext
                self.size += 1
                return
            elif(current.next is None):
                break
            else:
                current = current.next
        
        raise Exception("Insert after value not found")

    
    def printLinkedList(self):
        current = self.head
        while(current):
            print(current.val)
            current = current.next




if __name__ == "__main__":
    linkedList = DoublyLinkedList()
    linkedList.appendright(5)
    linkedList.appendright(6)
    linkedList.appendright(1)
    linkedList.appendleft(2)
    linkedList.insertAfter(2, 4)
    linkedList.printLinkedList()