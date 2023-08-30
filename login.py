from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
from datetime import datetime    
from tkinter import messagebox
from customer_registration import Register
from driver_registraion import Driver_register
from driver_dashboard import Driver
from admin_dashboard import Admin_dashboard
from booking_trip import Booking
import mysql.connector

class Login_Page:
  #initialize window
  def __init__(self,window):    
    self.window = window
    self.window.title("Online Taxi Booking system")
    self.window.geometry("1400x700+0+0")
    self.window.state('zoomed')

    # textvariables
    self.var_cmbusertype = StringVar()
    self.var_email = StringVar()
    self.var_password = StringVar()

  # set background Image
    self.bg = ImageTk.PhotoImage(file = r'image\taxx.png')
    lbl_bg = Label(self.window, image= self.bg)
    lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

    # Create a TimeLabel object
    self.time_label = Label(self.window, text="Date:",font=("Arial",11,'bold'),bg='#77D0FA',fg='black',width=35,height=1)
    self.time_label.place(x=20,y=5)

    self.update_time()

    #frame for driver_registration dashboard
    frame_2 = Frame(self.window,bg='#77D0FA')
    frame_2.place(x=800 , y=35, width = 420, height=45)

    lbl_title = Label(frame_2,text='To Work as Driver, Register Here', font=('Arial',15,'bold'),fg='white',bg='#77D0FA')
    lbl_title.place(x=5,y=6)

    btn_driver_reg = Button(frame_2,text="Sign Up",fg="white",font=("Arial",14,'bold'),bg="#1D93EF",activebackground="#1D93EF",activeforeground='white',border=1,cursor='hand2',command= self.open_driver_registration)
    btn_driver_reg.place(x=325,y=4)

    #frame for login
    frame_1 = Frame(self.window,bg='black')
    frame_1.place(x=490 , y=150, width = 340, height=440)

    # login Image
    my_image = Image.open(r'C:\Users\asus\Desktop\book_taxi\image\ss.png').resize((100,100))
    self.img_1 = ImageTk.PhotoImage(my_image)
    
    lbl_img_1 = Label(frame_1,image=self.img_1,bg='black',border=0)
    lbl_img_1.place(x=120,y=10,width=100,height=100)

    lbl_title = Label(frame_1,text='Get Started', font=('Arial',15,'bold'),fg='white',bg='black')
    lbl_title.place(x=115,y=115)
# -----------------------------------------
    #labels
    self.cmbusertype = ttk.Combobox(frame_1,textvariable = self.var_cmbusertype,font=('Arial',11,'bold'),width=16,state='readonly')
    self.cmbusertype['values']= ('Select UserType','Customer','Driver','Admin')
    self.cmbusertype.current(0)
    self.cmbusertype.place(x=97,y=150)

    lbl_email = Label(frame_1, text='email',font=('Arial',13,'bold'),fg='white',bg='black')
    lbl_email.place(x=50,y=195)

    self.entry_email = Entry(frame_1,textvariable=self.var_email,font=('Arial',13,'bold'),width=26,borderwidth=0)
    self.entry_email.place(x=50,y=225)

    lbl_pass = Label(frame_1,text='password',font=('Arial',13,'bold'),fg='white',bg='black')
    lbl_pass.place(x=50,y=255)

    self.entry_pass = Entry(frame_1,textvariable=self.var_password,font=('Arial',13,'bold'),show='*',width=26,borderwidth=0)
    self.entry_pass.place(x=50,y=285)

    #Buttons
    show_button = Checkbutton(frame_1,text='show password',fg='#19BA93',bg='black',font=('Arial',10,'bold'),activebackground='black',activeforeground='#19BA93',command=self.show_pass)
    show_button.place(x=45,y=315)

    btn_signUp = Button(frame_1,text="create new account",fg="#F84040",font=("Arial",10,'bold'),bg="black",activebackground="black",activeforeground='#F84040',border=0,cursor='hand2',command= self.register_window)
    btn_signUp.place(x=100,y=350)

    btn_forgot_pass = Button(frame_1,text="forgot password",fg="#F84040",font=("Arial",10,'bold'),bg="black",activebackground="black",activeforeground='#F84040',border=0,cursor="hand2",command=self.forgot_pass_win)
    btn_forgot_pass.place(x=200,y=316)

    btn_login = Button(frame_1,text='Login',font=('Arial',13,'bold'),fg='white',bg='#19BA93',border=0,padx=80,pady=3,activebackground='#19BA93',activeforeground='white',cursor="hand2",command=self.login)
    btn_login.place(x=63,y=390)

    # date time method 
  def update_time(self):
    self.time_label.config(text=datetime.now().strftime("""Date: %B %d,%Y      Time: %I:%M:%S %p"""))
    self.time_label.after(1000, self.update_time)

  # open customer registration window
  def register_window(self):
    self.new_window = Toplevel(self.window)
    self.app = Register(self.new_window)

  # open driver registration window
  def open_driver_registration(self):
    self.reg_div = Toplevel(self.window)
    self.rr= Driver_register(self.reg_div)

  # open driver dashboard  
  def driver_window(self,email):
    self.driver_win = Toplevel(self.window)
    self.dd = Driver(self.driver_win,email)

  # open admin dashboard
  def admin_dash_window(self):
    self.d_win = Toplevel(self.window)
    self.ad_window = Admin_dashboard(self.d_win)

  # open trip booking window
  def trip_booking_window(self,email):
    self.trip_book = Toplevel(self.window)
    self.ttb = Booking(self.trip_book,email)

    
