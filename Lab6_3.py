def pow(x,y):
    if y == 1:
        return x
    elif y == 0:
        return 1
    else:
        return x*pow(x,y-1)

x,y = input('Enter Input a b : ').split()
print(pow(int(x),int(y)))