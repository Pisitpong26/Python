class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def enQueue(self,val):
        return self.items.append(val)

    def deQueue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

inp = input("Enter Input : ").split(',')
S = Queue()
for i in inp:
    if i[0] == 'E':
        j = i.split()
        S.enQueue(j[1])
        print("Add " + str(S.items[S.size()-1]) + " index is " + str(S.size()-1))
    elif i[0] == 'D':
        if S.size() > 0:
            print("Pop " + str(S.deQueue()) + " size in queue is " + str(S.size()))
        else:
            print("-1")
if S.size() > 0:
    print("Number in Queue is :  "+str(S.items))
else:
    print("Empty")