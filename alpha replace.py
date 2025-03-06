s=input()
d=''
for i in s:
    if i.islower():
        d=d+chr(97+122-ord(i))
    elif i.isupper():
        d=d+chr(65+90-ord(i))
print(d)
