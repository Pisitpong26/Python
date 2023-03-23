class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)
class BTS:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
            return self.root
        else:
            node = self.root
            while True:
                if data < node.data:
                    if node.left == None:
                        node.left = Node(data)
                        return self.root
                    node = node.left
                else:
                    if node.right == None:
                        node.right = Node(data)
                        return self.root
                    node = node.right
        
    def rank(self,node,data):
        if self.root == None:
            return 0
        rank = 0
        if node != None:
            rank += self.rank(node.left,data)
            if node.data <= data:
                rank += 1
            rank += self.rank(node.right,data)
        return rank

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
T = BTS()
inp,data = input('Enter Input : ').split('/')
inp = [int(i) for i in inp.split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
print('Rank of {0} : {1}'.format(data,T.rank(root,int(data))))