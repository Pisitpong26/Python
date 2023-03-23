def pantip(k, n, arr, path):
    if sum(path) == k:
            print(" ".join(map(str,path)))
            path.clear()
            return 1
    elif len(arr) == 0 or sum(path) > k:
        return 0
    else :
        newN = n
        path1 = path+[]
        path2 = path+[]
        arr_1 = arr+[]
        arr_2 = arr+[]
        path1.append(arr_1[0])
        n += arr_1[0]
        arr_1.pop(0)
        arr_2.pop(0)
        return pantip(k, n, arr_1, path1) + pantip(k, newN, arr_2, path2)

inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))