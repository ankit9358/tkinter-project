import mysql.connector
import tkinter
from tkinter import *
import test 
from tkinter import ttk
con = mysql.connector.connect(host = 'localhost',database='project',user='root',password='Ankit@123')
cur=con.cursor()
def fun():
    win = tkinter.Tk()
    win.title('Login')
    width=win.winfo_screenwidth()
    height=win.winfo_screenheight()
    x=(width/2-650/2)
    y=(height/2-200/2)
    win.geometry("%dx%d+%d+%d"%(650,200,x,y))
    query="SELECT * FROM login"
    cur.execute(query)
    row=cur.fetchone()

    def action():
        Enter_ID=login_item.get()
        Enter_PASS=pass_item.get()
        if((Enter_ID==row[0])&(Enter_PASS==row[1])):
            
            win.destroy()
            test.admin_p()
        else:
            space_label=ttk.Label(win,text='              Wrong Credentials',font=("Times New Roman",10),foreground="red")
            space_label.grid(row=6,column=2,sticky=tkinter.W)
            
            
        


    space_label=ttk.Label(win,text='                   ',font=("Times New Roman",20))
    space_label.grid(row=0,column=0,sticky=tkinter.W)
    space_label=ttk.Label(win,text='                   ',font=("Times New Roman",20))
    space_label.grid(row=0,column=1,sticky=tkinter.W)
    space_label=ttk.Label(win,text='                 ',font=("Times New Roman",20))
    space_label.grid(row=0,column=2,sticky=tkinter.W)


    mob_label=ttk.Label(win,text='LOGIN ID :',font=("Times New Roman",20))
    mob_label.grid(row=2,column=1,sticky=tkinter.W)
    login_item=tkinter.StringVar(win)
    login_item_entrybox=ttk.Entry(win,width=30,textvariable=login_item)
    login_item_entrybox.grid(row=2,column=2,sticky=tkinter.W)


    mob_label=ttk.Label(win,text='PASSWORD :',font=("Times New Roman",20))
    mob_label.grid(row=3,column=1,sticky=tkinter.W)
    pass_item=tkinter.StringVar(win)
    pass_item_entrybox=ttk.Entry(win,show='*',width=30,textvariable=pass_item)
    pass_item_entrybox.grid(row=3,column=2,sticky=tkinter.W)


    submit_button=ttk.Button(win,text='Submit',command=action)
    submit_button.grid(row=4 , column=2)





    win.mainloop()
            
        

