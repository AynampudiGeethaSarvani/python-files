a=int(input('enter date'))
b=int(input('enter month'))
c=int(input('enter year'))
d=int(input('enter no of students'))
s=a+b+c
if((s%12==0) and (d>50 and d<100)):
    print('cinema day')
else:
    print('not a cinema day')
    
            