# -------------------------------------------------------------------------------
# method to show and hide password
  def show_pass(self):
    if self.entry_pass.cget('show')=='*':
      self.entry_pass.config(show = '')
    else:
      self.entry_pass.config(show = '*')

  # method to connect database 
  def connection(self):
    conn = mysql.connector.connect(host = 'localhost', user ='root',password ='Phurwa@807',database = 'pcps_python')
    return conn  

#  method to update password for forgot password
  def update_pass(self):
    # ----validations------
    if self.forgot_usertype.get()=='select usertype':
      messagebox.showerror('error','provide your user type',parent=self.root)
      
    elif self.comb_qsn.get()=='select':
      messagebox.showerror('error','select the Security question',parent=self.root)

    elif self.entry_ans.get()=="":
      messagebox.showerror('error','enter the answer',parent=self.root)

    elif self.entry_password.get()=="":
      messagebox.showerror("error",'enter the new password',parent=self.root)
    else:
      conn= self.connection()
      my_cursor = conn.cursor()   #initialize cusor
      if self.forgot_usertype.get()=='Customer':
              query = ("select * from customer where email =%s and security_q=%s and security_a=%s")
              value = (self.var_email.get(),self.comb_qsn.get(),self.entry_ans.get())
      elif self.forgot_usertype.get()=='Driver':
              query = ("select * from driver where email =%s and security_q=%s and security_a=%s")
              value = (self.var_email.get(),self.comb_qsn.get(),self.entry_ans.get())
     
      my_cursor.execute(query,value)
      row = my_cursor.fetchone()

      if row == None:
        messagebox.showerror("error",'please enter the correct answer',parent=self.root)
      else:
        if self.forgot_usertype.get()=='Customer':

          # query to update password of customer
          query2 = ('update customer set password =%s where email = %s')
          value2= (self.entry_password.get(),self.entry_email.get())
        elif self.forgot_usertype.get()=='Driver':

          # query to update password of driver
          query2 = ('update driver set password =%s where email = %s')
          value2= (self.entry_password.get(),self.entry_email.get())

        my_cursor.execute(query2,value2)
        conn.commit()
        conn.close()
        messagebox.showinfo("Info","Your password has been reset, please login with new password",parent=self.root)

