print('*** Election ***')
people = int(input('Enter a number of voter(s) : '))
number = input().split()
total = list(map(int,number))
a = len(total)

duplicateNum=[]

if (max(total)<=0):
    print('*** No Candidate Wins ***')
    exit()



for i in range(1,20):
    count=0
    for j in range(len(total)):
        if i == total[j]:
            count+=1
    duplicateNum.append(count)
    #print(str(i)+' dupes'+str(count))
#print(duplicateNum)

for x in range(len(duplicateNum)):
    for y in range(x+1,len(duplicateNum)):
        if duplicateNum[x]==duplicateNum[y] and duplicateNum[x]==max(duplicateNum):
            print('*** No Candidate Wins ***')
            exit()

#print(total)
#print(duplicateNum)

for i in range(len(duplicateNum)):
    if duplicateNum[i] == max(duplicateNum):
        print(i+1)