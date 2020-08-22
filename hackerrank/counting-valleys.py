input()
x=input()
lvl, c=0,0
for i in x:
    if i=="U":
        lvl+=1
    if i=="D":
        lvl-=1
    if lvl==0 and i=="U":
        c+=1
print(c)