# method for forget pass window
  def forgot_pass_win(self):
    # validations
    if self.var_email.get()=='':
      messagebox.showerror("Error","Email required",parent= self.window)
    elif self.var_cmbusertype.get() == 'Select UserType':
      messagebox.showerror("Error","UserType required",parent= self.window)
    elif self.var_cmbusertype.get() == 'Admin':
      messagebox.showerror("Erro","Admin Password cannot be reset",parent=self.window)
    else:
      conn= self.connection()
      my_cursor = conn.cursor(buffered=True)
      if self.var_cmbusertype.get()=='Customer':
        query = ("select * from customer where email =%s")
        value = (self.entry_email.get(),)
      elif self.var_cmbusertype.get()=='Driver':
        query = ("select * from driver where email =%s")
        value = (self.entry_email.get(),)
      my_cursor.execute(query,value)
      row = my_cursor.fetchone()

      #check if email is valid
      if row == None:
        messagebox.showerror("email error","Please provide valid information")
      else:
        conn.close()
        #create new window
        self.root = Toplevel()    
        self.root.title("reset password")
        self.root.geometry("310x365+500+200")
        self.root.config(bg='black')

        # labels,entryfields and combobox
        lbl_pass_title = Label(self.root,text='Forgot Password',font=("Arial",16,'bold'),fg='#19BA93',bg='black')
        lbl_pass_title.place(x=68,y=10)

        self.forgot_usertype = ttk.Combobox(self.root, font=('Arial',11,'bold'),width=16,state='readonly')
        self.forgot_usertype['values']= ('select usertype','Driver','Customer')
        self.forgot_usertype.current(0)
        self.forgot_usertype.place(x=80,y=50)

        lbl_qsn = Label(self.root,text= 'select security question',font=('Arial',13,'bold'),fg='white',bg='black')
        lbl_qsn.place(x=50,y=90)

        self.comb_qsn = ttk.Combobox(self.root, font=('Arial',11,'bold'),width=22,state='readonly')
        self.comb_qsn['values']= ('select','your favrioute place','your favrioute food','your favrioute movie')
        self.comb_qsn.current(0)
        self.comb_qsn.place(x=53,y=120)
   
        lbl_ans = Label(self.root,text= 'security answer',font=('Arial',13,'bold'),fg='white',bg='black')
        lbl_ans.place(x=50,y=160)

        self.entry_ans = Entry(self.root, width=24,font=('Arial',11,'bold'),border=0)
        self.entry_ans.place(x=53,y=190)

        lbl_new_password = Label(self.root,text= 'new password',font=('Arial',13,'bold'),fg='white',bg='black')
        lbl_new_password.place(x=50,y=225)

        self.entry_password = Entry(self.root, width=24,show='*',font=('Arial',11,'bold'),border=0)
        self.entry_password.place(x=53,y=255)

        #button
        btn_reset_pass = Button(self.root,text='reset',font=('Arial',13,'bold'),fg='white',bg='#19BA93',border=0,padx=23,pady=4,activebackground='#19BA93',activeforeground='white',cursor='hand2',command =self.update_pass)
        btn_reset_pass.place(x=100,y=300)

  # method to login to the system
  def login(self):
    email = self.var_email.get()    #initialze email
    # validations
    if self.var_email.get() == "":
      messagebox.showerror("Error","Enter your Email First")

    elif self.var_password.get() == "":
      messagebox.showerror("Error","Password is Required")

    elif self.var_cmbusertype.get() == "Select UserType":
      messagebox.showerror("Error","Usertype is Required")

    else:
      try:
        conn= self.connection()
        my_cursor = conn.cursor(buffered=True)
        if self.var_cmbusertype.get()=='Customer':
          # query to check email and password of customer
          my_cursor.execute("select * from customer where email = %s and password = %s",(
                                                                              self.var_email.get(),
                                                                              self.var_password.get(),                                                                     
                                                                                ))
        elif self.var_cmbusertype.get()=='Driver':
          # query to check email and password of driver
          my_cursor.execute("select * from driver where email = %s and password = %s",(
                                                                              self.var_email.get(),
                                                                              self.var_password.get()                                                                            
                                                                                ))

        elif self.var_cmbusertype.get()=='Admin':
          # query to check email and password of admin
          my_cursor.execute("select * from taxi_admin where email = %s and password = %s",(
                                                                              self.var_email.get(),
                                                                              self.var_password.get(),
                                                                                ))

        row = my_cursor.fetchone()
        # check if email and password is valid
        if row == None:
          messagebox.showerror("Error","Invalid email, Password or usertype")
        else:
          if self.var_cmbusertype.get() == 'Customer':

            # query to fetch fullname of customer to display 
            full_name = my_cursor.execute("select full_name from customer where email = '%s'" %(self.var_email.get()))
            my_cursor.execute(full_name)
            name_cus = my_cursor.fetchone()[0]
            messagebox.showinfo("success",f"Welcome {name_cus}")

            self.trip_booking_window(email)     #open booking dashboard

          elif self.var_cmbusertype.get() == 'Driver':

            # query to fetch fullname of customer to display
            full_name = my_cursor.execute("select full_name from driver where email = '%s'" %(self.var_email.get()))
            my_cursor.execute(full_name)
            name_driv = my_cursor.fetchone()[0]
            messagebox.showinfo("success",f"Welcome {name_driv}")

            self.driver_window(email)   #open driver dashboard
 
          elif self.var_cmbusertype.get() == 'Admin':
            messagebox.showinfo('Success','Welcome Admin')    
            self.admin_dash_window()      #open admin dashboard

          self.clear()    #clear all fields
        conn.commit()
        conn.close()
        
      except Exception as e:
        messagebox.showerror("Error",f"Due to {str(e)}",parent=self.window)
    
  # method to clear all fields
  def clear(self):
    self.var_cmbusertype.set('Select UserType')
    self.var_email.set('')
    self.var_password.set('')


# main fuction and creating object
def main():
  window = Tk()
  app = Login_Page(window)
  window.mainloop()

if __name__ == '__main__':
  main()
