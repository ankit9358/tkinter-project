import mysql.connector
import tkinter
from tkinter import messagebox
from tkinter import ttk
con = mysql.connector.connect(host = 'localhost',database='project',user='root',password='Ankit@123')
cur=con.cursor()
def add_i():
    win = tkinter.Tk()
    win.title('Add Item')
    win.geometry('2048x1536')

    space_label=ttk.Label(win,text='                   ',font=("Times New Roman",20))
    space_label.grid(row=0,column=0,sticky=tkinter.W)
    space_label=ttk.Label(win,text='                   ',font=("Times New Roman",20))
    space_label.grid(row=0,column=1,sticky=tkinter.W)
    space_label=ttk.Label(win,text='                 ',font=("Times New Roman",20))
    space_label.grid(row=0,column=2,sticky=tkinter.W)
    #space_label=ttk.Label(win,text='                   ',font=("Times New Roman",20))
    #space_label.grid(row=1,column=0,sticky=tkinter.W)

    Head_label= ttk.Label(win,text='ADD FOOD ITEM',font=("Times New Roman",25))
    Head_label.grid(row=0,column=2,sticky=tkinter.W)

    def action():
        i_f1=f1_item.get()
        i_f2=f2_item.get()
        i_f3=f3_item.get()
        i_f4=f4_item.get()
        i_f5=f5_item.get()
        i_p1=f1_price.get()
        i_p2=f2_price.get()
        i_p3=f3_price.get()
        i_p4=f4_price.get()
        i_p5=f5_price.get()
        try:
            cur.execute("INSERT INTO menu(item,price) VALUES (%s,%s)",(i_f1,i_p1))
            cur.execute("INSERT INTO menu(item,price) VALUES (%s,%s)",(i_f2,i_p2))
            cur.execute("INSERT INTO menu(item,price) VALUES (%s,%s)",(i_f3,i_p3))
            cur.execute("INSERT INTO menu(item,price) VALUES (%s,%s)",(i_f4,i_p4))
            cur.execute("INSERT INTO menu(item,price) VALUES (%s,%s)",(i_f5,i_p5))
        except Exception:
            con.commit()
            cur.execute('delete from menu where item="" ')
            
        #cur.fetchall()
        con.commit()
        con.close()
        messagebox.showinfo("Message", "Items had been added successfylly! ")
        win.destroy()

    space_label=ttk.Label(win,text='                                        ',font=("Times New Roman",20))
    space_label.grid(row=1,column=0,sticky=tkinter.W)
    space_label=ttk.Label(win,text='                                        ',font=("Times New Roman",20))
    space_label.grid(row=2,column=0,sticky=tkinter.W)

    mob_label=ttk.Label(win,text='Enter First Food Item',font=("Times New Roman",20))
    mob_label.grid(row=2,column=1,sticky=tkinter.W)
    f1_item=tkinter.StringVar(win)
    f1_item_entrybox=ttk.Entry(win,width=30,textvariable=f1_item)
    f1_item_entrybox.grid(row=2,column=2,sticky=tkinter.W)
    mob_label=ttk.Label(win,text='Price  ',font=("Times New Roman",20))
    mob_label.grid(row=2,column=4,sticky=tkinter.W)
    f1_price=tkinter.IntVar(win)
    f1_price_entrybox=ttk.Entry(win,width=14,textvariable=f1_price)
    f1_price_entrybox.grid(row=2,column=5,sticky=tkinter.W)


    space_label=ttk.Label(win,text='                                        ',font=("Times New Roman",20))
    space_label.grid(row=3,column=0,sticky=tkinter.W)
    space_label=ttk.Label(win,text='                                        ',font=("Times New Roman",20))
    space_label.grid(row=4,column=0,sticky=tkinter.W)

    mob_label=ttk.Label(win,text='Enter Second Food Item',font=("Times New Roman",20))
    mob_label.grid(row=4,column=1,sticky=tkinter.W)
    f2_item=tkinter.StringVar(win)
    f2_item_entrybox=ttk.Entry(win,width=30,textvariable=f2_item)
    f2_item_entrybox.grid(row=4,column=2,sticky=tkinter.W)
    mob_label=ttk.Label(win,text='Price  ',font=("Times New Roman",20))
    mob_label.grid(row=4,column=4,sticky=tkinter.W)
    f2_price=tkinter.IntVar(win)
    f2_price_entrybox=ttk.Entry(win,width=14,textvariable=f2_price)
    f2_price_entrybox.grid(row=4,column=5,sticky=tkinter.W)

    space_label=ttk.Label(win,text='                                        ',font=("Times New Roman",20))
    space_label.grid(row=5,column=0,sticky=tkinter.W)
    space_label=ttk.Label(win,text='                                        ',font=("Times New Roman",20))
    space_label.grid(row=6,column=0,sticky=tkinter.W)

    mob_label=ttk.Label(win,text='Enter Third Food Item',font=("Times New Roman",20))
    mob_label.grid(row=6,column=1,sticky=tkinter.W)
    f3_item=tkinter.StringVar(win)
    f3_item_entrybox=ttk.Entry(win,width=30,textvariable=f3_item)
    f3_item_entrybox.grid(row=6,column=2,sticky=tkinter.W)
    mob_label=ttk.Label(win,text='Price  ',font=("Times New Roman",20))
    mob_label.grid(row=6,column=4,sticky=tkinter.W)
    f3_price=tkinter.IntVar(win)
    f3_price_entrybox=ttk.Entry(win,width=14,textvariable=f3_price)
    f3_price_entrybox.grid(row=6,column=5,sticky=tkinter.W)

    space_label=ttk.Label(win,text='                                        ',font=("Times New Roman",20))
    space_label.grid(row=7,column=0,sticky=tkinter.W)
    space_label=ttk.Label(win,text='                                        ',font=("Times New Roman",20))
    space_label.grid(row=8,column=0,sticky=tkinter.W)

    mob_label=ttk.Label(win,text='Enter Fourth Food Item',font=("Times New Roman",20))
    mob_label.grid(row=8,column=1,sticky=tkinter.W)
    f4_item=tkinter.StringVar(win)
    f4_item_entrybox=ttk.Entry(win,width=30,textvariable=f4_item)
    f4_item_entrybox.grid(row=8,column=2,sticky=tkinter.W)
    mob_label=ttk.Label(win,text='Price  ',font=("Times New Roman",20))
    mob_label.grid(row=8,column=4,sticky=tkinter.W)
    f4_price=tkinter.IntVar(win)
    f4_price_entrybox=ttk.Entry(win,width=14,textvariable=f4_price)
    f4_price_entrybox.grid(row=8,column=5,sticky=tkinter.W)

    space_label=ttk.Label(win,text='                                        ',font=("Times New Roman",20))
    space_label.grid(row=9,column=0,sticky=tkinter.W)
    space_label=ttk.Label(win,text='                                        ',font=("Times New Roman",20))
    space_label.grid(row=10,column=0,sticky=tkinter.W)

    mob_label=ttk.Label(win,text='Enter Fifth Food Item',font=("Times New Roman",20))
    mob_label.grid(row=10,column=1,sticky=tkinter.W)
    f5_item=tkinter.StringVar(win)
    f5_item_entrybox=ttk.Entry(win,width=30,textvariable=f5_item)
    f5_item_entrybox.grid(row=10,column=2,sticky=tkinter.W)
    mob_label=ttk.Label(win,text='Price  ',font=("Times New Roman",20))
    mob_label.grid(row=10,column=4,sticky=tkinter.W)
    f5_price=tkinter.IntVar(win)
    f5_price_entrybox=ttk.Entry(win,width=14,textvariable=f5_price)
    f5_price_entrybox.grid(row=10,column=5,sticky=tkinter.W)

    space_label=ttk.Label(win,text='                                        ',font=("Times New Roman",20))
    space_label.grid(row=11,column=0,sticky=tkinter.W)
    space_label=ttk.Label(win,text='                                        ',font=("Times New Roman",20))
    space_label.grid(row=12,column=0,sticky=tkinter.W)



    submit_button=ttk.Button(win,text='Submit',command=action)
    submit_button.grid(row=12,column=5,sticky=tkinter.W)


    win.mainloop()

