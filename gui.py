



from tkinter import*
root = Tk()
root.geometry('900x600')
root.title("COVID-19")

def submit():
      pass

def cls():
      entry_1.delete(0,END)
      entry_2.delete(0,END)
      entry_3.delete(0,END)
      entry_4.delete(0,END)
      entry_5.delete(0,END)
      entry_6.delete(0,END)

def update():
      pass





label_0 = Label(root, text="COVID-19 Data",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

#--------------------------------------------------------------------------------------------
label_1 = Label(root, text="STATE",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,width=60,font='15')
entry_1.place(x=240,y=130)
#-------------------------------------------------------------------------------------------------
label_2 = Label(root, text="TIME",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,width=60,font='15')
entry_2.place(x=240,y=180)
#-----------------------------------------------------------------------------------------------------
label_3 = Label(root, text="CONFIRMED",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

entry_3= Entry(root,width=60,font='15')
entry_3.place(x=240,y=230)
#----------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
label_4 = Label(root, text="RECOVERED",width=20,font=("bold", 10))
label_4.place(x=80,y=280)

entry_4 = Entry(root,width=60,font='15')
entry_4.place(x=240,y=280)
#-------------------------------------------------------------------------------------------------
label_5 = Label(root, text="DEATHS",width=20,font=("bold", 10))
label_5.place(x=68,y=330)

entry_5 = Entry(root,width=60,font='15')
entry_5.place(x=240,y=330)
#------------------------------------------------------------------------------------------------------------------------------------
label_6 = Label(root, text="ACTIVE",width=20,font=("bold", 10))
label_6.place(x=70,y=380)

entry_6= Entry(root,width=60,font='15')
entry_6.place(x=240,y=380)
#--------------------------------------------------------------------------------------------------------------------------------------

Button(root, text='Submit',command=submit,width=20,bd=5,bg='brown',fg='white').place(x=180,y=480)

Button(root, text='clear',command=cls,width=20,bd=5,bg='brown',fg='white').place(x=380,y=480)

Button(root, text='Update',command=update,width=20,bd=5,bg='brown',fg='white').place(x=580,y=480)

root.mainloop()

