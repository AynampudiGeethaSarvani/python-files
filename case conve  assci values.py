# merging list ,tuple and place ina dictionary
t=(1,2,3,4,5)
l=['a','b','c','d']

# add two lists in dictionary data
x=zip(t,l)
k=dict(x)
for x,y in k.items():
    print(x,y)
# string format method
print('%s'%(str))

# positional argument

print('{} and {} '.format('gee','sar'))
