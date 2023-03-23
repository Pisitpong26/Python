class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):  
        if self.root == None:
            self.root = Node(val)
            print('*')    
            return self.root
        else:
            node = self.root
            while True:
                if int(val) < int(node.data):
                    print('L',end='')
                    if node.left == None:
                        node.left = Node(val)
                        print('*')
                        break
                    node = node.left
                else:
                    print('R',end='')
                    if node.right == None:
                        node.right = Node(val)
                        print('*')
                        break
                    node = node.right

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)

