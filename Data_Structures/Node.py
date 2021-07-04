class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class DoubleNode:
    def __init__(self, data):
        self.val = data
        self.next = None
        self.prev = None

class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)