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

inp = input('Enter Input : ').split()

S = Stack()
x = 0
i = 0
combo = 0

for e in inp:
    S.__init__(e)
    if S.size() > 1:
        while i < S.size():
            if i > 0:
                if S.items[i] == S.items[i-1]:
                    x += 1
                else :
                    x = 0
                if x == 2:
                    S.pop()
                    S.pop()
                    S.pop()
                    combo += 1
                    i = 0
                    x = 0
            i += 1

print(S.size())
S.items.reverse()
if S.size() == 0:
    print('Empty',end='')
else:
    for i in range(S.size()):
        print(S.items[i],end='')

if combo > 1:
    print('\nCombo : '+str(combo)+' ! ! !')
