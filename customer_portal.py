import mysql.connector
import tkinter
from tkinter import messagebox
from tkinter import ttk
import vacancy
con = mysql.connector.connect(host='localhost',database='project',user='root',password='Ankit@123')
cur=con.cursor()
def add_customer():
    win = tkinter.Tk()
    win.title('Add Customer')
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
        cos_date=str(day_var.get())+str(month_var.get())+str(year_var.get())
        cos_from=start_time_var.get()
        cos_to=stop_time_var.get()
        cos_tables=tables_var.get()
        cur.execute("INSERT INTO customer(name,age,email,mobile,gender,date,from_,to_,table_s) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(cos_name,cos_age,cos_email,cos_mob,cos_gender,cos_date,cos_from,cos_to,cos_tables))
        #cur.fetchall()
        messagebox.showinfo("Message", "Details of customer has been added successfylly! ")
        con.commit()
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
    date_label=ttk.Label(win,text='Enter reservation date',font=("Times New Roman",20))
    date_label.grid(row=5,column=0,sticky=tkinter.W)
    time_label=ttk.Label(win,text='Enter reservation time',font=("Times New Roman",20))
    time_label.grid(row=6,column=0,sticky=tkinter.W)
    from_label=ttk.Label(win,text='From-',font=("Times New Roman",20))
    from_label.grid(row=6,column=1,sticky=tkinter.W)
    to_label=ttk.Label(win,text='To-',font=("Times New Roman",20))
    to_label.grid(row=6,column=4,sticky=tkinter.W)
    tables_label=ttk.Label(win,text='Enter number of tables ',font=("Times New Roman",20))
    tables_label.grid(row=7,column=0,sticky=tkinter.W)

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
    mob_var=tkinter.StringVar(win)
    mob_entrybox=ttk.Entry(win,width=24,textvariable=mob_var)
    mob_entrybox.grid(row=3,column=1)

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

    start_time_var=tkinter.DoubleVar(win)
    start_time_combobox=ttk.Combobox(win, width=8 , textvariable=start_time_var, state='readonly')
    start_time_combobox['values']=(9.00,10.00,11.00,12.00,13.00,14.00,15.00,16.00,17.00,18.00,19.00,20.00)
    start_time_combobox.grid(row=6 , column=3,sticky=tkinter.W)

    stop_time_var=tkinter.IntVar(win)
    stop_time_var=ttk.Combobox(win, width=8 , textvariable=stop_time_var, state='readonly')
    stop_time_var['values']=(9.00,10.00,11.00,12.00,13.00,14.00,15.00,16.00,17.00,18.00,19.00,20.00)
    stop_time_var.grid(row=6 , column=5,sticky=tkinter.W)

    tables_var=tkinter.IntVar(win)
    tables_combobox=ttk.Combobox(win, width=8 , textvariable=tables_var, state='readonly')
    tables_combobox['values']=(1,2,3,4,5,6)
    tables_combobox.grid(row=7 , column=1,sticky=tkinter.W)






    #creating button
    
    submit_button=ttk.Button(win,text='Submit',command=action)
    submit_button.grid(row=10 , column=2)
    
    ##
    submit_button=ttk.Button(win,text='View Chart',command=vacancy.chart)
    submit_button.grid(row=10,column=1)




    #action



    win.mainloop()
