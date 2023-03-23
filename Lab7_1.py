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

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            p =  self.root
            x = True
            while x == True:
                if data < p.data:
                    if p.left != None:
                        p = p.left
                    else:
                        p.left = Node(data)
                        x = False
                if data > p.data:
                    if p.right != None:
                        p = p.right
                    else:
                        p.right = Node(data)
                        x = False
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
    print(root)
T.printTree(root)