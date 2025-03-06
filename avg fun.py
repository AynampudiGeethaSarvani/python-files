def avg(x,y,z):
    return x+y+z/3
a=int(input('enter'))
b=int(input('enter'))
c=int(input('enter'))
k=avg(a,b,c)%3
print(k)
print(avg(100,200,300)/3)
