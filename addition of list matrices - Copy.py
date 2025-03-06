n=int(input('enter'))
m=[]
a=[]
for i in range(n):
    l1=list(map(int,input().split()))
    m.append(l1)
for j in range(n):
    l2=list(map(int,input().split()))
    a.append(l2)
print(m)
print(a)
r=[]
for i in range(len(m)):
    s=[]
    for j in range(len(a)):
         k=m[i][j]+a[i][j]
         s.append(k)
    r.append(s)
print(r)
    
