class node:
    def __init__(self,data,next = None ):
        self.data = data
        if next == None:
            self.next = None
        else:
            self.next = next

    def __str__(self):
        return str(self.data)

def createList(l=[]):
    head = node(l[0])
    temp = head
    for i in range(1,len(l)):
        nxt = node(l[i])
        temp.next = nxt
        temp = temp.next
    return head

def printList(H):
    temp = H
    while temp != None:
        print(str(temp),end=' ')
        temp = temp.next
    print()


def mergeOrderesList(p,q):
    if int(p.data) < int(q.data):
        temp = p
        NextP = p.next
        NextQ = q
    else:
        temp = q
        NextP = p
        NextQ = q.next
    x = temp    
    while NextP != None or NextQ != None:
        if NextP != None and NextQ != None:
            if int(NextP.data) < int(NextQ.data):
                temp.next = NextP
                temp = temp.next
                NextP = NextP.next
            else:
                temp.next = NextQ
                temp = temp.next
                NextQ = NextQ.next
        elif NextP != None :
            temp.next = NextP
            temp = temp.next
            NextP = NextP.next
        else:
            temp.next = NextQ
            temp = temp.next
            NextQ = NextQ.next
    return x

inp1,inp2 = input("Enter 2 Lists : ").split()
L1 = inp1.split(',')
L2 = inp2.split(',')
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)