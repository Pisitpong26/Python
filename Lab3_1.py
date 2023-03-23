x = input("Enter Input : ").split(",")
stack = []
a = []
mix = list(map(str,x))

for i in range(len(mix)):
    if mix[i][0] == 'A':
        a = mix[i].split()
        stack.append(int(a[1]))
        print("Add = {}".format(stack[len(stack)-1]),"and Size = {}".format(len(stack)))
        a = []
    elif mix[i][0] == 'P':
        if (len(stack) == 0):
            print("-1")
        else:
            print("Pop = {}".format(stack.pop()),"and Index = {}".format(len(stack)))

    if i+1 == len(mix):
        print("Value in Stack =",end =" ")
        if len(stack) > 0:
            for i in range(len(stack)):
                print(stack[i],end =" ")
            print("".format(stack))
        else :
            print("Empty",end =" ")


        
        

