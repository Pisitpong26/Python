class Stack :

    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def dec2bin(self,decnum):
        while decnum > 0:
            self.items.append(decnum%2)
            decnum = int(decnum/2)
        if decnum <= 0:
            self.items.reverse()
        for e in self.items:
            print(e,end='')

print(" ***Decimal to Binary use Stack***")
s = Stack()
token = input("Enter decimal number : ")

print("Binary number : ",end='')
s.dec2bin(int(token))