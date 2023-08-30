from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import re

# Define a class for the customer registraion window
class Register:

  #initialize window
  def __init__(self,my_win):    
    self.my_win = my_win
    self.my_win.title("Online Taxi Booking system")
    self.my_win.geometry("1400x700+0+0")
    self.my_win.state('zoomed')

  # Initialize textvariables
    self.var_customer_id =IntVar()
    self.var_fullname = StringVar()
    self.var_email = StringVar()
    self.var_address = StringVar()
    self.var_contact = StringVar()
    self.var_qsn = StringVar()
    self.var_ans = StringVar()
    self.var_password = StringVar()
    self.var_confirm_password = StringVar()
    self.var_payment_method = StringVar()
    self.a = BooleanVar()
# ---------------------------------------------------------------------------------------------------------
    # set background image in window
    my_bg = Image.open(r'image\hk.jpg').resize((1300,900))
    self.bg = ImageTk.PhotoImage(my_bg)
    lbl_bg = Label(self.my_win, image= self.bg)
    lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

# --------------------------------------------------------------------------------------------------
    # initialize frame1
    frame_1 = Frame(self.my_win,bg='black')
    frame_1.place(x=330 , y=65, width = 590, height=490)
# -------------------------------------------------------
    # frame 2 inside frame1 for title
    frame_2 = Frame(frame_1,bg='#19BA93')
    frame_2.place(x=0 , y=0, width = 590, height=50)

  # label for title
    lbl_title = Label(frame_2,text= 'Sign up', font =('New Times Roman',16,'bold'),fg='white',bg='#19BA93')
    lbl_title.place(x=258,y=13)
# -------------------------------------------------------

    #labels and entry fields for sign up
    lbl_fullname = Label(frame_1,text='Fullname',font=('Arial',13,'bold'),fg='white',bg='black')
    lbl_fullname.place(x=60,y=70)

    self.entry_fullname = Entry(frame_1,textvariable=self.var_fullname, width=24,font=('Arial',11,'bold'),border=0)
    self.entry_fullname.place(x=60,y=100)

    # # call back to validate fullname
    validate_name= self.my_win.register(self.checkname)
    self.entry_fullname.config(validate='key',validatecommand=(validate_name,'%P'))
  # --------------------------------------------------------------------------------------------

    lbl_email = Label(frame_1,text='Email',font=('Arial',13,'bold'),fg='white',bg='black')
    lbl_email.place(x=335,y=70)

    self.entry_email = Entry(frame_1, textvariable= self.var_email, width=24,font=('Arial',11,'bold'),border=0)
    self.entry_email.place(x=335,y=100)
    # -------------------------------------------------------------------------------------------

    lbl_address = Label(frame_1,text='Address',font=('Arial',13,'bold'),fg='white',bg='black')
    lbl_address.place(x=60,y=140)

    self.entry_address = Entry(frame_1, textvariable=self.var_address, width=24,font=('Arial',11,'bold'),border=0)
    self.entry_address.place(x=60,y=170)
    # -------------------------------------------------------------------------------------------

    lbl_contact = Label(frame_1,text='Contact No',font=('Arial',13,'bold'),fg='white',bg='black')
    lbl_contact.place(x=335,y=140)

    self.entry_contact = Entry(frame_1, textvariable= self.var_contact, width=24,font=('Arial',11,'bold'),border=0)
    self.entry_contact.place(x=335,y=170)

    # # call back to validate contact
    validate_contact= self.my_win.register(self.checkcontact)
    self.entry_contact.config(validate='key',validatecommand=(validate_contact,'%P'))
    # ------------------------------------------------------------------------------------------- 

    lbl_qsn = Label(frame_1,text= 'Select security question',font=('Arial',13,'bold'),fg='white',bg='black')
    lbl_qsn.place(x=60,y=210)

    self.comb_qsn = ttk.Combobox(frame_1, textvariable=self.var_qsn, font=('Arial',11,'bold'),width=22,state='readonly',cursor='hand2')
    self.comb_qsn['values']= ('Select','Your favrioute place','your favrioute food','your favrioute movie')
    self.comb_qsn.current(0)
    self.comb_qsn.place(x=60,y=240)
    # -----------------------------------------------------------------------------------------------------

    lbl_ans = Label(frame_1,text= 'Security answer',font=('Arial',13,'bold'),fg='white',bg='black')
    lbl_ans.place(x=335,y=210)

    self.entry_ans = Entry(frame_1,textvariable= self.var_ans, width=24,font=('Arial',11,'bold'),border=0)
    self.entry_ans.place(x=335,y=240)
    # ------------------------------------------------------------------------------------------------------

    lbl_password = Label(frame_1,text= 'Password',font=('Arial',13,'bold'),fg='white',bg='black')
    lbl_password.place(x=60,y=280)

    self.entry_password = Entry(frame_1, textvariable= self.var_password, width=24,show='*',font=('Arial',11,'bold'),border=0)
    self.entry_password.place(x=60,y=310)
    # ------------------------------------------------------------------------------------------------------

    lbl_confirm_password = Label(frame_1,text= 'Confirm password',font=('Arial',13,'bold'),fg='white',bg='black')
    lbl_confirm_password.place(x=335,y=280)

    self.entry_confirm_password = Entry(frame_1, textvariable= self.var_confirm_password, width=24,show='*',font=('Arial',11,'bold'),border=0)
    self.entry_confirm_password.place(x=335,y=310)
    # ------------------------------------------------------------------------------------------------------

    lbl_payment_method = Label(frame_1,text= 'Payment method',font=('Arial',13,'bold'),fg='white',bg='black')
    lbl_payment_method.place(x=60,y=350)

    self.pay_method = ttk.Combobox(frame_1, textvariable=self.var_payment_method, font=('Arial',11,'bold'),width=22,state='readonly',cursor='hand2')
    self.pay_method['values']= ('Select','E-sewa','khalti','Phone Pay','Cash')
    self.pay_method.current(0)
    self.pay_method.place(x=60,y=380)
    
