from tkinter import *
root=Tk()
root.title('check box control')
root.geomentry('400x400')
def display_checked():
    red=red_var.get()
    yellow=yellow_var.get()
    green=green_var.get()
    blue=blue_var.get()
    print("red:{}\nyellow:{}\ngreen:{}\nblue:{}".format(red,yellow,green,blue))
label=Label(root,text='which colors do you like below?'font=('arial',16)).grid(row=)
red_var=intvar()
checkbutton(root,width=10,text='red',variable=red_var,bg='red',font=('arial',14)).grid(row=1)
yellow_var=intvar()
checkbutton(root,width=10,text='yellow',variable=red_var,bg='yellow',font=('arial',14)).grid(row=2)
green_var=intvar()
checkbutton(root,width=10,text='green',variable=red_var,bg='green',font=('arial',14)).grid(row=3)
blue_var=intvar()
checkbutton(root,width=10,text='blue',variable=red_var,bg='blue',font=('arial',14)).grid(row=4)
Button(root,text='tally',command=display_checked,font=('arial',16)).grid(row=5)
Button(root,text='end',command=root.quit,font=('arial',16)).grid(row=6)
root.mainloop()       
        

        

        

        
