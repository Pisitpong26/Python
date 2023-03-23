inp = input('Enter Input : ')
l = []
meta = 0
eqaul = 0
kata = 0
for i in inp:
    l.append(int(i))
for i in range(len(l)-1):
    if l[i] < l[i+1]: 
        meta += 1
    if l[i] == l[i+1]: 
        eqaul = 1
    if l[i] > l[i+1]: 
        kata += 1
if meta == len(l)-1:
    print("Metadrome")
elif meta > 0 and eqaul == 1 and kata == 0:
    print('Plaindrome')
elif kata == len(l)-1:
    print("Katadrome")
elif kata > 0 and eqaul == 1 and meta == 0:
    print('Nialpdrome')
elif eqaul == 1 and meta == 0 and kata == 0:
    print('Repdrome')
else:
    print('Nondrome')