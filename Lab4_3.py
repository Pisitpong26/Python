class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self,val):
        self.items.append(val)
    
    def deQueue(self):
        self.items.pop(0)
    
    def enCodemsg(self,lst1,lst2):
        alph = lst2.copy()
        for i in range(len(lst1)):
            self.items.append(lst1[i])
        for i in range(len(self.items)):
            if ord(self.items[i]) >= 65 and ord(self.items[i]) <= 90:
                if ord(self.items[i])+int(alph[0]) <= 90:
                    self.items[i] = chr(ord(self.items[i])+int(alph[0]))
                    alph.append(alph[0])
                    alph.pop(0) 
                else:
                    self.items[i] = chr(ord(self.items[i])+int(alph[0])-90+64)
                    alph.append(alph[0])
                    alph.pop(0)
            
            elif ord(self.items[i]) >= 97 and ord(self.items[i]) <= 122:
                if ord(self.items[i])+int(alph[0]) <= 122:
                    self.items[i] = chr(ord(self.items[i])+int(alph[0]))
                    alph.append(alph[0])
                    alph.pop(0)  
                else:
                    self.items[i] = chr(ord((self.items[i]))+int(alph[0])-122+96)
                    alph.append(alph[0])
                    alph.pop(0)

    def deCodemsg(self,lst1,lst2):
        alph = lst2.copy()
        for i in range(len(self.items)):
            if ord(self.items[i]) >= 65 and ord(self.items[i]) <= 90:
                if ord(self.items[i])-int(alph[0]) >= 65:
                    self.items[i] = chr(ord(self.items[i])-int(alph[0]))
                    alph.append(alph[0])
                    alph.pop(0) 
                else:
                    self.items[i] = chr(ord(self.items[i])-int(alph[0])-65+91)
                    alph.append(alph[0])
                    alph.pop(0)
            
            elif ord(self.items[i]) >= 97 and ord(self.items[i]) <= 122:
                if ord(self.items[i])-int(alph[0]) >= 97:
                    self.items[i] = chr(ord(self.items[i])-int(alph[0]))
                    alph.append(alph[0])
                    alph.pop(0)  
                else:
                    self.items[i] = chr(ord((self.items[i]))-int(alph[0])-97+123)
                    alph.append(alph[0])
                    alph.pop(0)
            
        


inp = input('Enter String and Code : ').split(',')
x = inp[0].replace(' ','')
y = inp[1]
string = []
number = []
for i in range(len(x)):
    string.append(x[i])
for i in range(len(y)):
    number.append(y[i])
q = Queue()
q.enCodemsg(string,number)
print("Encode message is :  "+str(q.items))
q.deCodemsg(string,number)
print("Decode message is :  "+str(q.items))
