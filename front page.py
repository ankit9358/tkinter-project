import mysql.connector
import tkinter
import test
import take_orders
import login
import customer_portal
from tkinter import ttk
con = mysql.connector.connect(host = 'localhost',database='project',user='root',password='Ankit@123')
cur=con.cursor()
win = tkinter.Tk()
win.title('Home')
win.geometry('2048x1536')



#################





###########

space_label=ttk.Label(win,text='                   ',font=("Times New Roman",20))
space_label.grid(row=0,column=0,sticky=tkinter.W)
space_label=ttk.Label(win,text='                   ',font=("Times New Roman",20))
space_label.grid(row=0,column=1,sticky=tkinter.W)
space_label=ttk.Label(win,text='                   ',font=("Times New Roman",20))
space_label.grid(row=0,column=2,sticky=tkinter.W)

space_label=ttk.Label(win,text='                       ',font=("Times New Roman",20))
space_label.grid(row=1,column=0,sticky=tkinter.W)
space_label=ttk.Label(win,text='                       ',font=("Times New Roman",20))
space_label.grid(row=1,column=1,sticky=tkinter.W)
space_label=ttk.Label(win,text='                       ',font=("Times New Roman",20))
space_label.grid(row=1,column=2,sticky=tkinter.W)

photo_home = tkinter.PhotoImage(file='home.png')
photo_home_label=ttk.Label(win, image=photo_home)
photo_home_label.grid( row=1 , column=3 ,sticky=tkinter.E)

#button_admin

photo_admin = tkinter.PhotoImage(file="Admin_icon.png")
photo_admin_label=ttk.Label(win, image=photo_admin)

x1=tkinter.Button(win)
x1.config(image=photo_admin,width="120",height="120",command=login.fun)
x1.grid(row=3,column=2)

admin_label=ttk.Label(win,text=' Admin Login',font=("Times New Roman",20))
admin_label.grid(row=4,column=2,sticky=tkinter.W)

#button_reservation

photo_res = tkinter.PhotoImage(file="res_icon.png")
photo_res_label=ttk.Label(win, image=photo_res)

x2=tkinter.Button(win)
x2.config(image=photo_res,width="120",height="120",command=customer_portal.add_customer)
x2.grid(row=3,column=3)

res_label=ttk.Label(win,text='     Table \nReservation',font=("Times New Roman",20))
res_label.grid(row=4,column=3)

#button_order

photo_order = tkinter.PhotoImage(file="order_icon.png")
photo_order_label=ttk.Label(win, image=photo_order)

x3=tkinter.Button(win)
x3.config(image=photo_order,width="120",height="120",command=take_orders.order)
x3.grid(row=3,column=4)

order_label=ttk.Label(win,text='    Order',font=("Times New Roman",20))
order_label.grid(row=4,column=4,sticky=tkinter.W)


