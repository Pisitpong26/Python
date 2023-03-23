k, dayNum = input('Enter Input : ').split('/')
dayNum = [int(i) for i in dayNum.split()]
num = []
van = {}    
for i in range(int(k)):
    num.append(i + 1)           
    van[i+1] = van.get(i+1, 0) 
    
for i in range(len(dayNum)):
    minNum = num.pop(0)
    van[minNum] = van.get(minNum, 0) + int(dayNum[i])   
    print(f'Customer {i+1} Booking Van {minNum} | {dayNum[i]} day(s)')

    for index in range(len(num)):   
        if van[minNum] < van[num[index]] or (van[minNum] == van[num[index]] and minNum < num[index]):
            num.insert(index, minNum)
            minNum = None
            break

    if minNum is not None:  
        num.append(minNum) 