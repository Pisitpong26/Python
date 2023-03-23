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
        
    def delete(self,node, data):
        if node == None:
            print('Error! Not Found DATA')
            return 
        elif node.data != data:
            if int(data) < int(node.data):
                node.left = self.delete(node.left,data)
            else:
                node.right = self.delete(node.right,data)
        else:
            if node.left == None:
                node = node.right
                return node
            elif node.right == None:
                node = node.left
                return node
            else:
                currentNode = node.right
                while currentNode.left != None:
                    currentNode = currentNode.left
                node.data = currentNode.data
                node.right = self.delete(node.right,currentNode.data)
        return node     


    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
x = input('Enter Input : ').split(',')
for i in x:
    if i[:1] == 'i':
        print('insert {0}'.format(i[2:]))
        root = T.insert(i[2:])
        T.printTree(root)
    if i[:1] == 'd':
        print('delete {0}'.format(i[2:]))
        T.root = T.delete(T.root,i[2:])
        T.printTree(T.root)

