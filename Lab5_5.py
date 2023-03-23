class LinkList:
    class Node:
        def __init__(self,data,next = None):
            self.data = data
            if next == None:
                self.next = None
            else:
                self.next = next
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):          
        s = ''
        p = self.head
        while p != None :
            if p.next !=None :
                s += str(p.data)+' -> '
            else :
                s += str(p.data)
            p = p.next
        return s
    
    def len(self):
        return self.size
    
    def append(self,data):
        if self.head == None:
            p = self.Node(data)
            self.head = p
            self.tail = p
            self.size += 1
        else:
            q = self.tail
            p = self.Node(data)     
            q.next = p
            self.tail = p
            self.size += 1

posMaxDigit = 0
negMaxDigit = 0
currentDigit = 0
x = 0
maxNum = 0
minNum = 0
inp = input("Enter Input : ").split()
posL = LinkList()
negL = LinkList()
for i in inp:
    currentDigit = int(i)
    if maxNum < currentDigit and currentDigit >= 0:
        maxNum = currentDigit
        posMaxDigit = len(str(currentDigit))
    elif minNum > currentDigit and currentDigit < 0:
        minNum = currentDigit
        negMaxDigit = len(str(currentDigit))-1
    if int(i) >= 0:
        posL.append(str(i))
    else:
        negL.append(str(i)[1:])
if negMaxDigit >= posMaxDigit:
    x = negMaxDigit
else:
    x = posMaxDigit
arrow =  ' -> '.join(inp)

###Positive
digit = -1
index = 0
posDigitList = [LinkList() for e in (range(posMaxDigit+1))]
while index < posMaxDigit+1:
    if index != 0:
        for i in reversed(range(10)):
            headDigit = posDigitList[index-1].head
            while headDigit != None:
                if len(str(headDigit.data)) < -digit and i == 0:
                    posDigitList[index].append(headDigit.data)
                elif len(str(headDigit.data)) >= -digit:
                    if i == int(str(headDigit.data)[digit]):
                        posDigitList[index].append(headDigit.data)
                headDigit = headDigit.next
    else:
        for i in reversed(range(10)):
            headDigit = posL.head
            while headDigit != None:
                if i == int(str(headDigit.data)[digit]):
                    posDigitList[index].append(headDigit.data)
                headDigit = headDigit.next
    index += 1
    digit -= 1

###Negative###
digit = -1
index = 0
negDigitList = [LinkList() for e in range(negMaxDigit+1)] 
while index < negMaxDigit+1:
    if index != 0:
        for i in (range(10)):
            headDigit = negDigitList[index-1].head
            while headDigit != None:
                if len(str(headDigit.data)) < -digit and i == 0:
                    negDigitList[index].append(headDigit.data)
                elif len(str(headDigit.data)) >= -digit:
                    if i == int(str(headDigit.data)[digit]):
                        negDigitList[index].append(headDigit.data)
                headDigit = headDigit.next
    else:
        for i in (range(10)):
            headDigit = negL.head
            while headDigit != None:
                if i == int(str(headDigit.data)[digit]):
                    negDigitList[index].append(headDigit.data)
                headDigit = headDigit.next
    index += 1
    digit -= 1
        
radixSort = LinkList()
radixSort_Display = LinkList()
posNum = posDigitList[-1].head
negNum = negDigitList[-1].head
while posNum != None or negNum != None:
    if negNum == None:
        radixSort.append(posNum.data)
        radixSort_Display.append(int(posNum.data))
        posNum = posNum.next
    else:
        if posNum == None:
            radixSort.append(negNum.data)
            radixSort_Display.append(int('-'+str(negNum.data)))
            negNum = negNum.next
        else:
            radixSort.append(posNum.data)
            radixSort_Display.append(int(posNum.data))
            posNum = posNum.next

check = 0
count = 1
stop = False
exp = 1
print('------------------------------------------------------------')
while not stop :
    print('Round : '+ str(count))
    for i in range(10):
        display = radixSort_Display.head
        print(str(i)+' :',end = ' ')
        while display != None:
            if i == ((-display.data//exp)%10) and display.data < 0:
                print(display.data,end = ' ')
                if i == 0:
                    check += 1
            elif i == ((display.data//exp)%10) and display.data >= 0:
                print(display.data,end = ' ')
                if i == 0:
                    check += 1
            display = display.next
        print()
    count += 1
    if check == radixSort_Display.size :
        stop = True
    check = 0
    if len(str(exp)) > x:
        stop = True
    exp *= 10
    print('------------------------------------------------------------')

print(str(count-2)+' Time(s)')
print('Before Radix Sort :',end=' ')
print(arrow)
print('After  Radix Sort :',end=' ')
print(radixSort_Display.__str__())
