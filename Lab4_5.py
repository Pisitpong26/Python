class Stack:

    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items += list

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def size(self):
        return len(self.items)
    
    def enQueue(self,val):
        return self.items.append(val)
    
    def deQueue(self):
        return self.items.pop(0)

team = ['NORMAL ','MIRROR']
S = Stack()
S2 = Stack()
Q = Queue()
i = 0
j = 0
inp = input("Enter Input (Normal, Mirror) : ").split()
x = []
y = []

for ele in inp[0]:
    y.append(ele)
for ele in inp[1]:
    x.append(ele)
x.reverse()

combo1 = 0
for ele in x:
    S.push(ele)
    if S.size() > 1:
            while i < S.size():
                if i > 0:
                    if S.items[i] == S.items[i-1]:
                        j += 1
                    else :
                        j = 0
                    if j == 2:
                        S.items.pop()
                        S.items.pop()
                        Q.enQueue(S.items.pop())
                        combo1 += 1
                        i = 0
                        j = 0
                i += 1

i = 0
j = 0
combo = 0
fail = 0
for ele in y:
    S2.push(ele)
    if S2.size() > 1:
            while i < S2.size():
                if i > 0:
                    if S2.items[i] == S2.items[i-1]:
                        j += 1
                    else :
                        j = 0
                    if j == 2:
                        if Q.size() > 0:
                            S2.items.insert(i,Q.deQueue())
                            if S2.items[i] == S2.items[i-1] == S2.items[i-2]:
                                S2.pop()
                                S2.pop()
                                S2.pop()
                                fail += 1
                                i = 0
                                j = 0
                        else:
                            S2.pop()
                            S2.pop()
                            S2.pop()
                            combo += 1
                            j = 0
                            i = 0
                i += 1
print("NORMAL :")
if S2.size() > 0:
    print(S2.size())
    S2.items.reverse()
    for i in S2.items:
        print(str(i),end='')
else:
    print(S2.size())
    print('Empty',end='')
print('\n'+str(combo)+' Explosive(s) ! ! ! (NORMAL)')
if fail > 0:
    print('Failed Interrupted '+str(fail)+' Bomb(s)')
print('------------MIRROR------------')
print(': RORRIM')
if S.size() > 0:
    print(S.size())
    S.items.reverse()
    for i in S.items:
        print(str(i),end='')
if S.size() == 0:
    print(S.size())
    print('ytpmE',end='')
print('\n(RORRIM) ! ! ! (s)evisolpxE '+str(combo1))
