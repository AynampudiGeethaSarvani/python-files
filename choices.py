l1=[12,34,56,67]
while True:
    print('1.Add ')
    print('2.Insert position')
    print('3.remove position')
    print('4.remove element')
    print('5.display')
    print('6.Exit')
    print('eneter your choice')
    a=int(input())
    if a==1:
          b=int(input('enter'))
          l1.append(b)
          print(l1)

    elif a==2:
        c=int(input('enter positioin'))
        d=int(input('enter element'))
        l1.insert(c,d)
        print(l1)
    elif a==3:
        e=int(input('enter position'))
        l1.pop(e)
        print(e)
    elif a==4:
        f=int(input('enter elemn'))
        l1.remove(f)
        print(l1)
    elif a==5:
        print(l1)
    else:
        break
              
