from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import re 

class Driver_register:
  #initialize window
  def __init__(self,reg):    
    self.reg = reg
    self.reg.title("Driver Registration")
    self.reg.geometry("1400x700+0+0")
    self.reg.state('zoomed')

    # textvariables
    self.var_driver_id =IntVar()
    self.var_fullname = StringVar()
    self.var_email = StringVar()
    self.var_address = StringVar()
    self.var_contact = StringVar()
    self.var_qsn = StringVar()
    self.var_ans = StringVar()
    self.var_password = StringVar()
    self.var_confirm_password = StringVar()
    self.var_lisence = StringVar()
    self.a = BooleanVar()

    # set background image in window
    my_bg = Image.open(r'C:\Users\asus\Desktop\book_taxi\image\hk.jpg').resize((1300,900))
    self.bg = ImageTk.PhotoImage(my_bg)
    lbl_bg = Label(self.reg, image= self.bg)
    lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


    # initialize frame1
    frame_1 = Frame(self.reg,bg='black')
    frame_1.place(x=330 , y=65, width = 590, height=475)

    # frame 2 inside frame1 for title
    frame_2 = Frame(frame_1,bg='#19BA93')
    frame_2.place(x=0 , y=0, width = 590, height=50)

    # label for title
    lbl_title = Label(frame_2,text= 'Sign up', font =('New Times Roman',16,'bold'),fg='white',bg='#19BA93')
    lbl_title.place(x=258,y=13)

    #labels and entry fields for sign up
    lbl_fullname = Label(frame_1,text='Fullname',font=('Arial',13,'bold'),fg='white',bg='black')
    lbl_fullname.place(x=60,y=70)

    self.entry_fullname = Entry(frame_1, textvariable=self.var_fullname, width=24,font=('Arial',11,'bold'),border=0)
    self.entry_fullname.place(x=60,y=100)

    # # call back and validation register
    validate_name= self.reg.register(self.checkname)
    self.entry_fullname.config(validate='key',validatecommand=(validate_name,'%P'))

    lbl_email = Label(frame_1,text='Email',font=('Arial',13,'bold'),fg='white',bg='black')
    lbl_email.place(x=335,y=70)

    self.entry_email = Entry(frame_1, textvariable= self.var_email, width=24,font=('Arial',11,'bold'),border=0)
    self.entry_email.place(x=335,y=100)

    lbl_address = Label(frame_1,text='Address',font=('Arial',13,'bold'),fg='white',bg='black')
    lbl_address.place(x=60,y=140)

    self.entry_address = Entry(frame_1, textvariable=self.var_address, width=24,font=('Arial',11,'bold'),border=0)
    self.entry_address.place(x=60,y=170)

    lbl_contact = Label(frame_1,text='Contact No',font=('Arial',13,'bold'),fg='white',bg='black')
    lbl_contact.place(x=335,y=140)

    self.entry_contact = Entry(frame_1, textvariable= self.var_contact, width=24,font=('Arial',11,'bold'),border=0)
    self.entry_contact.place(x=335,y=170)

    # # call back and validation contact
    validate_contact= self.reg.register(self.checkcontact)
    self.entry_contact.config(validate='key',validatecommand=(validate_contact,'%P'))

    lbl_qsn = Label(frame_1,text= 'Select security question',font=('Arial',13,'bold'),fg='white',bg='black')
    lbl_qsn.place(x=60,y=210)

    self.comb_qsn = ttk.Combobox(frame_1, textvariable=self.var_qsn, font=('Arial',11,'bold'),width=22,state='readonly')
    self.comb_qsn['values']= ('select','your favrioute place','your favrioute food','your favrioute movie')
    self.comb_qsn.current(0)
    self.comb_qsn.place(x=60,y=240)

    lbl_ans = Label(frame_1,text= 'Security answer',font=('Arial',13,'bold'),fg='white',bg='black')
    lbl_ans.place(x=335,y=210)

    self.entry_ans = Entry(frame_1,textvariable= self.var_ans, width=24,font=('Arial',11,'bold'),border=0)
    self.entry_ans.place(x=335,y=240)

    lbl_password = Label(frame_1,text= 'Password',font=('Arial',13,'bold'),fg='white',bg='black')
    lbl_password.place(x=60,y=280)

    self.entry_password = Entry(frame_1, textvariable= self.var_password, width=24,show='*',font=('Arial',11,'bold'),border=0)
    self.entry_password.place(x=60,y=310)

    lbl_confirm_password = Label(frame_1,text= 'Confirm password',font=('Arial',13,'bold'),fg='white',bg='black')
    lbl_confirm_password.place(x=335,y=280)

    self.entry_confirm_password = Entry(frame_1, textvariable= self.var_confirm_password, width=24,show='*',font=('Arial',11,'bold'),border=0)
    self.entry_confirm_password.place(x=335,y=310)

    lbl_lisence = Label(frame_1,text= 'Lisence No',font=('Arial',13,'bold'),fg='white',bg='black')
    lbl_lisence.place(x=60,y=350)

    self.entry_lisence = Entry(frame_1, textvariable=self.var_lisence, width=24,font=('Arial',11,'bold'),border=0)
    self.entry_lisence.place(x=60,y=380)

    # # call back and validation contact
    validate_license= self.reg.register(self.checklicense)
    self.entry_lisence.config(validate='key',validatecommand=(validate_license,'%P'))

    # Buttons
    btn_reset = Button(frame_1,text='Reset',font=('Arial',13,'bold'),fg='white',bg='#F84040',border=0,padx=40,pady=3,activebackground='#F84040',activeforeground='white',cursor= 'hand2',command= self.clear_data)
    btn_reset.place(x=415,y=423)

    btn_save = Button(frame_1,text='Save',font=('Arial',13,'bold'),fg='white',bg='#19BA93',border=0,padx=40,pady=3,activebackground='#19BA93',activeforeground='white',cursor= 'hand2',command= self.register_data)
    btn_save.place(x=235,y=423)

    btn_login_back = Button(frame_1,text='Back',font=('Arial',13,'bold'),fg='white',border=0,cursor= 'hand2',bg='orange',padx=40,pady=3,activebackground='orange',activeforeground='white',command=self.back_login)
    btn_login_back.place(x=50,y=423)

  # fuction to check validation in fullname
  def checkname(self,fullname):
    if re.match("^(?=[A-Z])[A-Za-z\s]*(?:\s(?=[A-Z])[A-Za-z\s]*)*$",fullname):
      return True
    elif fullname=='':
      return True
    else:
      messagebox.showerror("Invalid", 'First letter should be in UpperCase and You Cannot enter numbers/special charaters', parent=self.reg)
      return False
 
  # fuction to check validation in contact
  def checkcontact(self,contact):
    if contact.isdigit():
      return True
    if len(str(contact))==0:
      return True
    else:
      messagebox.showerror("Invalid",'Invalid Entry!! Character are not allowed',parent=self.reg)
      return False

  # fuction to check validation in license
  def checklicense(self,license):
    if license.isdigit():
      return True
    if len(str(license))==0:
      return True
    else:
      messagebox.showerror("Invalid",'Invalid Entry!! Character are not allowed',parent=self.reg)
      return False
  # logout fuction
  def back_login(self):
    self.reg.destroy()

  #method to check email validation
  def checkemail(self,email):
    if len(email)>7:
      if re.match('^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$', email):
        return True
      else:
        messagebox.showerror('Alert','Invalid email enter valid user email (example: pramesh@gmail.com)',parent=self.reg)
        return False
    else:
      messagebox.showerror('Invalid','Email length is too small',parent=self.reg)

  # connect_database function
  def connection(self):
    conn = mysql.connector.connect(host = 'localhost', user ='root',password ='Phurwa@807',database = 'pcps_python')
    return conn 

  # method to check validation and save user info
  def register_data(self):

    #validations
    if self.var_fullname.get()=='':
      messagebox.showerror('Error','Enter full Name',parent=self.reg)
    elif self.var_email.get()=='':
      messagebox.showerror('Error','Enter email',parent=self.reg)
    elif self.var_address.get()=='':
      messagebox.showerror('Error','Enter address',parent=self.reg)
    elif self.var_contact.get()=='':
      messagebox.showerror('Error','Enter contact no',parent=self.reg)
    elif len(self.var_contact.get())!= 10:
      messagebox.showerror("Error",'Contact no must be of 10 digit',parent=self.reg)
    elif self.var_qsn.get()=='select':
      messagebox.showerror('Error','select security question',parent=self.reg)
    elif self.var_ans.get()=='':
      messagebox.showerror('Error','enter security answer',parent=self.reg)
    elif self.var_password.get()=='':
      messagebox.showerror('Error','Enter password',parent=self.reg)
    elif self.var_confirm_password.get()=='':
      messagebox.showerror('Error','Enter confirm password',parent=self.reg)
    elif self.var_lisence.get()=='':
      messagebox.showerror('Error','Provide your lisence No',parent=self.reg)
    elif len(self.var_lisence.get())!=7:
      messagebox.showerror("Error",'License no must be of 7 digits',parent=self.reg)
    elif self.var_password.get()!= self.var_confirm_password.get():
      messagebox.showerror("Error",'password and confirm password must be same',parent=self.reg)
    elif self.var_email.get() != None:
      self.a=self.checkemail(self.var_email.get())

    if (self.a == True):
      try:
        conn= self.connection()
        my_cursor = conn.cursor()       #initialze cursor

        # checks if email is already registered
        query = ('select * from driver where email = %s')
        values = (self.var_email.get(),)
        my_cursor.execute(query,values)
        row = my_cursor.fetchone()
        if row != None:
          messagebox.showerror("Error","Driver already exist, please use another email",parent=self.reg)
        else:
          #query to save data in driver table
          my_cursor.execute('insert into driver values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                      self.var_driver_id.get(),
                                                                      self.var_fullname.get(),
                                                                      self.var_email.get(),
                                                                      self.var_address.get(),
                                                                      self.var_contact.get(),
                                                                      self.var_qsn.get(),
                                                                      self.var_ans.get(),
                                                                      self.var_password.get(),
                                                                      self.var_lisence.get(),
                                                                      'Available',
                                                                      'Not Approved'
                                                                                   ))      
          conn.commit()
          conn.close()
          messagebox.showinfo('Success','saved successfully',parent=self.reg)
          self.clear_data()

      except Exception as e:
        messagebox.showerror("Error",f"Due to {str(e)}",parent=self.reg)
            
# method to clear all fields
  def clear_data(self):
    self.var_fullname.set('')
    self.var_email.set('')
    self.var_contact.set('')
    self.var_address.set('')
    self.var_qsn.set('Select')
    self.var_ans.set('')
    self.var_password.set('')
    self.var_confirm_password.set('')
    self.var_lisence.set('')


      
# main function and creating object
if __name__ == '__main__':
  reg = Tk()
  dd_reg = Driver_register(reg)
  reg.mainloop()

