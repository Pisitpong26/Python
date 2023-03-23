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
        return self.getHeight(node.left) - self.getHeight(node.right)
    
    def leftRotate(self,node):
        a = node.right
        b = a.left

        a.left = node 
        node.right = b

        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))
        a.height = 1 + max(self.getHeight(a.left),self.getHeight(a.right))

        return a

    def rightRotate(self,z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3
        
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    def insert(self, root, key):
     
        if root == None:
            return Node(key)
        elif key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))
 
        balance = self.getBalance(root)

        if balance > 1 and key < root.left.data:
            return self.rightRotate(root)
 
        if balance < -1 and key >= root.right.data:
            return self.leftRotate(root)
 
        if balance > 1 and key >= root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        if balance < -1 and key <= root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root
 
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
