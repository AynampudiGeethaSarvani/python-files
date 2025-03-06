sname=input('stu name')
total=0
count=0
print('sub marks(marks<=100):')
while (count<3):
    marks=int(input())
    if marks >100:
        continue
    total=total+marks
    count=count+1
print(sname)
print(total)
