class sample:
    x=10
    y=20
    def f(self):
        print(self.x,self.y)
a=sample()
a.f()
print(a.x)
print(sample.y)
