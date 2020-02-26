import mysql.connector
import tkinter
from tkinter import messagebox
from tkinter import ttk
con = mysql.connector.connect(host = 'localhost',database='project',user='root',password='Ankit@123')
cur=con.cursor()
def check_e():
    win = tkinter.Tk()
    win.title('Employe')
    win.geometry('2048x1536')
    Head_label= ttk.Label(win,text='Search Result',font=("Times New Roman",25))
    Head_label.pack()
    mob_label=ttk.Label(win,text='                        ',font=("Times New Roman",20))
    mob_label.pack()

    def action():
        cos_mob=mob_var.get()
        query = "SELECT * FROM employe WHERE mobile = %s"
        try:
            
            cur.execute(query,(cos_mob,))
            #cur.execute('SELECT * FROM customer WHERE mobile= "%s"',(cos_mob))
            row=cur.fetchone()

            mob_label=ttk.Label(win,text='                        ',font=("Times New Roman",20))
            mob_label.pack()

            tree = ttk.Treeview(win,height=2,columns=('name','age','email','mobile','gender','date','from','to'))
            tree.pack()
            tree.heading("#0",text="Name")
            tree.column("#0",width=120)
            tree.heading("#1",text="Age")
            tree.column("#1",width=80)
            tree.heading("#2",text="Email")
            tree.column("#2",width=180)
            tree.heading("#3",text="Mobile")
            tree.column("#3",width=100)
            tree.heading("#4",text="Gender")
            tree.column("#4",width=80)
            tree.heading("#5",text="Join Date")
            tree.column("#5",width=120)
            tree.heading("#6",text="Salary")
            tree.column("#6",width=80)
            tree.heading("#7",text="Job Role")
            tree.column("#7",width=80)
            tree.heading("#8",text="Date of Birth")
            tree.column("#8",width=120)
            tree.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
            tree.tag_configure('T',font='Arial 45')
            cancel_label=ttk.Label(win,text='Remove Employe',font=("Times New Roman",20))
            cancel_label.pack()
            def action2(): 
                cur.execute("DELETE FROM employe WHERE mobile = '%s'"%cos_mob)
                #print(cos_mob)
                #row=cur.fetchone()
                messagebox.showinfo("Message", "Details of employee has been removed successfylly! ")
                con.commit()
                win.destroy()
            def action3():
                #con.close()
                win.destroy()
            del_button=ttk.Button(win,text='Yes',command=action2)
            del_button.pack()
            del_button=ttk.Button(win,text='No',command=action3)
            del_button.pack()
            
        except Exception:
            mob_label=ttk.Label(win,text='                        ',font=("Times New Roman",20))
            mob_label.pack()
            mob_label=ttk.Label(win,text='SEARCH RESULT: Not Found',font=("Times New Roman",20))
            mob_label.pack()
        finally:
            pass
            #con.close()
        #win.destroy()

    mob_label=ttk.Label(win,text='Enter your Mobile number',font=("Times New Roman",20))
    mob_label.pack()
    mob_label=ttk.Label(win,text='                        ',font=("Times New Roman",20))
    mob_label.pack()



    mob_var=tkinter.StringVar(win)
    mob_entrybox=ttk.Entry(win,width=35,textvariable=mob_var)
    mob_entrybox.pack()
    mob_label=ttk.Label(win,text='                        ',font=("Times New Roman",20))
    mob_label.pack()

    submit_button=ttk.Button(win,text='Submit',command=action)
    submit_button.pack()





    win.mainloop()
