s=input()
s=''.join(sorted(s))
c=''
d=''
for i in s:
    if i.isalpha():
        d=d+i
    elif  i.isdigit():
        c=c+i
print(d+c)
    

    
    
