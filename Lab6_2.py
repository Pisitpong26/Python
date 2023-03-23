def sort(n,x):
    if len(n) < 1:
        return x
    else:
        y = max(n)
        x.append(int(y))
        n.remove(y)
        return sort(n,x)

x = []
inp = [int(item) for item in input("Enter your List : ").split(',')]
print('List after Sorted : '+str(sort(inp,x)))