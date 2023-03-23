def minimumWeight(lists, box):
    L = []

    if box == 1:
        return sum(lists)

    for i in range(len(lists)):
        if len(lists[i:]) < box - 1:
            break

        thisBox = sum(lists[:i])
        otherBox = minimumWeight(lists[i:], box - 1)
        L.append(max(thisBox, otherBox))
        minWeight = min(L)
    return minWeight

lists, numOfBox = input("Enter Input : ").split('/')
numOfBox = int(numOfBox)
weightLists = [int(i) for i in lists.split()]
print("Minimum weigth for {0} box(es) = {1}".format(numOfBox,minimumWeight(weightLists,numOfBox)))