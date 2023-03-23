x =input("Enter expresion : ")
open = '([{'
close = ')]}'
mix = []
er = 0
for i in range(len(x)): 
    e = x[i]
    if e in '([{':
        mix.append(e)
    else:
        if e in ')]}':
            if len(mix) > 0:
                if not open.index(mix.pop()) == close.index(e):
                    er = 1 #not match
            elif len(mix) == 0 and er == 0:
                er = 2 # no open paren
if len(mix) > 0:
    er = 3 #open paren(s) excesses
if er == 1:
    print(x,'Unmatch open-close')
elif er == 2:
    print(x,'close paren excess')
elif er == 3:
    print(x,'open paren excess  ',len(mix),': ',end ='')
    for e in mix:
        print(e,sep = ' ',end='')
    print()
else:
    print(x,'MATCH')


            
