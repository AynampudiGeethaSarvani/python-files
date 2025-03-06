a=list(map(int,input().split(' ')))
for i in range(len(a)):
    if (a[i]==(a[i+1] and a[i+2])):
        print('yes')
else:
        print('no')
