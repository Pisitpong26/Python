class LinkList:
    class node:
        def __init__(self,data,next = None,previous = None):
            self.data = data
            if next == None:
                self.next = None
            else:
                self.next = next

            if previous == None:
                self.previous = None
            else:
                self.previous = previous

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def toNode(self,index):
        p = self.head
        for i in range(0,index):
            p = p.next
        return p

    def append(self,data):
        if self.head == None:
            item = self.node(data)
            self.head = item
            self.tail = item
            self.next = None
            self.previous = None
            self.size += 1
        else:
            self.insert(self.size-1,data)
    
    def insert(self,i,data):
        if self.size == 0:
            self.addHead(data)   
        else:
            if i<0:
                if(-i > self.size):
                    i = -1
                else:
                    i = self.size + i-1
            if i >= self.size:
                i = self.size-1
            if i == -1:
                self.addHead(data)
            else:
                q = self.toNode(i)
                p = self.node(data)
                if self.size-1!=i:
                    r = self.toNode(i+1)
                    r.previous = p

                p.next = q.next
                q.next = p
                p.previous = q
                
                if i == self.size-1:
                    self.tail = p
                self.size += 1

    def deleteData(self,index):
        if self.size > 0:
            p = self.toNode(index)
            p.next = p.next.next
            self.size -= 1
    
    def deleteHead(self):
        q = self.head.next
        q.previous = None
        self.head = q
        self.size-=1
    
    def addHead(self,data) :
        if self.size == 0 :
            p = self.node(data)
            self.head = p
            self.tail = p
            self.size += 1
        else :
            q = self.head
            p = self.node(data)
            q.previous = p
            p.next = q
            self.head = p
            self.size += 1

L = LinkList()
cursor = 0
inp = input('Enter Input : ').split(',')
for i in range(len(inp)):
    x = inp[i].split()
    if x[0] == 'I':
        if(cursor!=0):
            L.insert(cursor-1,x[1])
        else:
            L.addHead(x[1])
        cursor += 1
    elif x[0] == 'L' and cursor > 0:
        cursor -= 1
    elif x[0] == 'R' and cursor < L.size:
        cursor += 1
    elif x[0] == 'B' and cursor > 0:
        cursor -= 1
        L.deleteData(cursor-1)
    elif x[0] == 'D' and cursor < L.size:
        if cursor == 0:
            L.deleteHead()
        else:
            L.deleteData(cursor-1)
    
for i in range(L.size):
    if cursor == i:
        print("|",end=' ')
    print(L.toNode(i).data,end=' ')
if cursor == L.size:
        print("|",end=' ')
        