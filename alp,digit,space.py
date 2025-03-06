s=input()
if s.isalpha():
    print('alphabet')
    if s.isupper():
        print('upper')
    else:
        print('lower')
elif s.isdigit():
    print('digit')
elif s.isspace():
    print('space')
else:
    print('special char')
    


    
