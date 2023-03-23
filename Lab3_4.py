class StackCalc:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items += list

    def run(self,arg):
        inp = arg.split()
        
        for i in range(len(inp)):
            if inp[i].isdigit():
                self.items.append(inp[i])
            elif inp[i] == '+':
                    x = int(self.items.pop())+int(self.items.pop())
                    x = int(x)
                    self.items.append(x)
            elif inp[i] == '-':
                    x = int(self.items.pop())-int(self.items.pop())
                    x = int(x)
                    self.items.append(x)
            elif inp[i] == '*':
                    x = int(self.items.pop())*int(self.items.pop())
                    x = int(x)
                    self.items.append(x)
            elif inp[i] == '/':
                    x = int(self.items.pop())/int(self.items.pop())
                    x = int(x)
                    self.items.append(x)
            elif inp[i] == 'DUP' and len(self.items) > 0:
                y = self.items[i-1]
                self.items.append(y)
            elif inp[i] == 'POP' and len(self.items) > 0:
                self.items.pop()
                i = 0
            elif inp[i] == 'PSH':
                continue
            elif inp[i][0] == '-' and inp[i][1].isdigit():
                self.items.append(inp[i])
            else:
                print('Invalid instruction: '+str(inp[i]))
                exit()    

                
    def getValue(self):
        if len(self.items) > 0:
            value = self.items.pop()
        else:
            value = 0
        return value

print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())