# ----------------------------------------------------------------------------------------
    # Buttons
    btn_reset = Button(frame_1,text='Reset',font=('Arial',13,'bold'),fg='white',bg='#F84040',border=0,padx=40,pady=3,activebackground='#F84040',activeforeground='white',cursor= 'hand2',command= self.clear_data)
    btn_reset.place(x=415,y=440)

    btn_save = Button(frame_1,text='Save',font=('Arial',13,'bold'),fg='white',bg='#19BA93',border=0,padx=40,pady=3,activebackground='#19BA93',activeforeground='white',cursor= 'hand2',command= self.register_data)
    btn_save.place(x=235,y=440)

    btn_login_back = Button(frame_1,text='Back',font=('Arial',13,'bold'),fg='white',border=0,cursor= 'hand2',bg='orange',padx=40,pady=3,activebackground='orange',activeforeground='white',command=self.back_login)
    btn_login_back.place(x=50,y=440)

  # fuction to check validation in fullname
  def checkname(self,fullname): 
    if re.match("^(?=[A-Z])[A-Za-z\s]*(?:\s(?=[A-Z])[A-Za-z\s]*)*$",fullname):
      return True
    elif fullname=='':
      return True
    else:
      messagebox.showerror("Invalid", 'First letter should be in UpperCase and You Cannot enter numbers/special charaters', parent=self.my_win)
      return False
 
  # fuction to check validation in contact
  def checkcontact(self,contact):
    if contact.isdigit():
      return True
    if len(str(contact))==0:
      return True
    else:
      messagebox.showerror("Invalid",'Invalid Entry!! Character are not allowed',parent=self.my_win)
      return False

  # logout fuction
  def back_login(self):
    self.my_win.destroy()  

  #fuction to check validation in email
  def checkemail(self,email):
    if len(email)>7:
      if re.match('^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$', email):
        return True
      else:
        messagebox.showerror('Alert','Invalid email enter valid user email (example: pramesh@gmail.com)',parent=self.my_win)
        return False
    else:
      messagebox.showerror('Invalid','Email length is too small',parent=self.my_win)

  # connect_database function
  def connection(self):
    conn = mysql.connector.connect(host = 'localhost', user ='root',password ='Phurwa@807',database = 'pcps_python')
    return conn   

  # method to check validation and save user info
  def register_data(self):
    #validation
    if self.var_fullname.get()=='':
      messagebox.showerror('Error','Enter full Name',parent=self.my_win)
    elif self.var_email.get()=='':
      messagebox.showerror('Error','Enter email',parent=self.my_win)
    elif self.var_address.get()=='':
      messagebox.showerror('Error','Enter address',parent=self.my_win)
    elif self.var_contact.get()=='':  
      messagebox.showerror('Error','Enter contact no',parent=self.my_win)
    elif len(self.var_contact.get())!= 10:
      messagebox.showerror("Error",'Contact no must be of 10 digit',parent=self.my_win)
    elif self.var_qsn.get()=='Select':
      messagebox.showerror('Error','select security question',parent=self.my_win)
    elif self.var_ans.get()=='':
      messagebox.showerror('Error','enter security answer',parent=self.my_win)
    elif self.var_password.get()=='':
      messagebox.showerror('Error','Enter password',parent=self.my_win)
    elif self.var_confirm_password.get()=='':
      messagebox.showerror('Error','Enter confirm password',parent=self.my_win)
    elif self.var_payment_method.get()=='Select':
      messagebox.showerror('Error','select payment meythod',parent=self.my_win)
    elif self.var_password.get()!= self.var_confirm_password.get():
      messagebox.showerror("Error",'Password Should match',parent=self.my_win)
    elif self.var_email.get() != None:
      self.a=self.checkemail(self.var_email.get())
    if (self.a == True):
      try:
        conn= self.connection()
        my_cursor = conn.cursor()    #initialize cursor

        query = ('select * from customer where email = %s')
        values = (self.var_email.get(),)
        my_cursor.execute(query,values)
        row = my_cursor.fetchone()

        # checks if email is already registered
        if row != None:
          messagebox.showerror("Error","User already exist, please use another email",parent=self.my_win)
        else:
          #query to save data in customer table
          my_cursor.execute('insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                      self.var_customer_id.get(),
                                                                      self.var_fullname.get(),
                                                                      self.var_email.get(),
                                                                      self.var_address.get(),
                                                                      self.var_contact.get(),
                                                                      self.var_qsn.get(),
                                                                      self.var_ans.get(),
                                                                      self.var_password.get(),
                                                                      self.var_payment_method.get()                                                  
                                                                                   ))      
          conn.commit()
          conn.close()      #close connection
          messagebox.showinfo('Success','saved successfully',parent=self.my_win)
          self.clear_data()   #clear all fields

      except Exception as e:
        messagebox.showerror("Error",f"Due to {str(e)}",parent=self.my_win)
            
# -------------------------------------------------------------------------------------
# fuction for clear fields
  def clear_data(self):
    self.var_fullname.set('')
    self.var_email.set('')
    self.var_contact.set('')
    self.var_address.set('')
    self.var_qsn.set('Select')
    self.var_ans.set('')
    self.var_password.set('')
    self.var_confirm_password.set('')
    self.var_payment_method.set('Select')
      
# main function and creating object
if __name__ == '__main__':
  my_win = Tk()   
  reg = Register(my_win)    
  my_win.mainloop()         

