def num_grid(lst):
    for e in range(len(lst)):
        for i in range(len(lst[e])):
            if lst[e][i] == '-':
                lst[e][i] = 0

    for e in range(len(lst)):
        for i in range(len(lst[e])): 
            if lst[e][i] == '#':
                ###ตรงกลาง
                if e > 0 and e < 4 and i > 0 and i < 4:
                    if lst[e-1][i-1] != '#':
                        lst[e-1][i-1] += 1
                    if lst[e-1][i+1] != '#':
                        lst[e-1][i+1] += 1
                    if lst[e-1][i] != '#':
                        lst[e-1][i] += 1
                    if lst[e][i-1] != '#':
                        lst[e][i-1] += 1
                    if lst[e][i+1] != '#':
                        lst[e][i+1] += 1   
                    if lst[e+1][i] != '#':
                        lst[e+1][i] += 1
                    if lst[e+1][i+1] != '#':
                        lst[e+1][i+1] += 1
                    if lst[e+1][i-1] != '#':
                        lst[e+1][i-1] += 1
                
                
                ###ขอบบน
                elif e == 0:
                    ###มุมขวาบน
                    if e == 0 and i == 4:
                        if lst[e+1][i] != '#':
                            lst[e+1][i] += 1
                        if lst[e+1][i-1] != '#':
                            lst[e+1][i-1] += 1
                        if lst[e][i-1] != '#':
                            lst[e][i-1] += 1
                    ###มุมซ้ายบน        
                    elif e == 0 and i == 0:
                        if lst[e+1][i] != '#':
                            lst[e+1][i] += 1
                        if lst[e+1][i+1] != '#':
                            lst[e+1][i+1] += 1
                        if lst[e][i+1] != '#':
                            lst[e][i+1] += 1
                    ###ตรงกลาง        
                    elif e == 0 and i < 4:
                        if lst[e][i-1] != '#':
                            lst[e][i-1] += 1
                        if lst[e][i+1] != '#':
                            lst[e][i+1] += 1 
                        if lst[e+1][i] != '#':
                            lst[e+1][i] += 1
                        if lst[e+1][i+1] != '#':
                            lst[e+1][i+1] += 1
                        if lst[e+1][i-1] != '#':
                            lst[e+1][i-1] += 1 
   
                ###ขอบล่าง
                elif e == 4:
                    ###มุมซ้ายล่าง
                    if e == 4 and i == 0:
                        if lst[e-1][i+1] != '#':
                            lst[e-1][i+1] += 1
                        if lst[e-1][i] != '#':
                            lst[e-1][i] += 1
                        if lst[e][i+1] != '#':
                            lst[e][i+1] += 1
                    ###มุมขวาล่าง
                    elif e == 4 and i == 4:
                        if lst[e-1][i-1] != '#':
                            lst[e-1][i-1] += 1
                        if lst[e-1][i] != '#':
                            lst[e-1][i] += 1
                        if lst[e][i-1] != '#':
                            lst[e][i-1] += 1
                    ###ตรงกลาง
                    elif e == 4 and i < 4:
                        if lst[e][i-1] != '#':
                            lst[e][i-1] += 1
                        if lst[e][i+1] != '#':
                            lst[e][i+1] += 1
                        if lst[e-1][i-1] != '#':
                            lst[e-1][i-1] += 1
                        if lst[e-1][i+1] != '#':
                            lst[e-1][i+1] += 1
                        if lst[e-1][i] != '#':
                            lst[e-1][i] += 1  

                ###ขอบซ้าย
                elif i == 0 and e  < 4:
                    if lst[e-1][i+1] != '#':
                        lst[e-1][i+1] += 1
                    if lst[e-1][i] != '#':
                        lst[e-1][i] += 1
                    if lst[e][i+1] != '#':
                        lst[e][i+1] += 1  
                    if lst[e+1][i] != '#':
                        lst[e+1][i] += 1
                    if lst[e+1][i+1] != '#':
                        lst[e+1][i+1] += 1

                ###ขอบขวา
                elif i == 4 and e < 4:
                    if lst[e-1][i-1] != '#':
                        lst[e-1][i-1] += 1
                    if lst[e-1][i] != '#':
                        lst[e-1][i] += 1
                    if lst[e+1][i] != '#':
                        lst[e+1][i] += 1
                    if lst[e+1][i-1] != '#':
                        lst[e+1][i-1] += 1
                    if lst[e][i-1] != '#':
                        lst[e][i-1] += 1
            

 
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst[i][j] = str(lst[i][j])
 
    return lst



'''lst_input = [

    ["-","-","-","-","-"],

    ["-","-","-","-","-"],

    ["-","-","#","-","-"],

    ["-","-","-","-","-"],

    ["-","-","-","-","-"]

]'''

lst_input = []
print("*** Minesweeper ***")
input_list = input("Enter input(5x5) : ").split(",")

for e in input_list:

  lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")

print("\n",*num_grid(lst_input),sep = "\n")