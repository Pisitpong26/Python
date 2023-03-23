def sumPow(m,n):
    sum = 0                            
    if n >= len(m):            
        return 0
    sum += sumPow(m,2 * n + 1)     
    sum += sumPow(m,2 * n + 2)    
    return m[n] + sum

knightPow, knightGroup = input('Enter Input : ').split('/')
knightPow = [int(i) for i in knightPow.split()]
knightGroup = knightGroup.split(',')

print(sumPow(knightPow,0))                

for i in knightGroup:
    i = i.split()
    sum1 = sumPow(knightPow,int(i[0]))          
    sum2 = sumPow(knightPow,int(i[1]))         

    if sum1 > sum2:
        print('{0}>{1}'.format(i[0],i[1]))
    elif sum1 < sum2:
        print('{0}<{1}'.format(i[0],i[1]))
    else:
        print('{0}={1}'.format(i[0],i[1]))