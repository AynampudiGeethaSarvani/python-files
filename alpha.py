a=input('enter ')
if a>='A' and a<='Z':
    while a<='Z':
        print(a,end=' ')
        k=ord(a)+1
        a=chr(k)
elif a>='a' and a<='z':
    while a<='z':
        print(a,end='')
        k=ord(a)+1
        a=chr(k)
    
