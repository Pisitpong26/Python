class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

def insert(root,data):
    if root == None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left,data)
        else:
            root.right = insert(root.right,data)
    return root

def printTree(node, level = 0):
        if node != None:
            printTree(node.right, level + 1)
            print('     ' * level, node)
            printTree(node.left, level + 1)

def bi_search(root, target):
    if root == None:
        return False
    elif root.data == target:
        return True
    elif root.data < target:
        return bi_search(root.right,target)
    else:
        return bi_search(root.left,target)

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
root = None
for i in arr:
    root = insert(root,i)
print(bi_search(root,k))