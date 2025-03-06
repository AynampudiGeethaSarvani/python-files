def analyse_string(s):
    al=l=u=spe=spa=di=0
    for i in s:
        if i.isalpha():
            al=al+1
        if  i.islower():
            l=l+1
        if i.isupper():
            u=u+1
        if i.isdigit():
            d=d+1
        if i.isspace():
            sp=sp+1
    return al,l,u,d,sp
string=input('enter')
print(analyse_string(string))
                    
        
        
    

