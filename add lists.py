s1=list(map(int,input().split()))
s2=list(map(int,input().split()))
k=[]
i=0
j=0
while i<len(s1) or j<len(s2):           
    s=0
    if i<len(s1):
        s=s+s1[i]
        i=i+1
    if j<len(s2):
        s=s+s2[j]
        j=j+1
    k.append(s)
print(k)   
