class Node:
    def __init__(self, data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.data)

class Stack:

    def __init__(self,list = None):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):  
        if self.root == None:
            self.root = Node(val)
            return self.root
        else:
            node = self.root
            while True:
                if int(val) < int(node.data):
                    if node.left == None:
                        node.left = Node(val)
                        return self.root
                    node = node.left
                else:
                    if node.right == None:
                        node.right = Node(val)
                        return self.root
                    node = node.right

    def prefix(self, node):
        if node == None:
            return ''
        s = str(node.data)\
            + self.prefix(node.left)\
                + self.prefix(node.right)
        return s

    def infix(self, node):
        if node == None:
            return ''
        s = self.infix(node.left)\
             + str(node.data)\
                 + self.infix(node.right)
        if node.left is not None and node.right is not None:
            s = '(' + s + ')'
        return s


    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
S = Stack()
inp = input('Enter Postfix : ')
for chr in inp:
    if chr in'+-*/':
        op1 = S.pop()
        op2 = S.pop()
        S.push(Node(chr,op2,op1))
    else:
        S.push(Node(chr))
print('Tree : ')
root = S.pop()
T.printTree(root)
print('--------------------------------------------------')
print('Infix : '+T.infix(root))
print('Prefix : '+T.prefix(root))

