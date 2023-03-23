class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.data)

class AVL:
    def __init__(self):
        self.root = None

    def getHeight(self,node):
        if node == None:
            return 0
        return node.height

    def getBalance(self,node):
        if node == None:
            return 0
        return (self.getHeight(node.left)-self.getHeight(node.right))

    def leftRotate(self,node):
        a = node.right
        b = a.left

        a.left = node
        node.right = b

        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))
        a.height = 1 + max(self.getHeight(a.left),self.getHeight(a.right))
        return a

    def rightRotate(self,node):
        a = node.left
        b = a.right

        a.right = node
        node.left = b

        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))
        a.height = 1 + max(self.getHeight(a.left),self.getHeight(a.right))
        return a

    def insert(self,node,data):
        if node == None:
            return Node(data)
        else:
            if data < node.data:
                node.left = self.insert(node.left,data) 
            else:
                node.right = self.insert(node.right,data)
            
        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))

        balance = self.getBalance(node)

        if balance > 1 and data < node.left.data:
            return self.rightRotate(node)

        if balance > 1 and data >= node.left.data:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        if balance < -1 and data < node.right.data:
            return self.leftRotate(node)

        if balance < -1 and data >= node.right.data:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    """def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return self.root
        else:
            node = self.root
            while True:
                if node.data < data:
                    if node.right != None:
                        node = node.right
                    else:
                        node.right = Node(data)
                        return self.root
                else:
                    if node.left != None:
                        node = node.left
                    else:
                        node.left = Node(data)
                        return self.root"""
    
    def delete(self,node,data):
        if node == None:
            print('Error! Not Found DATA')
            return
        elif node.data < data:
            node.right = self.delete(node.right,data)
        elif node.data > data:
            node.left = self.delete(node.left,data)
        else:
            if node.right == None:
                node = node.left
                return node
            if node.left == None:
                node = node.right
                return node
            else:
                cur = node.right
                while cur.left != None:
                    cur = cur.left
                node.data = cur.data
                node.right = self.delete(node.right,cur.data)
        return node

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = AVL()
inp = [int(i) for i in input('Enter Input : ').split()]
root = None
for i in inp:
    print('Insert : ( {0} )'.format(i))
    root = T.insert(root,i)
    T.printTree(root)
    print('--------------------------------------------------')