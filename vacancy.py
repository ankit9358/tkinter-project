import mysql.connector
import tkinter
from tkinter import messagebox
from tkinter import ttk
con = mysql.connector.connect(host = 'localhost',database='project',user='root',password='Ankit@123')
cur=con.cursor()

def chart():
    win = tkinter.Tk()
    win.title('Chart')
    width=win.winfo_screenwidth()
    height=win.winfo_screenheight()
    x=(width/2-600/2)
    y=(height/2-200/2)
    win.geometry("%dx%d+%d+%d"%(600,200,x,y))


    def action():
        cos=str(day_var.get())+str(month_var.get())+str(year_var.get())
        try:
            cur.execute("select to_, from_, table_s from customer where date='%s'"%cos)
            row=cur.fetchall()
            tree = ttk.Treeview(win,height=2,columns=('to_','from_'))
            tree.grid(row=2,column=0)
            tree.heading("#0",text="From")
            tree.column("#0",width=80)
            tree.heading("#1",text="To")
            tree.column("#1",width=80)
            tree.heading("#2",text="Tables")
            tree.column("#2",width=80)
            for i in row:
                tree.insert('','end',text=i[1],values=(i[0],i[2]))
                tree.tag_configure('T',font='Arial 20')


                                
        except Exception:
            mob_label=ttk.Label(win,text='SEARCH RESULT: Not Found',font=("Times New Roman",20))
            mob_label.grid(row=4,column=0)
        finally:
            pass
                                


    mob_label=ttk.Label(win,text='          Enter Date:          ',font=("Times New Roman",20))
    mob_label.grid(row=0,column=0)



    day_var=tkinter.IntVar(win)
    day_combobox=ttk.Combobox(win, width=8 , textvariable=day_var, state='readonly')
    day_combobox['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
    day_combobox.grid(row=0 , column=1,sticky=tkinter.W)

    gap1=ttk.Label(win,text='- ')
    gap1.grid(row=0,column=2,sticky=tkinter.W)

    month_var=tkinter.StringVar(win)
    month_combobox=ttk.Combobox(win, width=8 , textvariable=month_var, state='readonly')
    month_combobox['values']=('January','February','March','April','May','June','July','August','September','October','November','December')
    month_combobox.grid(row=0 , column=3,sticky=tkinter.W)

    gap2=ttk.Label(win,text='- ')
    gap2.grid(row=0,column=4,sticky=tkinter.W)

    year_var=tkinter.IntVar(win)
    year_combobox=ttk.Combobox(win, width=8 , textvariable=year_var, state='readonly')
    year_combobox['values']=(2019,2020,2021)
    year_combobox.grid(row=0 , column=5,sticky=tkinter.W)





    submit_button=ttk.Button(win,text='Submit',command=action)
    submit_button.grid(row=1,column=3)


    win.mainloop()
