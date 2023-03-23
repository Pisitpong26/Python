def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
inp = input('Enter Number : ')
print('fibo({0}) = {1}'.format(inp,str(Fibonacci(int(inp)))))