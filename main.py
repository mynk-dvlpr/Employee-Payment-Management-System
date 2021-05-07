from tkinter import*
from tkinter import messagebox,ttk
import pymysql
import time
import os
import tempfile

#==========Admin Login===================================
class Main:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payment Management System")
        self.root.geometry("1199x600+140+100")
        self.root.resizable(False,False)

        #=====BG Image=====
        self.bg=PhotoImage(file="images/new.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #==========Login Frame
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,height=300,width=425)

        title=Label(Frame_login,text="Login Here", font=("Impact",20),fg="black",bg="gold")
        title.place(x=0,y=0,width=425,height=50)
        desc=Label(Frame_login,text="Admin Login", font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=50,y=60)

        lbl_admin=Label(Frame_login,text="Admin ID / Username", font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=50,y=100)
        self.txt_user=Entry(Frame_login,font=("Times new roman",15),bg="lightgray")
        self.txt_user.place(x=52,y=130,width=300,height=30)

        lbl_pass=Label(Frame_login,text="Password", font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=50,y=160)
        self.txt_pass=Entry(Frame_login,show="*",font=("Times new roman",15),bg="lightgray")
        self.txt_pass.place(x=52,y=190,width=300,height=30)

        forget_btn=Button(Frame_login,text="Forget Password?",command=self.fwindow,activebackground="skyblue",bg="white",fg="black",bd=0,font=("times new roman",12)).place(x=50,y=230)
        Login_btn=Button(self.root,command=self.login_function,text="Login",bg="#d77337",fg="white",font=("times new roman",18)).place(x=260,y=430,width=200,height=38)

    #=========Forget Password==========
    def fwindow(self):
        if self.txt_user.get()=="":
            messagebox.showerror("Error","Please Enter the Valid Id")
        else:
            forgetwindow=Toplevel()
            self.forgetwindow=forgetwindow
            self.forgetwindow.title("FORGET PASSWORD")
            self.forgetwindow.geometry("600x500+400+150")
            self.forgetwindow.resizable(False,False)
            self.forgetwindow.focus_force()
            self.forgetwindow.grab_set()
            self.forgetwindow.bg=PhotoImage(file="images/login.png")
            self.forgetwindow.bg_image=Label(forgetwindow,image=forgetwindow.bg).place(x=0,y=0,relwidth=1,relheight=1)



            lbl_admin=Label(self.forgetwindow,text="Admin ID / Username", font=("Goudy old style",15,"bold"),fg="RED").place(x=50,y=120)
            self.txt_user=Entry(self.forgetwindow,font=("Times new roman",15),bg="white")
            self.txt_user.place(x=52,y=150,width=300,height=30)

            lbl_pass=Label(self.forgetwindow,text="NEW PASSWORD", font=("Goudy old style",15,"bold"),fg="BLACK").place(x=50,y=210)
            self.txt_new_pass=Entry(self.forgetwindow,show="*",font=("Times new roman",15),bg="lightgray")
            self.txt_new_pass.place(x=52,y=240,width=300,height=30)

            lbl_pass =Label(self.forgetwindow,text="CONFIRM PASSWORD", font=("Goudy old style",15,"bold"),fg="BLACK").place(x=50,y=300)
            self.txt_conf_pass=Entry(self.forgetwindow,font=("Times new roman",15),bg="lightgray")
            self.txt_conf_pass.place(x=52,y=330,width=300,height=30)

            change_btn=Button(self.forgetwindow,text="Reset Password",command=self.change_pass, font=("times new roman",15,"bold"),fg="white",bg="green").place(x=50,y=390,width=180,height=30)

    #=====================Creating Database Connection==============
    def login_function(self):    
            con=pymysql.connect(host='localhost',user='root',password='',db='emps')
            cur=con.cursor()
            cur.execute("Select * from admin_login where admin_id=%s and admin_pswd=%s",(self.txt_user.get(),self.txt_pass.get()))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("WARNING","User Id Not Found")
            else:
                return self.main()
                
                
    #============Change Password==============================
    def change_pass(self):
        if self.txt_user.get()=='' and self.txt_new_pass.get()=='' and self.txt_conf_pass.get()=='':
            messagebox.showerror("Warning","All fields are required")
        else:    
            con=pymysql.connect(host='localhost',user='root',password='',db='emps')
            cur=con.cursor()
            cur.execute("UPDATE admin_login set admin_pswd=%s where admin_id=%s",(self.txt_new_pass.get(),self.txt_user.get()))
            con.commit()
            con.close()
            messagebox.showinfo("SUCCESS","PASSWORD CHANGE SUCCESSFULLY")


