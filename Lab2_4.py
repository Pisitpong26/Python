from re import L


def hbd(age):

    x = 0
    y = 0
    if age % 2 == 0:
        x = int(age/2)
        y = 20
    else :
        x = int((age-1)/2)
        y = 21
    return "saimai is just " + str(y) +", in base " + str(x)+"!"

year = input("Enter year : ")

print(hbd(int(year)))