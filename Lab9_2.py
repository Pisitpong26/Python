def selection(l,i,biggest):
    if i > 0:
        if l[i-1] > biggest:
            biggest = l[i-1]
        return selection(l,i-1,biggest)
            
    return biggest

def index(l,x,i):
    if i < len(l):
        if x == l[i]:
            return i
        else:
            return index(l,x,i+1)

def StraightSelectionSort(i,l,d):
    last = len(l)-d
    if last > 0:
        if l[last] != l[i]:
            l[last],l[i] = l[i],l[last]
            print('swap {0} <-> {1} : {2}'.format(l[i],l[last],l))
            x = selection(l,len(l)-(d+1),l[len(l)-(d+1)])
            i = index(l,x,0)
            return StraightSelectionSort(i,l,d+1)
        else:   
            x = selection(l,len(l)-(d+1),l[len(l)-(d+1)])
            i = index(l,x,0)
            return StraightSelectionSort(i,l,d+1)

l = [int(i) for i in input("Enter Input : ").split()]
StraightSelectionSort(index(l,selection(l,len(l)-1,l[len(l)-1]),0),l,1)
print(l)