#=========Employeee Details Entry Page============================================
    def main(self):
        empwindow=Toplevel()
        self.empwindow=empwindow
        self.empwindow.title("Employee Payment Management System | Developed By Mayank")
        self.empwindow.geometry("1380x700+70+55")
        self.empwindow.resizable(False,False)
        self.empwindow.config(bg="white")
        self.empwindow.grab_set()
        title=Label(self.empwindow,text="Employee Payment Management System", font=("times new roman",30,"bold"),bg="#262626", fg="white", anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        btn_emp=Button(self.empwindow,text="All Employee's",command= self.employee_frame,font=("times new roman", 13),bg="gray",fg="white").place(x=1100,y=10, height=30, width=120)
        btn_logout=Button(self.empwindow,text="LogOut",command=empwindow.destroy,font=("times new roman", 13),bg="gray",fg="white").place(x=1240,y=10, height=30, width=120)
                
        #============Frame1===========================
        #==========Variables===============
        self.var_emp_id=StringVar()
        self.var_designation=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_hr_location=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_proof_id=StringVar()  #=====Adhaar Card=====
        self.var_contact=StringVar()
        self.var_status=StringVar()
        self.var_experience=StringVar()
        

        Frame1=Frame(self.empwindow,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=70,width=750,height=620)
        title2=Label(Frame1,text="Employee Details", font=("times new roman", 20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        lbl_Id=Label(Frame1,text="Employee ID", font=("times new roman", 20),bg="white",fg="black").place(x=10,y=70)
        self.txt_Id=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_emp_id,bg="lightyellow",fg="black")
        self.txt_Id.place(x=170,y=75,width=200)
        btn_search=Button(Frame1,text="Search",command=self.search, font=("times new roman", 20),bg="gray",fg="black").place(x=440,y=72, height=30)
        
        #==========Row1
        lbl_designation = Label(Frame1,text="Designation:", font=("times new roman", 20),bg="white",fg="black").place(x=10,y=120)
        txt_designation = Entry(Frame1,font=("times new roman", 15),textvariable=self.var_designation,bg="lightyellow",fg="black").place(x=170,y=125,width=200)
        lbl_dob=Label(Frame1,text="D.O.B:", font=("times new roman", 20),bg="white",fg="black").place(x=390,y=120)
        txt_dob=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_dob,bg="lightyellow",fg="black").place(x=520,y=125)

        #==========Row2
        lbl_Name=Label(Frame1,text="Name:", font=("times new roman", 20),bg="white",fg="black").place(x=10,y=170)
        txt_Name=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_name,bg="lightyellow",fg="black").place(x=170,y=175,width=200)
        lbl_doj=Label(Frame1,text="D.O.J:", font=("times new roman", 20),bg="white",fg="black").place(x=390,y=170)
        txt_doj=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_doj,bg="lightyellow",fg="black").place(x=520,y=175)

        #==========Row3
        lbl_age=Label(Frame1,text="Age:", font=("times new roman", 20),bg="white",fg="black").place(x=10,y=220)
        txt_age=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_age,bg="lightyellow",fg="black").place(x=170,y=225,width=200)
        lbl_experience=Label(Frame1,text="Experience:", font=("times new roman", 20),bg="white",fg="black").place(x=390,y=220)
        txt_experience=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_experience,bg="lightyellow",fg="black").place(x=520,y=225)

        #==========Row4
        lbl_gender=Label(Frame1,text="Gender:", font=("times new roman", 20),bg="white",fg="black").place(x=10,y=270)
        txt_gender=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_gender,bg="lightyellow",fg="black").place(x=170,y=275,width=200)
        lbl_proof=Label(Frame1,text="Proof ID:", font=("times new roman", 20),bg="white",fg="black").place(x=390,y=270)
        txt_proof=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_proof_id,bg="lightyellow",fg="black").place(x=520,y=275)

        #==========Row5
        lbl_email=Label(Frame1,text="Email:", font=("times new roman", 20),bg="white",fg="black").place(x=10,y=320)
        txt_email=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_email,bg="lightyellow",fg="black").place(x=170,y=325,width=200)
        lbl_contact=Label(Frame1,text="Contact No.:", font=("times new roman", 20),bg="white",fg="black").place(x=390,y=320)
        txt_contact=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_contact,bg="lightyellow",fg="black").place(x=520,y=325)

         #==========Row6
        lbl_hired=Label(Frame1,text="Hired Location:", font=("times new roman", 18),bg="white",fg="black").place(x=10,y=372)
        txt_hired=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_hr_location,bg="lightyellow",fg="black").place(x=170,y=375,width=200)
        lbl_status=Label(Frame1,text="Status:", font=("times new roman", 20),bg="white",fg="black").place(x=390,y=370)
        txt_status=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_status,bg="lightyellow",fg="black").place(x=520,y=375)

         #==========Row7
        lbl_address=Label(Frame1,text="Address:", font=("times new roman", 18),bg="white",fg="black").place(x=10,y=422)
        self.txt_address=Text(Frame1,font=("times new roman", 15),bg="lightyellow",fg="black")
        self.txt_address.place(x=170,y=425,width=550,height=150)



        #============Frame2=========================== 
        #==========Variables===============
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_salary=StringVar()
        self.var_total_days=StringVar()
        self.var_absent=StringVar()
        self.var_medical=StringVar()
        self.var_pf=StringVar()
        self.var_convence=StringVar()
        self.var_net_salary=StringVar()
               
        
        Frame2=Frame(self.empwindow,bd=2,relief=RIDGE,bg="white")
        Frame2.place(x=770,y=70,width=600,height=300)

        title3=Label(Frame2,text="Employee Salary Details", font=("times new roman", 20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        lbl_month=Label(Frame2,text="Month:", font=("times new roman", 20),bg="white",fg="black").place(x=10,y=60)
        txt_month=Entry(Frame2,font=("times new roman", 18),textvariable=self.var_month,bg="lightyellow",fg="black").place(x=110,y=63,width=100)
        
        lbl_year=Label(Frame2,text="Year:", font=("times new roman", 20),bg="white",fg="black").place(x=210,y=60)
        txt_year=Entry(Frame2,font=("times new roman", 18),textvariable=self.var_year,bg="lightyellow",fg="black").place(x=280,y=63,width=100)
        
        lbl_salary=Label(Frame2,text="Salary:", font=("times new roman", 20),bg="white",fg="black").place(x=395,y=60)
        txt_salary=Entry(Frame2,font=("times new roman", 18),textvariable=self.var_salary,bg="lightyellow",fg="black").place(x=485,y=63,width=100)
        
        #==========Row1
        lbl_days=Label(Frame2,text="Total Days:", font=("times new roman", 18),bg="white",fg="black").place(x=10,y=120)
        txt_days=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_total_days,bg="lightyellow",fg="black").place(x=170,y=125,width=100)
        lbl_absent=Label(Frame2,text="Absents:", font=("times new roman", 18),bg="white",fg="black").place(x=300,y=120)
        txt_absent=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_absent,bg="lightyellow",fg="black").place(x=420,y=125,width=120)

        #==========Row2
        lbl_medical=Label(Frame2,text="Medical:", font=("times new roman", 18),bg="white",fg="black").place(x=10,y=150)
        txt_medical=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_medical,bg="lightyellow",fg="black").place(x=170,y=155,width=100)
        lbl_pf=Label(Frame2,text="Provident Fund:", font=("times new roman", 18),bg="white",fg="black").place(x=300,y=150)
        txt_pf=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_pf,bg="lightyellow",fg="black").place(x=465,y=155,width=120)

        #==========Row3
        lbl_convence=Label(Frame2,text="Convence:", font=("times new roman", 18),bg="white",fg="black").place(x=10,y=180)
        txt_convence=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_convence,bg="lightyellow",fg="black").place(x=170,y=185,width=100)
        lbl_netsalry=Label(Frame2,text="Net Salary:", font=("times new roman", 18),bg="white",fg="black").place(x=300,y=180)
        txt_netsalary=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_net_salary,bg="lightgray",fg="black").place(x=465,y=185,width=120)

        btn_calculate=Button(Frame2,text="Calculate",command=self.calculate,font=("times new roman", 20),bg="orange",fg="black").place(x=140,y=225, height=30, width=120)
        self.btn_save=Button(Frame2,text="Save",command=self.add,font=("times new roman", 20),bg="green",fg="white")
        self.btn_save.place(x=285,y=225, height=30, width=120)
        btn_clear=Button(Frame2,text="Clear",command=self.clear, font=("times new roman", 20),bg="gray",fg="black").place(x=430,y=225, height=30, width=120)
        
        self.btn_update=Button(Frame2,text="Update",command=self.update,state=DISABLED,font=("times new roman", 20),bg="blue",fg="white")
        self.btn_update.place(x=140,y=260, height=30, width=200)
        self.btn_delete=Button(Frame2,text="Delete",command=self.delete,state=DISABLED,font=("times new roman", 20),bg="red",fg="white")
        self.btn_delete.place(x=350,y=260, height=30, width=200)
        
        
        #============Frame3===========================
        
        
        Frame3=Frame(self.empwindow,bd=2,relief=RIDGE,bg="white")
        Frame3.place(x=770,y=380,width=600,height=310)
        
        #=====Calculator==============================
        self.var_txt=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)

        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''
        def clear_cal():
            self.var_txt.set('')
            self.var_operator=''

        Cal_Frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        Cal_Frame.place(x=10,y=2,width=248,height=300)

        txt_Result=Entry(Cal_Frame,bg='lightyellow',textvariable=self.var_txt,font=("times new roman",20,"bold"),justify=RIGHT).place(x=0,y=0,relwidth=1,height=55)

        #=========Row1================================
        btn_7=Button(Cal_Frame,text='7',command=lambda:btn_click(7),font=("times new roman",15,"bold")).place(x=1,y=55,w=60,h=60)
        btn_8=Button(Cal_Frame,text='8',command=lambda:btn_click(8),font=("times new roman",15,"bold")).place(x=62,y=55,w=60,h=60)
        btn_9=Button(Cal_Frame,text='9',command=lambda:btn_click(9),font=("times new roman",15,"bold")).place(x=123,y=55,w=60,h=60)
        btn_div=Button(Cal_Frame,text='/',command=lambda:btn_click('/'),font=("times new roman",15,"bold")).place(x=184,y=55,w=60,h=60)
        
        #=========Row2================================
        btn_4=Button(Cal_Frame,text='4',command=lambda:btn_click(4),font=("times new roman",15,"bold")).place(x=1,y=115,w=60,h=60)
        btn_5=Button(Cal_Frame,text='5',command=lambda:btn_click(5),font=("times new roman",15,"bold")).place(x=62,y=115,w=60,h=60)
        btn_6=Button(Cal_Frame,text='6',command=lambda:btn_click(6),font=("times new roman",15,"bold")).place(x=123,y=115,w=60,h=60)
        btn_mul=Button(Cal_Frame,text='*',command=lambda:btn_click('*'),font=("times new roman",15,"bold")).place(x=184,y=115,w=60,h=60)

        #=========Row3================================
        btn_1=Button(Cal_Frame,text='1',command=lambda:btn_click(1),font=("times new roman",15,"bold")).place(x=1,y=175,w=60,h=60)
        btn_2=Button(Cal_Frame,text='2',command=lambda:btn_click(2),font=("times new roman",15,"bold")).place(x=62,y=175,w=60,h=60)
        btn_3=Button(Cal_Frame,text='3',command=lambda:btn_click(3),font=("times new roman",15,"bold")).place(x=123,y=175,w=60,h=60)
        btn_min=Button(Cal_Frame,text='-',command=lambda:btn_click('-'),font=("times new roman",15,"bold")).place(x=184,y=175,w=60,h=60)
        
        #=========Row4================================
        btn_0=Button(Cal_Frame,text='0',command=lambda:btn_click(0),font=("times new roman",15,"bold")).place(x=1,y=235,w=60,h=60)
        btn_dot=Button(Cal_Frame,text='C',command=clear_cal,font=("times new roman",15,"bold")).place(x=62,y=235,w=60,h=60)
        btn_equal=Button(Cal_Frame,text='=',command=result,font=("times new roman",15,"bold")).place(x=123,y=235,w=60,h=60)
        btn_sum=Button(Cal_Frame,text='+',command=lambda:btn_click('+'),font=("times new roman",15,"bold")).place(x=184,y=235,w=60,h=60)
        
        #==========Salary Frame=======================
        sal_Frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        sal_Frame.place(x=260,y=2,width=325,height=300)
        title_sal=Label(sal_Frame,text="Salary receipt", font=("times new roman", 20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        sal_Frame2=Frame(sal_Frame,bg='white',bd=2,relief=RIDGE)
        sal_Frame2.place(x=0,y=30,relwidth=1,height=230)
        self.sample=f'''\tCompany Name, XYZ\n\tAddress: Xyz, Floor4
-------------------------------------------------
Employee ID\t\t:  
Salary Of\t\t:  Mon-YYYY
Generated On\t\t:  DD-MM-YYYY
-------------------------------------------------
Total Days\t\t:  DD
Total Present\t\t:  DD
Total Absent\t\t:  DD
Convence\t\t:  Rs.---- 
Medical\t\t:  Rs.----
PF\t\t:  Rs.----
Gross Payment\t\t:  Rs.------
Net Salary\t\t:  Rs.------
-------------------------------------------------
This is System generated receipt, not re-quired any signature
'''   

        scroll_y=Scrollbar(sal_Frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_receipt=Text(sal_Frame2,font=("tims new roman",13),bg='lightyellow',yscrollcommand=scroll_y.set)
        self.txt_salary_receipt.pack(fill=BOTH,expand=2)
        scroll_y.config(command=self.txt_salary_receipt.yview)
        self.txt_salary_receipt.insert(END,self.sample)

        self.btn_print=Button(sal_Frame,text="Print",command=self.print,state=DISABLED, font=("times new roman", 20),bg="lightblue",fg="black")
        self.btn_print.place(x=180,y=262, height=30, width=120)
      
        self.check_connection()
    #=================All Functions Start Here================================================================
    def search(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='emps')
            cur=con.cursor()
            cur.execute("select * from emp_salary where emp_id=%s",(self.var_emp_id.get()))
            row=cur.fetchone()
            #print(rows)
            if row==None:
                messagebox.showerror("Error","Invalid Employee ID, Please Try with another Employee ID", parent=self.empwindow)
            else:
                print(row)
                self.var_emp_id.set(row[0])
                self.var_designation.set(row[1])
                self.var_name.set(row[2])
                self.var_age.set(row[3])
                self.var_gender.set(row[4])
                self.var_email.set(row[5])
                self.var_hr_location.set(row[6])
                self.var_doj.set(row[7])
                self.var_dob.set(row[8])
                self.var_experience.set(row[9])
                self.var_proof_id.set(row[10])
                self.var_contact.set(row[11])
                self.var_status.set(row[12])
                self.txt_address.delete('1.0',END)
                self.txt_address.insert(END, row[13])

                self.var_month.set(row[14])
                self.var_year.set(row[15])
                self.var_salary.set(row[16])
                self.var_total_days.set(row[17])
                self.var_absent.set(row[18])
                self.var_medical.set(row[19])
                self.var_pf.set(row[20])
                self.var_convence.set(row[21])
                self.var_net_salary.set(row[22])
                file_=open('Salary_receipt/'+str(row[23]),'r')
                self.txt_salary_receipt.delete('1.0',END)
                for i in file_:
                    self.txt_salary_receipt.insert(END, i)
                file_.close()
                self.btn_save.config(state=DISABLED)
                self.btn_update.config(state=NORMAL)
                self.btn_delete.config(state=NORMAL)
                self.txt_Id.config(state='readonly')
                self.btn_print.config(state=NORMAL)    

        except Exception as ex:
            messagebox.showerror("Error",f'Error due to:{str(ex)}')
    

    def clear(self):
        self.btn_save.config(state=NORMAL)
        self.btn_update.config(state=DISABLED)
        self.btn_delete.config(state=DISABLED)
        self.btn_print.config(state=DISABLED)
        self.txt_Id.config(state=NORMAL)

        self.var_emp_id.set('')
        self.var_designation.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_gender.set('')
        self.var_email.set('')
        self.var_hr_location.set('')
        self.var_doj.set('')
        self.var_dob.set('')
        self.var_experience.set('')
        self.var_proof_id.set('')
        self.var_contact.set('')
        self.var_status.set('')
        self.txt_address.delete('1.0',END)
        

        self.var_month.set('')
        self.var_year.set('')
        self.var_salary.set('')
        self.var_total_days.set('')
        self.var_absent.set('')
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_convence.set('')
        self.var_net_salary.set('')
        self.txt_salary_receipt.delete('1.0',END)
        self.txt_salary_receipt.insert(END,self.sample)


    def delete(self):
        if self.var_emp_id.get()=='':
            messagebox.showerror("Error","Employee ID must be required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='emps')
                cur=con.cursor()
                cur.execute("select * from emp_salary where emp_id=%s",(self.var_emp_id.get()))
                row=cur.fetchone()
                #print(rows)
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID, Please Try with another Employee ID", parent=self.empwindow)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?")
                    if op==True:
                        cur.execute("delete from emp_salary where emp_id=%s",(self.var_emp_id.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Delete","Employee Record Deleted Successfully", parent=self.empwindow)
                        self.clear()
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to:{str(ex)}')
    

    def add(self):
        if self.var_emp_id.get()=='' or self.var_net_salary.get()=='' or self.var_name.get()=='' or self.var_dob.get()=='':
            messagebox.showerror("Error","Employee details are required...")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='emps')
                cur=con.cursor()
                cur.execute("select * from emp_salary where emp_id=%s",(self.var_emp_id.get()))
                row=cur.fetchone()
                #print(rows)
                if row!=None:
                    messagebox.showerror("Error","This Employee ID has already available in our record, Try again with another ID", parent=self.empwindow)
                else:
                    cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_emp_id.get(),
                        self.var_designation.get(),
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_hr_location.get(),
                        self.var_doj.get(),
                        self.var_dob.get(),
                        self.var_experience.get(),
                        self.var_proof_id.get(),
                        self.var_contact.get(),
                        self.var_status.get(),
                        self.txt_address.get('1.0',END),

                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_salary.get(),
                        self.var_total_days.get(),
                        self.var_absent.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),
                        self.var_net_salary.get(),
                        self.var_emp_id.get()+".txt"
                    
                    )
                    )
                    con.commit()
                    con.close()
                    file_=open('Salary_receipt/'+str(self.var_emp_id.get())+".txt",'w')
                    file_.write(self.txt_salary_receipt.get('1.0',END))
                    file_.close()

                    messagebox.showinfo("Success","Record Added Successfully")
                    self.btn_print.config(state=NORMAL)

            except Exception as ex:
                messagebox.showerror("Error",f'Error due to:{str(ex)}')

    def update(self):
        if self.var_emp_id.get()=='' or self.var_net_salary.get()=='' or self.var_name.get()=='' or self.var_dob.get()=='':
            messagebox.showerror("Error","Employee details are required...")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='emps')
                cur=con.cursor()
                cur.execute("select * from emp_salary where emp_id=%s",(self.var_emp_id.get()))
                row=cur.fetchone()
                #print(rows)
                if row==None:
                    messagebox.showerror("Error","This Employee ID is invalid, Try again with valid Employee ID", parent=self.empwindow)
                else:
                    cur.execute("UPDATE `emp_salary` SET `designation`=%s,`name`=%s,`age`=%s,`gender`=%s,`email`=%s,`hr_location`=%s,`doj`=%s,`dob`=%s,`experience`=%s,`proof_id`=%s,`contact`=%s,`status`=%s,`address`=%s,`month`=%s,`year`=%s,`basic_salary`=%s,`total_days`=%s,`absent_days`=%s,`medical`=%s,`pf`=%s,`convence`=%s,`net_salary`=%s,`salary_receipt`=%s WHERE `emp_id`=%s",
                    (
                        
                        self.var_designation.get(),
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_hr_location.get(),
                        self.var_doj.get(),
                        self.var_dob.get(),
                        self.var_experience.get(),
                        self.var_proof_id.get(),
                        self.var_contact.get(),
                        self.var_status.get(),
                        self.txt_address.get('1.0',END),
                        
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_salary.get(),
                        self.var_total_days.get(),
                        self.var_absent.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),
                        self.var_net_salary.get(),
                        self.var_emp_id.get()+".txt",
                        self.var_emp_id.get()
                    
                    )
                    )
                    con.commit()
                    con.close()
                    file_=open('Salary_receipt/'+str(self.var_emp_id.get())+".txt",'w')
                    file_.write(self.txt_salary_receipt.get('1.0',END))
                    file_.close()

                    messagebox.showinfo("Success","Record Updated Successfully")

            except Exception as ex:
                messagebox.showerror("Error",f'Error due to:{str(ex)}')


    def calculate(self):
            if self.var_month.get()=='' or self.var_year.get()=='' or self.var_salary.get()=='' or self.var_total_days.get()=='' or self.var_absent.get()=='' or self.var_medical.get()=='':
                messagebox.showerror('Error','All fields are required')
            else:
                # self.var_net_salary.set("RESULT")
                # 35000/31==1752
                #31-10=21*1752
                per_day=int(self.var_salary.get())/int(self.var_total_days.get())
                work_day=int(self.var_total_days.get())-int(self.var_absent.get())
                sal_=per_day*work_day
                deduct=int(self.var_medical.get())+int(self.var_pf.get())
                addition=int(self.var_convence.get())
                net_sal=sal_-deduct+addition
                self.var_net_salary.set(str(round(net_sal,2)))
                #=============Update the receipt
                new_sample=f'''\tCompany Name, XYZ\n\tAddress: Xyz, Floor4
-------------------------------------------------
Employee ID\t\t:  {self.var_emp_id.get()} 
Salary Of\t\t:  {self.var_month.get()}-{self.var_year.get()}
Generated On\t\t:  {str(time.strftime("%d-%m-%Y"))}
-------------------------------------------------
Total Days\t\t:  {self.var_total_days.get()}
Total Present\t\t:  {str(int(self.var_total_days.get())-int(self.var_absent.get()))} 
Total Absent\t\t:  {self.var_absent.get()}
Convence\t\t:  Rs.{self.var_convence.get()} 
Medical\t\t:  Rs.{self.var_medical.get()}
PF\t\t:  Rs.{self.var_pf.get()}
Gross Payment\t\t:  Rs.{self.var_salary.get()}
Net Salary\t\t:  Rs.{self.var_net_salary.get()}
-------------------------------------------------
This is System generated receipt, not re-quired any signature
'''
                self.txt_salary_receipt.delete('1.0',END)
                self.txt_salary_receipt.insert(END,new_sample)



    def check_connection(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='emps')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            print(rows)

        except Exception as ex:
            messagebox.showerror("Error",f'Error due to:{str(ex)}')

    def show(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='emps')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            #print(rows)
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert('',END, values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to:{str(ex)}')


    def employee_frame(self):
        self.empframe=Toplevel(self.empwindow)
        self.empframe.title("Employee Payment Management System | Developed By Mayank")
        self.empframe.geometry("1000x550+240+150")
        self.empframe.config(bg="white")
        title=Label(self.empframe,text="All Employee Details", font=("times new roman", 30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).pack(side=TOP,fill=X)
        self.empframe.focus_force()
        self.empframe.grab_set()

        scrolly=Scrollbar(self.empframe,orient=VERTICAL)
        scrollx=Scrollbar(self.empframe,orient=HORIZONTAL)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)


        self.employee_tree=ttk.Treeview(self.empframe,columns=('emp_id', 'designation', 'name', 'age', 'gender', 'email', 'hr_location', 'doj', 'dob', 'experience', 'proof_id', 'contact', 'status', 'address', 'month', 'year', 'basic_salary', 'total_days', 'absent_days', 'medical', 'pf', 'convence', 'net_salary', 'salary_receipt'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.employee_tree.heading('emp_id',text='EID')
        self.employee_tree.heading('designation',text='Designation')
        self.employee_tree.heading('name',text='Name')
        self.employee_tree.heading('age',text='Age')
        self.employee_tree.heading('gender',text='Gender')
        self.employee_tree.heading('email',text='Email')
        self.employee_tree.heading('hr_location',text='Hr. Loc.')    
        self.employee_tree.heading('dob',text='D.O.B.')
        self.employee_tree.heading('doj',text='D.O.J.')
        self.employee_tree.heading('experience',text='Experience')
        self.employee_tree.heading('proof_id',text='Proof')
        self.employee_tree.heading('contact',text='Contact')
        self.employee_tree.heading('status',text='Status')
        self.employee_tree.heading('address',text='Address')
        self.employee_tree.heading('month',text='Month')
        self.employee_tree.heading('year',text='Year')
        self.employee_tree.heading('basic_salary',text='Basic Salary')
        self.employee_tree.heading('total_days',text='Days')
        self.employee_tree.heading('absent_days',text='Absent')
        self.employee_tree.heading('medical',text='Medical')
        self.employee_tree.heading('pf',text='PF')
        self.employee_tree.heading('convence',text='Convence')
        self.employee_tree.heading('net_salary',text='Net Salary')
        self.employee_tree.heading('salary_receipt',text='Salary reciept')
        self.employee_tree['show']='headings'

        self.employee_tree.column('emp_id',width=100)
        self.employee_tree.column('designation',width=100)
        self.employee_tree.column('name',width=100)
        self.employee_tree.column('age',width=100)
        self.employee_tree.column('gender',width=100)
        self.employee_tree.column('email',width=100)
        self.employee_tree.column('hr_location',width=100)    
        self.employee_tree.column('dob',width=100)
        self.employee_tree.column('doj',width=100)
        self.employee_tree.column('experience',width=100)
        self.employee_tree.column('proof_id',width=100)
        self.employee_tree.column('contact',width=100)
        self.employee_tree.column('status',width=100)
        self.employee_tree.column('address',width=500)
        self.employee_tree.column('month',width=100)
        self.employee_tree.column('year',width=100)
        self.employee_tree.column('basic_salary',width=100)
        self.employee_tree.column('total_days',width=100)
        self.employee_tree.column('absent_days',width=100)
        self.employee_tree.column('medical',width=100)
        self.employee_tree.column('pf',width=100)
        self.employee_tree.column('convence',width=100)
        self.employee_tree.column('net_salary',width=100)
        self.employee_tree.column('salary_receipt',width=100)
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1)
        self.show()


        self.empframe.mainloop()

    def print(self):
        file_=tempfile.mktemp(".txt")
        open(file_,'w').write(self.txt_salary_receipt.get('1.0',END))
        os.startfile(file_,'print')

        



root=Tk()
obj=Main(root)
root.mainloop()