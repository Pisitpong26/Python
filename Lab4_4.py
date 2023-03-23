class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def match(self,lst):
        activity = ["Eat","Game","Learn","Movie"]
        location = ["Res.","ClassR.","SuperM.","Home"]
        x = lst.copy()
        for i in range(len(x)):
            j = x[i].split(':')
            self.items.append(j[0])
            self.items.append(j[1])
        
        while len(self.items):
            if len(self.items) > 2:
                print(str(activity[int(self.items.pop(0))])+":"+str(location[int(self.items.pop(0))]+','),end = ' ')
            else:
                print(str(activity[int(self.items.pop(0))])+":"+str(location[int(self.items.pop(0))]),end = ' ')

    def score(sel,my,your):
        x = my.copy()
        y = your.copy()
        me = []
        you = []
        score = 0
        for i in range(len(x)):
            k = x[i].split(':')
            me.append(int(k[0]))
            me.append(int(k[1]))
        for i in range(len(y)):
            k = y[i].split(':')
            you.append(int(k[0]))
            you.append(int(k[1]))
        while len(me) > 0:
            i = 0
            if me[i] == you[i] and me[i+1] == you[i+1]:
                score += 4
                me.pop(0)
                me.pop(0)
                you.pop(0)
                you.pop(0)
                
            elif me[i] != you[i] and me[i+1] == you[i+1]:
                score += 2
                me.pop(0)
                me.pop(0)
                you.pop(0)
                you.pop(0)

            elif me[i] == you[i] and me[i+1] != you[i+1]:
                score += 1
                me.pop(0)
                me.pop(0)
                you.pop(0)
                you.pop(0)

            else:
                score -= 5
                me.pop(0)
                me.pop(0)
                you.pop(0)
                you.pop(0)

        return score

inp =input("Enter Input : ").split(",")
j = inp
x = []
S = Queue()
T = Queue()
me = []
you = []
for i in range(len(j)):
    k = j[i].split()
    for l in range(len(k)):
        n = k[l].split()
        x.append(n[0])
for ele in range(len(x)):
    if ele % 2 == 0:
        me.append(x[ele]) 
    else:
        you.append(x[ele]) 

print("My   Queue =",end = ' ')
for i in range(len(me)):
    if len(me)-i >= 2:
        print(str(me[i])+',',end = ' ')
    else:
        print(str(me[i]),end = ' ')

print("\nYour Queue =",end = ' ')
for i in range(len(you)):
    if len(you)-i >= 2:
        print(str(you[i])+',',end = ' ')
    else:
        print(str(you[i]),end = ' ')

print("\nMy   Activity:Location =",end = ' ')
S.match(me)
print("\nYour Activity:Location =",end = ' ')
T.match(you)
score = S.score(me,you)
if score >= 7: 
    print("\nYes! You're my love! : Score is "+str(score)+'.')
elif score > 0 and score < 7:
    print("\nUmm.. It's complicated relationship! : Score is "+str(score)+'.')
else:
    print("\nNo! We're just friends. : Score is "+str(score)+'.')
    

