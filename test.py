import mysql.connector
import tkinter
import add_emp
import check_emp
import check_res
import admin_add_item
from tkinter import ttk
con = mysql.connector.connect(host = 'localhost',database='project',user='root',password='Ankit@123')
cur=con.cursor()
def admin_p():
    win = tkinter.Tk()
    win.title('Admin Portal')
    win.geometry('2048x1536')

    space_label=ttk.Label(win,text='                   ',font=("Times New Roman",20))
    space_label.grid(row=0,column=0,sticky=tkinter.W)
    space_label=ttk.Label(win,text='                   ',font=("Times New Roman",20))
    space_label.grid(row=0,column=1,sticky=tkinter.W)
    space_label=ttk.Label(win,text='                       ',font=("Times New Roman",20))
    space_label.grid(row=0,column=2,sticky=tkinter.W)

    space_label=ttk.Label(win,text='                         ',font=("Times New Roman",20))
    space_label.grid(row=1,column=0,sticky=tkinter.W)
    space_label=ttk.Label(win,text='                         ',font=("Times New Roman",20))
    space_label.grid(row=1,column=1,sticky=tkinter.W)
    space_label=ttk.Label(win,text='                         ',font=("Times New Roman",20))
    space_label.grid(row=1,column=2,sticky=tkinter.W)

    space_label=ttk.Label(win,text='ADMIN PORTAL',font=("Times New Roman",30),foreground="blue")
    space_label.grid(row=1,column=3,sticky=tkinter.W)

    space_label=ttk.Label(win,text='                        ',font=("Times New Roman",20))
    space_label.grid(row=2,column=2,sticky=tkinter.W)
    space_label=ttk.Label(win,text='                         ',font=("Times New Roman",20))
    space_label.grid(row=3,column=2,sticky=tkinter.W)


    #button_check_reservation


    x2=tkinter.Button(win)
    x2.config(text='Check \nReservation',width="12",height="4",font=("Comic Sans MS",15),foreground='red',command=check_res.check_r)
    x2.grid(row=3,column=3)

    ##res_label=ttk.Label(win,text='    Check \nReservation',font=("Times New Roman",15))
    ##res_label.grid(row=4,column=3)


    space_label=ttk.Label(win,text='                         ',font=("Times New Roman",20))
    space_label.grid(row=4,column=2,sticky=tkinter.W)
    space_label=ttk.Label(win,text='                         ',font=("Times New Roman",20))
    space_label.grid(row=4,column=2,sticky=tkinter.W)

    #button_add_emp


    x3=tkinter.Button(win)
    x3.config(text='Add \nEmploye',width="12",height="4",font=("Comic Sans MS",15),foreground='red',command=add_emp.add_e)
    x3.grid(row=5,column=2)

    ##order_label=ttk.Label(win,text='   Add \nEmploye',font=("Times New Roman",15))
    ##order_label.grid(row=6,column=2)

    #button_check_emp


    x3=tkinter.Button(win)
    x3.config(text='Check \nEmployes',width="12",height="4",font=("Comic Sans MS",15),foreground='red',command=check_emp.check_e)
    x3.grid(row=5,column=3)

    ##order_label=ttk.Label(win,text='   Check \nEmployes',font=("Times New Roman",15))
    ##order_label.grid(row=6,column=3)

    #button_add_item


    x1=tkinter.Button(win)
    x1.config(text='Add \n Item',width="12",height="4",font=("Comic Sans MS",15),foreground='red',command=admin_add_item.add_i)
    x1.grid(row=5,column=4)

    ##admin_label=ttk.Label(win,text=' Add \n Item',font=("Times New Roman",15))
    ##admin_label.grid(row=6,column=4)

    #button_change_pwd



    win.mainloop()

