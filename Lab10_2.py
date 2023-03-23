def moreThan(comp,l,i=0,greaterVal = []):
    if i == len(comp):
        return greaterVal

    for j in range(len(l)):
        x = len(comp)
        if len(comp) > 0:
            if comp[i] < l[j]:
                greaterVal.append(l[j])
                comp.pop(0)
            if j == len(l)-1 and len(comp) == x:
                greaterVal.append('No First Greater Value')

        else:
            return greaterVal

    return moreThan(comp,l,i+1,greaterVal)

l,comp = input('Enter Input : ').split('/')
l = [int(i) for i in l.split()]
comp = [int(i) for i in comp.split()]
l.sort()
comp.sort()
ans = moreThan(comp,l)
if ans == []:
   print('No First Greater Value')
else:
    for i in ans:
        print(i)


                
