a=int(input('enter'))
c=0
b=a
d=a
s=0
while a>0:
    a=a//10
    c=c+1
while b>0:
    r=b%10
    s=s+r**c
    b=b//10
if s==d:
    print('amstrong no')
else:
    print('not an amstrong')



