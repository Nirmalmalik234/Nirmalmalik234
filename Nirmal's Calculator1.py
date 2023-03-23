#!/usr/bin/env python
# coding: utf-8

# In[14]:


from tkinter import *
def buttonClick(number):
    global val
    val=val+str(number)
    data.set(val)
    
def buttonClear():
    global val
    val=""
    data.set("")

def buttonEquals():
    global val
    result=str(eval(val))
    data.set(result)
    
root=Tk()
root.title("Nirmal's Calculator")
root.geometry("361x381+500+200")
val=""
data=StringVar()
display=Entry(root,textvariable=data,bd=29,justify="right",bg="powder blue",font=("ariel",20))
display.grid(row=0,columnspan=4)
button7=Button(root,text="7",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:buttonClick(7))
button7.grid(row=1,column=0)
button8=Button(root,text="8",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:buttonClick(8))
button8.grid(row=1,column=1)
button9=Button(root,text="9",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:buttonClick(9))
button9.grid(row=1,column=2)
button_Plus=Button(root,text="+",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:buttonClick('+'))
button_Plus.grid(row=1,column=3)


button4=Button(root,text="4",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:buttonClick(4))
button4.grid(row=2,column=0)
button5=Button(root,text="5",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:buttonClick(5))
button5.grid(row=2,column=1)
button6=Button(root,text="6",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:buttonClick(6))
button6.grid(row=2,column=2)
button_Sub=Button(root,text="-",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:buttonClick('-'))
button_Sub.grid(row=2,column=3)

button1=Button(root,text="1",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:buttonClick(1))
button1.grid(row=3,column=0)
button2=Button(root,text="2",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:buttonClick(2))
button2.grid(row=3,column=1)
button3=Button(root,text="3",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:buttonClick(3))
button3.grid(row=3,column=2)
button_Mul=Button(root,text="X",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:buttonClick('*'))
button_Mul.grid(row=3,column=3)


button_Clear=Button(root,text="C",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=buttonClear)
button_Clear.grid(row=4,column=0)
button_Zero=Button(root,text="0",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:buttonClick(0))
button_Zero.grid(row=4,column=1)
button_Div=Button(root,text="÷",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:buttonClick('/'))
button_Div.grid(row=4,column=2)
button_Equals=Button(root,text="=",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=buttonEquals)
button_Equals.grid(row=4,column=3)
root.mainloop()


# In[ ]:




