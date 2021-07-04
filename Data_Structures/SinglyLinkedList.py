from Node import Node

class SinglyLinkedList:
    #Must provide head with a Node type
    def __init__(self,head = None):
        self.head = head
        self.size = 0 if head is None else 1

    def __len__(self):
        return self.size

    '''
    Runtime: O(n), unless we add a refence to the tail, which would make it O(1)
    '''
    def appendright(self, newData):
        newNode = Node(newData)

        if(self.head): #if head exists
            current = self.head

            while(current.next):
                current = current.next
            current.next = newNode
            
        else: #head does not already exist
            self.head = newNode

        self.size += 1

    '''
    Runtime: O(1)
    '''
    def appendleft(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    '''
    Runtime: Search time + O(1)
    '''
    def insertAfter(self, valToFind, newData):

        newNode = Node(newData)

        current = self.head

        while(current):
            if(current.val == valToFind):
                prevNext = current.next
                current.next = newNode
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
    myList = SinglyLinkedList()
    myList.appendright(5)
    myList.appendright(4)
    myList.appendleft(3)
    myList.insertAfter(4,7)
    myList.appendleft(1)
    myList.printLinkedList()
    print("Length:",len(myList))




