def process(result,l,index = 0,mix = [],ele = []):
    if index >= len(l):
        return mix
    ele.append(l[index])
    if sum(ele) == result:
        mix.append(ele.copy())
    mix = process(result,l,index+1,mix,ele)
    ele.pop()
    mix = process(result,l,index+1,mix,ele)
    return mix
    
def bubble(l): 
    for last in range(len(l)-1, 0,-1):# จาก last ind ถึง ind 0 
        swaped = False
        for i in range(last): 
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i] #swap
                swaped = True
        
        if not swaped:
            break

    return l
                
def lenSort(l,index = 0):
    for last in range(len(l)-1, 0,-1):# จาก last ind ถึง ind 0 
        swaped = False
        for i in range(last): 
            if len(l[i]) > len(l[i+1]):
                l[i], l[i+1] = l[i+1], l[i] #swap
                swaped = True
        
        if not swaped:
            break

    return l



result,inp = input('Enter Input : ').split('/')
l = inp.split()
for i in range(len(l)):
    l[i] = int(l[i])
l = bubble(l)
viable_lst = process(int(result),l)
ans = lenSort(viable_lst)
if ans == []:
    print('No Subset')
else:
    for i in ans:
        print(i)
