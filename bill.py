a=int(input('enter units'))
if(a<=200):
    print(a*0.5)
elif(a<=400):
    print(a*0.65+100)
elif(a<=600):
    print(a*0.80+200)
elif(a>=600):
    print(a*1.25+425)


