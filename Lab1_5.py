from operator import le


price = input("Enter All Bid : ").split()
total = list(map(int,price))
total.sort()
numlist = len(total)
num = numlist - 2
check = 0

if total[num] == total[numlist-1]:
    check = 1

if numlist == 1:
    print("not enough bidder")
elif check == 1:
    print("error : have more than one highest bid")
else:
    print("winner bid is",max(total),"need to pay",total[num])
