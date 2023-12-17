 #viveksagar
print('TIK TAK TOE')
fpl=input('Enter player 1 name (*)')
spl=input('Enter player 2 name (0)')
a=['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ']
print(a[7],'|',a[8],'|',a[9],'|')
print(a[4],'|',a[5],'|',a[6],'|')
print(a[1],'|',a[2],'|',a[3],'|')
desc=fpl
f=[]
s=[]
for i in range(9):
    print(desc,' turn')
    c=int(input('Enter no from 1 to 9 = '))
    if(i%2==0):
        d='*'
        desc=spl
        f.append(c)
    else:
        d='0' 
        desc=fpl
        s.append(c)
    a[c]=d
    print(a[7],'|',a[8],'|',a[9],'|')
    print(a[4],'|',a[5],'|',a[6],'|')
    print(a[1],'|',a[2],'|',a[3],'|')
    if(a[1]=='*' and a[2]=='*' and a[3]=='*' or a[7]=='*' and a[8]=='*' and a[9]=='*'  or a[4]=='*' and a[5]=='*' and a[6]=='*'  or a[1]=='*' and a[4]=='*' and a[7]=='*' or a[2]=='*' and a[5]=='*' and a[8]=='*'  or a[3]=='*' and a[6]=='*' and a[9]=='*' or a[1]=='*' and a[5]=='*' and a[9]=='*' or a[3]=='*' and a[5]=='*' and a[7]=='*'):
        print(fpl,' wins')
        break
    elif(a[1]=='0' and a[2]=='0' and a[3]=='0' or a[7]=='0' and a[8]=='0' and a[9]=='0'  or a[4]=='0' and a[5]=='0' and a[6]=='0' or a[1]=='0' and a[4]=='0' and a[7]=='0' or a[2]=='0' and a[5]=='0' and a[8]=='0'  or a[3]=='0' and a[6]=='0' and a[9]=='0' or a[1]=='0' and a[5]=='0' and a[9]=='0' or a[3]=='0' and a[5]=='0' and a[7]=='0'):
        print(spl,' wins')
        break
    else:
        continue
print('Game Over')


