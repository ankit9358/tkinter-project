from tkinter import *
from tkinter import ttk
import mysql.connector
con = mysql.connector.connect(host = 'localhost',database='project',user='root',password='Ankit@123')
cur=con.cursor()
def order():
    win = Tk()
    win.title('Order')
    #center allign
    width=win.winfo_screenwidth()
    height=win.winfo_screenheight()
    x=(width/2-950/2)
    y=(height/2-450/2)
    win.geometry("%dx%d+%d+%d"%(900,350,x,y))
    def action():
        q1=Q1_var.get()
        q2=Q2_var.get()
        q3=Q3_var.get()
        q4=Q4_var.get()
        q5=Q5_var.get()
        q6=Q6_var.get()
        q7=Q7_var.get()
        i1=item1_var.get()
        i2=item2_var.get()
        i3=item3_var.get()
        i4=item4_var.get()
        i5=item5_var.get()
        i6=item6_var.get()
        i7=item7_var.get()
        total=0
        if(q1!=0):
            query="SELECT price FROM menu WHERE item = %s"
            cur.execute(query,(i1,))
            row1=cur.fetchone()
            total=total+row1[0]*q1
            q1_label=ttk.Label(win,text=i1+" - "+str(q1),font=("Times New Roman",20))
            q1_label.grid( row=16, column=4, sticky=W)
        if(q2!=0):
            query="SELECT price FROM menu WHERE item = %s"
            cur.execute(query,(i2,))
            row2=cur.fetchone()
            total=total+row2[0]*q2
            q1_label=ttk.Label(win,text=i2+" - "+str(q2),font=("Times New Roman",20))
            q1_label.grid( row=17, column=4, sticky=W)
        if(q3!=0):
            query="SELECT price FROM menu WHERE item = %s"
            cur.execute(query,(i3,))
            row3=cur.fetchone()
            total=total+row3[0]*q3
            q3_label=ttk.Label(win,text=i3+" - "+str(q3),font=("Times New Roman",20))
            q3_label.grid( row=18, column=4, sticky=W)
        if(q4!=0):
            query="SELECT price FROM menu WHERE item = %s"
            cur.execute(query,(i4,))
            row4=cur.fetchone()
            total=total+row4[0]*q4
            q4_label=ttk.Label(win,text=i4+" - "+str(q4),font=("Times New Roman",20))
            q4_label.grid( row=19, column=4, sticky=W)
        if(q5!=0):
            query="SELECT price FROM menu WHERE item = %s"
            cur.execute(query,(i5,))
            row5=cur.fetchone()
            total=total+row5[0]*q5
            q5_label=ttk.Label(win,text=i5+" - "+str(q5),font=("Times New Roman",20))
            q5_label.grid( row=20, column=4, sticky=W)
        if(q6!=0):
            query="SELECT price FROM menu WHERE item = %s"
            cur.execute(query,(i6,))
            row6=cur.fetchone()
            total=total+row6[0]*q6
            q6_label=ttk.Label(win,text=i6+" - "+str(q6),font=("Times New Roman",20))
            q6_label.grid( row=21, column=4, sticky=W)
        if(q7!=0):
            query="SELECT price FROM menu WHERE item = %s"
            cur.execute(query,(i7,))
            row7=cur.fetchone()
            total=total+row7[0]*q7
            q7_label=ttk.Label(win,text=i7+" - "+str(q7),font=("Times New Roman",20))
            q7_label.grid( row=22, column=4, sticky=W)
        ##print(total)
        bill_label=ttk.Label(win,text=' TOTAL AMOUNT = Rs '+str(total),font=("Times New Roman",20))
        bill_label.grid( row=20, column=8, sticky=W)

        
            


    space_label=ttk.Label(win,text='        ',font=("Times New Roman",20))
    space_label.grid(row=0,column=0,sticky=W)
    space_label=ttk.Label(win,text='        ',font=("Times New Roman",20))
    space_label.grid(row=0,column=1,sticky=W)
    '''space_label=ttk.Label(win,text='            ',font=("Times New Roman",20))
    space_label.grid(row=0,column=2,sticky=W)
    space_label=ttk.Label(win,text='            ',font=("Times New Roman",20))
    space_label.grid(row=0,column=3,sticky=W)
    space_label=ttk.Label(win,text='            ',font=("Times New Roman",20))
    space_label.grid(row=0,column=4,sticky=W)'''


    '''cur.execute("select * from menu")
    row=cur.fetchall()
    tree = ttk.Treeview(win,height=30,columns=('item'))
    tree.grid(row=0,column=0)

    tree.heading("#0",text="Item")
    tree.column("#0",width=180)
    tree.heading("#1",text="Price")
    #tree.column("#1",width=120)

    for i in row:
        tree.insert('','end',text=i[0],values=(i[1]))
        tree.tag_configure('T',font='Arial 20')'''

    #
    item1_label=ttk.Label(win,text='Enter First Item ',font=("Times New Roman",20))
    item1_label.grid( row=0, column=2, sticky=W)

    cur.execute("select item from menu")
    item = cur.fetchall()

    item1_var=StringVar(win)
    item1_combobox=ttk.Combobox(win, width=25 , textvariable=item1_var, state='readonly')
    item1_combobox['values']=(item)
    item1_combobox.grid(row=0, column=3,sticky=E)

    #
    item2_label=ttk.Label(win,text='Enter Second Item ',font=("Times New Roman",20))
    item2_label.grid( row=2, column=2, sticky=W)

    item2_var=StringVar(win)
    item2_combobox=ttk.Combobox(win, width=25 , textvariable=item2_var, state='readonly')
    item2_combobox['values']=(item)
    item2_combobox.grid(row=2, column=3,sticky=E)

    #
    item3_label=ttk.Label(win,text='Enter Third Item ',font=("Times New Roman",20))
    item3_label.grid( row=4, column=2, sticky=W)

    item3_var=StringVar(win)
    item3_combobox=ttk.Combobox(win, width=25 , textvariable=item3_var, state='readonly')
    item3_combobox['values']=(item)
    item3_combobox.grid(row=4, column=3,sticky=E)

    #
    item4_label=ttk.Label(win,text='Enter Fourth Item ',font=("Times New Roman",20))
    item4_label.grid( row=6, column=2, sticky=W)

    item4_var=StringVar(win)
    item4_combobox=ttk.Combobox(win, width=25 , textvariable=item4_var, state='readonly')
    item4_combobox['values']=(item)
    item4_combobox.grid(row=6, column=3,sticky=E)

    #
    item5_label=ttk.Label(win,text='Enter Fifth Item ',font=("Times New Roman",20))
    item5_label.grid( row=8, column=2, sticky=W)

    item5_var=StringVar(win)
    item5_combobox=ttk.Combobox(win, width=25 , textvariable=item5_var, state='readonly')
    item5_combobox['values']=(item)
    item5_combobox.grid(row=8, column=3,sticky=E)

    #
    item6_label=ttk.Label(win,text='Enter Sixth Item ',font=("Times New Roman",20))
    item6_label.grid( row=10, column=2, sticky=W)

    item6_var=StringVar(win)
    item6_combobox=ttk.Combobox(win, width=25 , textvariable=item6_var, state='readonly')
    item6_combobox['values']=(item)
    item6_combobox.grid(row=10, column=3,sticky=E)

    #
    item7_label=ttk.Label(win,text='Enter Seventh Item ',font=("Times New Roman",20))
    item7_label.grid( row=12, column=2, sticky=W)

    item7_var=StringVar(win)
    item7_combobox=ttk.Combobox(win, width=25 , textvariable=item7_var, state='readonly')
    item7_combobox['values']=(item)
    item7_combobox.grid(row=12, column=3,sticky=E)


    ###
    #quantity
    ###

    Q1_label=ttk.Label(win,text=' Quantity ',font=("Times New Roman",20))
    Q1_label.grid( row=0, column=4, sticky=W)
    Q1_var=IntVar(win)
    Q1_entrybox=ttk.Entry(win,width=20,textvariable=Q1_var)
    Q1_entrybox.grid(row=0,column=5)
    #
    Q2_label=ttk.Label(win,text=' Quantity ',font=("Times New Roman",20))
    Q2_label.grid( row=2, column=4, sticky=W)
    Q2_var=IntVar(win)
    Q2_entrybox=ttk.Entry(win,width=20,textvariable=Q2_var)
    Q2_entrybox.grid(row=2,column=5)
    #
    Q3_label=ttk.Label(win,text=' Quantity ',font=("Times New Roman",20))
    Q3_label.grid( row=4, column=4, sticky=W)
    Q3_var=IntVar(win)
    Q3_entrybox=ttk.Entry(win,width=20,textvariable=Q3_var)
    Q3_entrybox.grid(row=4,column=5)
    #
    Q4_label=ttk.Label(win,text=' Quantity ',font=("Times New Roman",20))
    Q4_label.grid( row=6, column=4, sticky=W)
    Q4_var=IntVar(win)
    Q4_entrybox=ttk.Entry(win,width=20,textvariable=Q4_var)
    Q4_entrybox.grid(row=6,column=5)
    #
    Q5_label=ttk.Label(win,text=' Quantity ',font=("Times New Roman",20))
    Q5_label.grid( row=8, column=4, sticky=W)
    Q5_var=IntVar(win)
    Q5_entrybox=ttk.Entry(win,width=20,textvariable=Q5_var)
    Q5_entrybox.grid(row=8,column=5)
    #
    Q6_label=ttk.Label(win,text=' Quantity ',font=("Times New Roman",20))
    Q6_label.grid( row=10, column=4, sticky=W)
    Q6_var=IntVar(win)
    Q6_entrybox=ttk.Entry(win,width=20,textvariable=Q6_var)
    Q6_entrybox.grid(row=10,column=5)
    #
    Q7_label=ttk.Label(win,text=' Quantity ',font=("Times New Roman",20))
    Q7_label.grid( row=12, column=4, sticky=W)
    Q7_var=IntVar(win)
    Q7_entrybox=ttk.Entry(win,width=20,textvariable=Q7_var)
    Q7_entrybox.grid(row=12,column=5)
    ##




    submit_button=ttk.Button(win,text='Submit',command=action)
    submit_button.grid(row=14 , column=5)

    ##









    win.mainloop()
