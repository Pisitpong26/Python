class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self,table,tablSize,conllision):
        self.table = table
        self.tableSize = tablSize
        self.conllision = conllision

    def charToAscii(self,key):
        sumKey = 0
        for i in key:
            sumKey += ord(i)
        return sumKey

    def QuadraticProbing(self,key):
        index = self.charToAscii(key)%self.tableSize
        conllision = 1
        while self.table[index] != None:
            print('collision number {0} at {1}'.format(conllision,index))
            if conllision == self.conllision:
                print('Max of collisionChain') 
                return None
            index = (self.charToAscii(key) + pow(conllision,2))%self.tableSize
            conllision += 1

        return index

    def printTable(self):
        for i in range(self.tableSize):
            print('#'+str(i+1)+'	'+str(self.table[i]))
        print('---------------------------')

print(' ***** Fun with hashing *****')
inp1,inp2 = input('Enter Input : ').split('/')
inp1 = inp1.split()
tableSize = int(inp1[0])
conllision = int(inp1[1])
L = inp2.split(',')
table = [None] * tableSize
x = hash(table,tableSize,conllision)
for i in range(len(L)):
    check = 0
    for j in range(len(table)):
        if table[j] != None:
            check += 1
        if check == len(table):
            print('This table is full !!!!!!')
            exit()
    key,value = L[i].split()
    index = x.QuadraticProbing(key)
    if index != None:
        table[index] = Data(key,value)
    x.printTable()

