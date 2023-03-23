def bubble(l): 
    for last in range(len(l)-1, 0,-1):# จาก last ind ถึง ind 0 
        for i in range(last): 
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i] #swap

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "quick sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    newList = []
    x = []
    pos = 0
    median = 0
    for i in l:
        newList.append(i)
        x.append(i)
        bubble(x)
        if (len(x)+1)/2 % 1 > 0:
            pos = (len(x))/2
            pos = int(round(pos,0))
            median = (x[pos]+x[pos-1])/2
        else:
            pos = int((len(x))/2)
            median = x[pos]/1

        print('list = {0} : median = {1}'.format(newList,median))