
def staircase(m,n):
    if n > 0:
        print('_'*(n-1)+'#'*(m))
        staircase(m+1,n-1)
    
    elif n < 0:
        print('_'*(m)+'#'*(n*-1))
        staircase(m+1,n+1)

inp = int(input("Enter Input : "))
if inp > 0:
    staircase(1,inp)
elif inp < 0:
    staircase(0,inp)
else:
    print('Not Draw!')