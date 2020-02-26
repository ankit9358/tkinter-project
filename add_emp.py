import mysql.connector
import tkinter
from tkinter import messagebox
from tkinter import ttk
con = mysql.connector.connect(host='localhost',database='project',user='root',password='Ankit@123')
cur=con.cursor()
def add_e():
    win = tkinter.Tk()
    win.title('Add Employe')
    #center allign
    width=win.winfo_screenwidth()
    height=win.winfo_screenheight()
    x=(width/2-750/2)
    y=(height/2-450/2)
    win.geometry("%dx%d+%d+%d"%(750,350,x,y))
    
    #action
    def action():
        cos_name=name_var.get()
        cos_age=age_var.get()
        cos_email=email_var.get()
        cos_mob=mob_var.get()
        cos_gender=gender_var.get()
        cos_join=str(day_var.get())+str(month_var.get())+str(year_var.get())
        cos_salary=salary_var.get()
        cos_job=role_var.get()
        cos_DOB=str(dob_day_var.get())+str(dob_month_var.get())+str(dob_year_var.get())
        cur.execute("INSERT INTO employe(name,age,email,mobile,gender,join_date,salary,job_role,DOB) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(cos_name,cos_age,cos_email,cos_mob,cos_gender,cos_join,cos_salary,cos_job,cos_DOB))
        #cur.fetchall()
        con.commit()
        messagebox.showinfo("Message", "Details of employee has been added successfylly! ")
        con.close()
        win.destroy()


    #creating labels
    name_label=ttk.Label(win,text='Enter Your Name',font=("Times New Roman",20))
    name_label.grid( row=0, column=0, sticky=tkinter.W)
    age_label=ttk.Label(win,text='Enter Your Age',font=("Times New Roman",20))
    age_label.grid(row=1, column=0, sticky=tkinter.W)
    email_label=ttk.Label(win,text='Enter your Email',font=("Times New Roman",20))
    email_label.grid(row=2, column=0, sticky=tkinter.W)
    mob_label=ttk.Label(win,text='Enter your Mobile number',font=("Times New Roman",20))
    mob_label.grid(row=3,column=0,sticky=tkinter.W)
    gender_label=ttk.Label(win,text='Gender ',font=("Times New Roman",20))
    gender_label.grid(row=4,column=0,sticky=tkinter.W)
    date_label=ttk.Label(win,text='Enter Joining date',font=("Times New Roman",20))
    date_label.grid(row=5,column=0,sticky=tkinter.W)
    salary_label=ttk.Label(win,text='Enter Salary',font=("Times New Roman",20))
    salary_label.grid(row=6,column=0,sticky=tkinter.W)
    job_label=ttk.Label(win,text='Enter Job Role ',font=("Times New Roman",20))
    job_label.grid(row=7,column=0,sticky=tkinter.W)
    dob_label=ttk.Label(win,text='Enter Date of Birth ',font=("Times New Roman",20))
    dob_label.grid(row=8,column=0,sticky=tkinter.W)

    #creating entry box
    name_var=tkinter.StringVar(win)
    name_entrybox=ttk.Entry(win, width=24,textvariable=name_var)
    name_entrybox.grid(row=0, column=1)
    age_var=tkinter.StringVar(win)
    age_entrybox=ttk.Entry(win, width=24, textvariable=age_var)
    age_entrybox.grid(row=1, column=1)
    email_var=tkinter.StringVar(win)
    email_entrybox=ttk.Entry(win, width=24, textvariable=email_var)
    email_entrybox.grid(row=2, column=1)
    mob_var=tkinter.IntVar(win)
    mob_entrybox=ttk.Entry(win,width=24,textvariable=mob_var)
    mob_entrybox.grid(row=3,column=1)
    salary_var=tkinter.IntVar(win)
    salary_entrybox=ttk.Entry(win,width=24,textvariable=salary_var)
    salary_entrybox.grid(row=6,column=1)

    #creating combo box
    gender_var=tkinter.StringVar(win)
    gender_combobox=ttk.Combobox(win, width=8 , textvariable=gender_var, state='readonly')
    gender_combobox['values']=('Male','Female','Other')
    gender_combobox.grid(row=4 , column=1,sticky=tkinter.W)

    day_var=tkinter.IntVar(win)
    day_combobox=ttk.Combobox(win, width=8 , textvariable=day_var, state='readonly')
    day_combobox['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
    day_combobox.grid(row=5 , column=1,sticky=tkinter.W)

    gap1=ttk.Label(win,text='- ')
    gap1.grid(row=5,column=2,sticky=tkinter.W)

    month_var=tkinter.StringVar(win)
    month_combobox=ttk.Combobox(win, width=8 , textvariable=month_var, state='readonly')
    month_combobox['values']=('January','February','March','April','May','June','July','August','September','October','November','December')
    month_combobox.grid(row=5 , column=3,sticky=tkinter.W)

    gap2=ttk.Label(win,text='- ')
    gap2.grid(row=5,column=4,sticky=tkinter.W)

    year_var=tkinter.IntVar(win)
    year_combobox=ttk.Combobox(win, width=8 , textvariable=year_var, state='readonly')
    year_combobox['values']=(2019,2020,2021)
    year_combobox.grid(row=5 , column=5,sticky=tkinter.W)


    role_var=tkinter.StringVar(win)
    role_combobox=ttk.Combobox(win, width=8 , textvariable=role_var, state='readonly')
    role_combobox['values']=('Cheff','Waiter','Helper')
    role_combobox.grid(row=7 , column=1,sticky=tkinter.W)

    ####
    dob_day_var=tkinter.IntVar(win)
    dob_day_combobox=ttk.Combobox(win, width=8 , textvariable=dob_day_var, state='readonly')
    dob_day_combobox['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
    dob_day_combobox.grid(row=8 , column=1,sticky=tkinter.W)

    gap1=ttk.Label(win,text='- ')
    gap1.grid(row=5,column=2,sticky=tkinter.W)

    dob_month_var=tkinter.StringVar(win)
    dob_month_combobox=ttk.Combobox(win, width=8 , textvariable=dob_month_var, state='readonly')
    dob_month_combobox['values']=('January','February','March','April','May','June','July','August','September','October','November','December')
    dob_month_combobox.grid(row=8 , column=3,sticky=tkinter.W)

    gap2=ttk.Label(win,text='- ')
    gap2.grid(row=8,column=4,sticky=tkinter.W)

    dob_year_var=tkinter.IntVar(win)
    dob_year_combobox=ttk.Combobox(win, width=8 , textvariable=dob_year_var, state='readonly')
    dob_year_combobox['values']=(1998,1999,2000,2001,2002,2003,2004,2005,2006,2007)
    dob_year_combobox.grid(row=8 , column=5,sticky=tkinter.W)

    ####




    #creating button 
    submit_button=ttk.Button(win,text='Submit',command=action)

    submit_button.grid(row=10 , column=2)


    #action



    win.mainloop()
