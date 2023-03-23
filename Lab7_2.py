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
    
    def below(self,node,data):
        if node == None:
            return ''
        belowNum = ''
        belowNum += self.below(node.left,data)
        if int(node.data) < int(data):
            belowNum += str(node.data) + ' '
        belowNum += self.below(node.right,data)
        return belowNum


    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
x,y = input('Enter Input : ').split('|')
inp = [int(i) for i in x.split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
belowList = T.below(root,y)
if belowList == '':
    print('Below '+str(y)+' : Not have')
else:
    print('Below '+str(y)+' : '+belowList)