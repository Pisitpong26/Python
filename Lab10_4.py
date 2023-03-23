class Data:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "{0}".format(self.value)

class hash:
    def __init__(self,table,tablSize,conllision):
        self.table = table
        self.tableSize = tablSize
        self.conllision = conllision

    def QuadraticProbing(self,value):
        index = value%self.tableSize
        conllision = 1
        while self.table[index] != None:
            print('collision number {0} at {1}'.format(conllision,index))
            if conllision == self.conllision:
                print('****** Max collision - Rehash !!! ******')
                return None
            index = (value + pow(conllision,2))%self.tableSize
            conllision += 1

        return index

    def printTable(self):
        for i in range(self.tableSize):
            print('#'+str(i+1)+'	'+str(self.table[i]))
        print('----------------------------------------')

def prime(tableSize):
    if tableSize % 2 != 0 and tableSize % 3 != 0:
        return tableSize
    return prime(tableSize+1)

def countData(table):
    count = 0
    for i in table:
        if i != None:
            count += 1
    return count

print(' ***** Rehashing *****')
inp1,inp2 = input('Enter Input : ').split('/')
print('Initial Table :')
inp1 = inp1.split()
tableSize = int(inp1[0])
conllision = int(inp1[1])
Threshold  = int(inp1[2])
L = inp2.split()
table = [None] * tableSize
x = hash(table,tableSize,conllision)
status = 0
i = 0
cop = None
while i != (len(L)):

    if status == 0 :
        x.printTable()
        print('Add :',L[i])

    if cop == L[i]:
        status = 0

    index = x.QuadraticProbing(int(L[i]))

    if index != None:
        table[index] = Data(int(L[i]))
        
        if (countData(table)*100)/tableSize >= Threshold:

            print('****** Data over threshold - Rehash !!! ******') 
            cop = L[i]
            status = 1
            x2 = tableSize*2
            newTableSize = prime(x2)
            tableSize = newTableSize
            table = [None] * tableSize
            x = hash(table,newTableSize,conllision)
            i = 0

        else:    
            i += 1

        if i == len(L):
            x.printTable()
    else:
        cop = L[i]
        x2 = tableSize*2
        newTableSize = prime(x2)
        tableSize = newTableSize
        table = [None] * tableSize
        x = hash(table,newTableSize,conllision)
        status = 1
        i = 0

        """if index != None:
            table[index] = Data(int(L[i]))
        x.printTable()"""

        


    

