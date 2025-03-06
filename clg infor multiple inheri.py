class cse:
    cname=branches=''
    fee=0
    def f1(self,cname,branches,fee):
        self.cname=cname
        self.branches=branches
        self.fee=fee
    def display1(self):
        print(self.cname)
        print(self.branches)
        print(self.fee)
class ece:
    cname=branches=''
    fee=0
    def f2(self,cname1,branches1,fee1):
        self.cname1=cname1
        self.branches1=branches1
        self.fee1=fee1
    def display2(self):
        print(self.cname1)
        print(self.branches1)
        print(self.fee1)
class civil:
    cname=branches=''
    fee=0
    def f3(self,cname2,branches2,fee2):
        self.cname2=cname2
        self.branches2=branches2
        self.fee2=fee2
    def display3(self):
        print(self.cname2)
        print(self.branches2)
        print(self.fee2)
class college(cse,ece,civil):
    cnames=univ=''
    def f4(self):
        self.cnames=cnames
        self.univ=univ
    def display(self):
        print(self.cnames)
        print(self.univ)
        self.display1()
        self.display2()
        self.display3()
b=college()
b.f1('cse','ai,ds',24000)
b.f2('ece','it',45000)
b.f3('civil','no',35000)
b.f4=('chebrolu','jntuk')
b.display()









        
        
    
