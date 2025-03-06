a=list(map(int,input('enter').split()))
f=0
k=int(input('enter'))
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            if abs(i-j)<=k:
                f=1
if f==0:
    print("False")
else:
    print("True")
        
            
            
