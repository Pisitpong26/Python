class Calculator() :

    def __init__(self,number):
        self.number=number

    def __add__(self,x):

        return self.number + x.number

    def __sub__(self,x):

        return self.number - x.number

    def __mul__(self,x):

        return self.number * x.number

    def __truediv__(self,x):

        return self.number / x.number


x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep="\n")