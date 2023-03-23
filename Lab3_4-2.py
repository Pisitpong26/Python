class StackCalc:
    def __init__(self,list = None) :
        if list== None :
            self.items = []
            self.sysbol=['+','-','*','/','DUP','POP','PSH']
            self.ans=0
            self.cheak=False
        else :
            self.items = list

    def run(self,str):
        self.items=str.split(' ')
        for i in range (len(self.items)): 
            try:  
                if self.items[i] in self.sysbol:
                    continue
                else:
                    self.items[i] =int(self.items[i])
            except:
                print("Invalid instruction: "+ self.items[i])
                exit()
        temp=[]
        for i in self.items:
            temp.append(i)
            if i=='+':
                temp.pop()
                self.ans = temp[-1] + temp[-2]
                temp.pop()
                temp.pop()
                temp.append(self.ans)
                self.cheak=True

            elif i=='-': 
                temp.pop()
                self.ans = temp[-1] - temp[-2]
                temp.pop()
                temp.pop()
                temp.append(self.ans)
                self.cheak=True
                        
            elif i =='*': 
                temp.pop()
                self.ans = temp[-1] * temp[-2]
                temp.pop()
                temp.pop()
                temp.append(self.ans)
                self.cheak=True

            elif i =='/': 
                temp.pop()
                self.ans = temp[-1] / temp[-2]
                temp.pop()
                temp.pop()
                temp.append(self.ans)
                self.cheak=True
            elif i == 'DUP':
                temp.pop()
                temp.append(int(temp[-1]))
            elif i =='POP':
                temp.pop()
                temp.pop()
            elif i=='PSH':
                temp.pop()
        if not self.cheak :
                if temp == []:
                    self.ans=0
                else :
                    self.ans = temp[-1]
        self.items=temp
        
    def getValue(self) :
        return str(int(self.ans))

    def __str__(self) :
        return str(self.items)


print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())