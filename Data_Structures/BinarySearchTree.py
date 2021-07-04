from Node import TreeNode


class BinarySearchTree:
    def __init__(self, root):
        self.root = root
        self.size = 1

    def __len__(self):
        return self.size

    '''
    Time Complexity: O(log(n)) -> binary search
    Returns: bool
    ''' 
    def exists(self, root, key):
        if(root is None):
            return False
        if(key == root.val):
            return True
        
        if(key > root.val):
            return self.exists(root.right,key)
        else:
            return self.exists(root.left,key)

    '''
    Gets the desired node if it exists. If it doesnt exist, returns None
    Time Complexity: O(log(n)) -> binary search
    Returns: root
    ''' 
    def search(self, root, key):
        if(root is None or key == root.val):
            return root
        
        if(key > root.val):
            return self.search(root.right,key)
        else:
            return self.search(root.left,key)

    '''
    Inserts node into BST. Will not insert if duplicate found
    Time Complexity: O(log(n)) -> binary search
    Returns: root
    '''
    def insert(self, root, val):
        if(root):
            if(val == root.val): #duplicate, do nothing
                return root
            elif(val > root.val):
                root.right = self.insert(root.right,val)
            elif(val < root.val):
                root.left = self.insert(root.right,val)
        else:
            self.size += 1
            return TreeNode(val)

        return root

    def successor(self, root):
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val


    '''
    Delete node with val = key
    Time Complexity: O(log(n)) -> Binary Search
    '''
    def delete(self, root, key):
        if not root:
            return None

        # delete from the right subtree
        if key > root.val:
            root.right = self.delete(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.delete(root.left, key)
        # delete the current node
        else:
            
            # the node is a leaf
            if not (root.left or root.right):
                self.size -= 1
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.delete(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child
            else:
                root.val = self.predecessor(root)
                root.left = self.delete(root.left, root.val)

        return root

    

if __name__ == "__main__":
    bst = BinarySearchTree(TreeNode(5))
    bst.insert(bst.root,7)
    print(bst.search(bst.root,5))
    print(bst.exists(bst.root,7))
    print(bst.exists(bst.root,8))
    print(len(bst))
    bst.insert(bst.root,9)
    print(bst.exists(bst.root,9))
    print(len(bst))
    bst.delete(bst.root,7)
    print(bst.exists(bst.root,7))
    print(len(bst))
    bst.delete(bst.root,9)
    print(bst.exists(bst.root,9))
    print(len(bst))


        




