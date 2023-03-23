def bubble(l,z): 
    for last in range(len(l)-1, 0,-1):# จาก last ind ถึง ind 0 
        swaped = False
        x = 'None'
        for i in range(last): 
            if l[i] > l[i+1]:
                x = l[i]
                l[i], l[i+1] = l[i+1], l[i] #swap
                swaped = True
        z += 1
        if swaped:
            if z == len(l)-1:
                print('last step : {0} move[{1}]'.format(l,x))
            else:
                print('{0} step : {1} move[{2}]'.format(z,l,x))
                
        else:
            print('last step : {0} move[{1}]'.format(l,x))
                
        if not swaped:
            break
            
l = [int(i) for i in input('Enter Input : ').split()]
bubble(l,0)
