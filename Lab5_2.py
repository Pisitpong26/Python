class DoublyLinklist:
    class Node:
        def __init__(self, data,previous = None,next = None):
            self.data = data
            self.next = next
            self.previous = previous

    def __init__(self):
        self.dummy = self.Node(None,None,None)
        self.dummy.next = self.dummy.previous = self.dummy
        self.siz = 0   
    
    def __str__(self):
        s = ''
        p = self.dummy.next
        for i in range(len(self)-1):
            s += str(p.data) + '->'
            p = p. next
        if str(p.data) != 'None':
            s += str(p.data)
        return s
    
    def str_reverse(self):
        s = ''
        p = self.goToNode(len(self)-1)
        for i in range(len(self)-1):
            s += str(p.data) + '->'
            p = p.previous
        if str(p.data) != 'None':
            s += str(p.data)
        return s

    def __len__(self) :
        return self.siz

    def isEmpty(self):
        return self.siz == 0    

    def index(self,data):
        p = self.dummy.next
        for i in range(len(self)):
            if p.data == data:
                return i
            p = p.next
        return -1

    def goToNode(self,index):
        p = self.dummy
        for i in range(-1,index):
            p = p.next
        return p

    def insert(self,p,data):
        s = p.previous
        x = self.Node(data,s,p)
        s.next = p.previous = x 
        self.siz += 1

    def append(self,data):
        self.insert(self.goToNode(len(self)),data)

    def remove(self,data):
        if self.index(data) >= 0:
            data = self.goToNode(self.index(data))
            p = data.previous
            q = data.next
            q.previous = p
            p.next = q
            self.siz -= 1
            return data
        else:
            return -1
    
d = DoublyLinklist()
inp = input('Enter Input : ').split(',')
for i in range(len(inp)):
    alpha = inp[i].split()
    x = alpha[0]
    y = alpha[1]
    if x == 'A':
        d.append(y)
    elif x == 'Ab':
        d.insert(d.goToNode(0),y)
    elif x == 'I':
        y = y.split(':')
        if int(y[0]) < 0 or len(d) < int(y[0]):
            print("Data cannot be added")
        else:
            d.insert(d.goToNode(int(y[0])),y[1])
            print("index = {0} and data = {1}".format(y[0],y[1]))
    elif x == 'R':
        i = d.index(y)
        j = d.remove(y)
        if j == -1:
            print("Not Found!")
        else:
            print("removed : {0} from index : {1}".format(str(j.data),str(i)))
        
    print("linked list : " + str(d))
    print("reverse : "+d.str_reverse())
    
