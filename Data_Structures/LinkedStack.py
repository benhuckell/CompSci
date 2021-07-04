from Node import Node

class LinkedStack:

    def __init__(self):
        self.head = None
        return

    '''
    Remove the top item from the stack
    '''
    def pop(self):

        if(self.isEmpty()):
            return None

        val = self.head.val
        self.head = self.head.next
        return val
    
    '''
    Ad an item to the top of the stack
    '''
    def push(self, item):
        newNode = Node(item)
        oldHead = self.head
        self.head = newNode
        newNode.next = oldHead
        return

    '''
    Return the top of the stack
    '''
    def peek(self):

        if(self.isEmpty()):
            return None

        return self.head.val

    '''
    Return true if and only if the stack is empty
    '''
    def isEmpty(self):
        return (self.head == None)

    '''
    Prints out the stack
    '''
    def display(self):
         
        iternode = self.head
        if self.isEmpty():
            print("Stack Underflow")
         
        else:
            while(iternode != None):
                 
                print(iternode.val,"->",end = " ")
                iternode = iternode.next
            return


if __name__ == "__main__":
    linkedStack = LinkedStack()
    print(linkedStack.isEmpty())
    linkedStack.push(4)
    linkedStack.push(7)
    linkedStack.push(1)
    print(linkedStack.peek())
    print(linkedStack.pop())
    print(linkedStack.peek())
    linkedStack.display()