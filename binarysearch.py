l=list(map(int,input().split()))
s=int(input('enter serch element'))
l.sort()
a=0
h=len(l)-1
c=0
while a<=h:
    m=(a+h)//2
    if s==l[m]:
        c=1
        break
    if s<l[m]:
        h=m-1
    elif s>l[m]:
        a=m+1
if c==1:
    print('found')
else:
    print('not found')
    
