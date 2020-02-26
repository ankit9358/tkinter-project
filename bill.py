from tkinter import *
from tkinter import ttk
import mysql.connector
con = mysql.connector.connect(host = 'localhost',database='project',user='root',password='Ankit@123')
cur=con.cursor()

def bl():
    win = Tk()
    win.title('BILL')
    #center allign
    width=win.winfo_screenwidth()
    height=win.winfo_screenheight()
    x=(width/2-550/2)
    y=(height/2-450/2)
    win.geometry("%dx%d+%d+%d"%(500,350,x,y))



    space_label=ttk.Label(win,text='            ',font=("Times New Roman",20))
    space_label.grid(row=0,column=2,sticky=W)
    space_label=ttk.Label(win,text='            ',font=("Times New Roman",20))
    space_label.grid(row=0,column=3,sticky=W)
    space_label=ttk.Label(win,text='            ',font=("Times New Roman",20))
    space_label.grid(row=0,column=4,sticky=W)


    cur.execute("select * from bill")
    row=cur.fetchall()
    tree = ttk.Treeview(win,height=10,columns=('item','price','quantity'))
    tree.grid(row=0,column=0)

    tree.heading("#0",text="Item")
    tree.column("#0",width=180)
    tree.heading("#1",text="Price per unit")
    tree.column("#1",width=80)
    tree.heading("#2",text="quantity")
    tree.column("#2",width=80)
    tree.heading("#3",text="sum")
    #tree.column("#1",width=120)

    for i in row:
        tree.insert('','end',text=i[0],values=(i[1],i[2],i[3]))
        tree.tag_configure('T',font='Arial 20')

    #cur.execute("select sum_ from bill")
    cur.execute("SELECT SUM(sum_) FROM bill")
    result = cur.fetchone()[0]
    #print(result)

    space_label=ttk.Label(win,text=' TOTAL AMOUNT = Rs '+str(result)+' /-',font=("Times New Roman",20))
    space_label.grid(row=1,column=0,sticky=W)
    cur.execute("Truncate table bill")
    con.commit()

    win.mainloop()


