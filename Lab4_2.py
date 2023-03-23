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

    def move(self,lst,min):
        cashier_1 = []
        cashier_2 = []
        for i in range(len(lst)):
            self.items.append(lst[i])
        for i in range(1,min+1):
                
            if i > 1 and (i-1) % 3 == 0 and len(cashier_1) > 0: #เมื่อผ่านไป 3 นาที ให้หัวแถวออกจากคิว
                cashier_1.pop(0)

            if len(cashier_2) > 0 and i % 2 == 0: #ถ้าแคชเชียร์ 2 มีคิว และเวลาผ่านไป 2 นาที ให้หัวแถวออกจากคิว
                cashier_2.pop(0)

            if len(cashier_1) < 5 and len(self.items) > 0: #เช็คว่าแคชเชียร์ 1 เต็มรึยัง
                cashier_1.append(self.items.pop(0))

            elif len(cashier_1) == 5 and len(self.items) > 0: #ถ้าแคชเชียร์ 1 เต็มให้ไปต่อแคชเชียร์ 2 
                cashier_2.append(self.items.pop(0))


            print(i,self.items,cashier_1,cashier_2)

inp = input("Enter people and time : ")
x = inp.split()
S = Queue()
S.move(x[0],int(x[1]))