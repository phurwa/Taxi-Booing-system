from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from request_driver import Request_list
import mysql.connector
class Driver_info:

  # initialize window
  def __init__(self,d_info):
    self.d_info= d_info
    self.d_info.title("Driver Information")
    self.d_info.geometry("800x500+300+80")
    self.view_table()

    #text_variables
    self.var_id= StringVar()

    # initialize frame1
    frame_1 = Frame(self.d_info,bg='#D5F0DD')
    frame_1.place(x=0 , y=0, width = 800, height=100)

    # labels and entryfield
    lbl_search= Label(frame_1,text="Search Driver",font=('Arial',11,'bold'),fg='black',bg='#D5F0DD')
    lbl_search.place(x=5,y=15)

    self.entry_search = Entry(frame_1,textvariable=self.var_id, width=10,font=('Arial',12,'bold'),border=1,bg="light blue")
    self.entry_search.place(x=122,y=15)

    lbl_Available= Label(frame_1,text="Available Drivers",font=('Arial',13,'bold'),fg='black',bg='#D5F0DD')
    lbl_Available.place(x=100,y=73)

    lbl_booked= Label(frame_1,text="Booked Drivers",font=('Arial',13,'bold'),fg='black',bg='#D5F0DD')
    lbl_booked.place(x=520,y=73)


    # image for reload button
    reload_img = Image.open(r'C:\Users\asus\Desktop\book_taxi\image\reload.png').resize((30,30))
    self.img_re = ImageTk.PhotoImage(reload_img)

    # buttons
    btn_reqload = Button(frame_1,image=self.img_re,border=0,cursor= 'hand2',bg='#D5F0DD',activebackground='#D5F0DD',command= self.vacant_driver_info)
    btn_reqload.place(x=380,y=62)

    btn_search = Button(frame_1,text='Search',font=('Arial',13,'bold'),fg='white',bg='#5B83F6',border=1,padx=13,pady=1,activebackground='#5B83F6',activeforeground='white',cursor='hand2',command=self.view_searched_drivers)
    btn_search.place(x=360,y=10)

    btn_request = Button(frame_1,text='Driver Requests',font=('Arial',13,'bold'),fg='white',bg='#F86F3C',border=1,padx=30,pady=4,activebackground='#F86F3C',activeforeground='white',cursor='hand2',command=self.request_window)
    btn_request.place(x=560,y=10)


# scrollbar and treeview to display drivers
  def view_table(self):
    # frame for available driver
    frame_2 = Frame(self.d_info,bg='red')
    frame_2.place(x=0 , y=100, width = 400, height=400)

    # initialize scrollbar for available driver
    scroll_win = Scrollbar(frame_2,orient= VERTICAL)

    self.tr_vacant_driver = ttk.Treeview(frame_2,height=13,columns=("driver_id","FullName","Email","Address","Contact","Lisence","driver_status"),xscrollcommand = scroll_win.set)
    scroll_win.pack(side=RIGHT, fill=Y)

    self.tr_vacant_driver.heading("driver_id",text= "ID")
    self.tr_vacant_driver.heading("FullName",text= "FullName")
    self.tr_vacant_driver.heading("Email",text= "Email")
    self.tr_vacant_driver.heading("Address",text= "Address")
    self.tr_vacant_driver.heading("Contact",text= "Contact")
    self.tr_vacant_driver.heading("Lisence",text= "Lisence")
    self.tr_vacant_driver.heading("driver_status",text= "driver_status")
    self.tr_vacant_driver['show'] = 'headings'

    self.tr_vacant_driver.column("driver_id",width = 40)
    self.tr_vacant_driver.column("FullName",width = 100)
    self.tr_vacant_driver.column("Email",width = 120)
    self.tr_vacant_driver.column("Address",width = 100)
    self.tr_vacant_driver.column("Contact",width = 100)
    self.tr_vacant_driver.column("Lisence",width = 100)
    self.tr_vacant_driver.column("driver_status",width = 100)
    
    self.tr_vacant_driver.pack(fill=BOTH, expand=1)
    self.vacant_driver_info()     #display available driver in frame1 treeview 



    # initialize frame and scrollbar for available driver
    frame_3 = Frame(self.d_info,bg='blue')
    frame_3.place(x=400 , y=100, width = 400, height=400)

    scroll_win_2 = Scrollbar(frame_3,orient= VERTICAL)

    self.tr_driver = ttk.Treeview(frame_3,height=13,columns=("driver_id","FullName","Email","Address","Contact","Lisence","driver_status"),xscrollcommand = scroll_win.set)
    scroll_win_2.pack(side=RIGHT, fill=Y)

    self.tr_driver.heading("driver_id",text= "ID")
    self.tr_driver.heading("FullName",text= "FullName")
    self.tr_driver.heading("Email",text= "Email")
    self.tr_driver.heading("Address",text= "Address")
    self.tr_driver.heading("Contact",text= "Contact")
    self.tr_driver.heading("Lisence",text= "Lisence")
    self.tr_driver.heading("driver_status",text= "driver_status")
    self.tr_driver['show'] = 'headings'

    self.tr_driver.column("driver_id",width = 40)
    self.tr_driver.column("FullName",width = 100)
    self.tr_driver.column("Email",width = 120)
    self.tr_driver.column("Address",width = 100)
    self.tr_driver.column("Contact",width = 100)
    self.tr_driver.column("Lisence",width = 100)
    self.tr_driver.column("driver_status",width = 100)
    
    self.tr_driver.pack(fill=BOTH, expand=1)
    self.assigned_driver()      #display assigned driver in frame 2 treeview


# functions

  # method to connect database
  def connection(self):
    conn = mysql.connector.connect(host = 'localhost', user ='root',password ='Phurwa@807',database = 'pcps_python')
    return conn

  # open request driver window
  def request_window(self):
    self.r_wind = Toplevel(self.d_info)
    self.r_w = Request_list(self.r_wind)
 
  # method to display searched driver
  def view_searched_drivers(self):

    # validation
    if self.var_id.get()=='':
      messagebox.showerror('Error','Search By Driver ID',parent=self.d_info)
    else:
      try:
        conn = self.connection()
        my_cursor = conn.cursor()     #initialize cursor

        # query to fetch searched driver data
        my_cursor.execute("select driver_id,full_name,email,address,contact,license_no,driver_status from driver where driver_id = %s",(self.var_id.get(),))
        search_driv= my_cursor.fetchall()
        if len(search_driv) != 0:
          self.tr_vacant_driver.delete(*self.tr_vacant_driver.get_children())
          for row in search_driv:
            self.tr_vacant_driver.insert("", END,values = row)
        else:
          messagebox.showinfo('Message','Driver Not Found',parent=self.d_info)
        self.var_id.set('')     #clear field
      except Exception as e:
          messagebox.showerror("Error",f"Due to {str(e)}",parent=self.d_info)

  # method to display available driver 
  def vacant_driver_info(self):
    try:
      conn = self.connection()
      my_cursor = conn.cursor()       #initialize cursor

      # query to fetch driver data of driver with driver_status available 
      my_cursor.execute("select driver_id,full_name,email,address,contact,license_no,driver_status from driver where driver_status = 'Available' and request_status = 'Approved' ")
      vac_driv= my_cursor.fetchall()
      if len(vac_driv) != 0:
        self.tr_vacant_driver.delete(*self.tr_vacant_driver.get_children())
        for row in vac_driv:
          self.tr_vacant_driver.insert("", END,values = row)

    except Exception as e:
        messagebox.showerror("Error",f"Due to {str(e)}",parent=self.d_info)

  # method to display assigned driver
  def assigned_driver(self):
    try:
      conn = self.connection()
      my_cursor = conn.cursor()     #initialize cursor

      # query to fetch driver data with driver status assigned
      my_cursor.execute("select driver_id,full_name,email,address,contact,license_no,driver_status from driver where driver_status = 'Assigned'")
      ass_driv= my_cursor.fetchall()
      if len(ass_driv) != 0:
        self.tr_driver.delete(*self.tr_driver.get_children())
        for row in ass_driv:
          self.tr_driver.insert("", END,values = row)

    except Exception as e:
        messagebox.showerror("Error",f"Due to {str(e)}",parent=self.d_info)

  
# main function and creating object
if __name__ == '__main__':
  d_info = Tk()
  details_driver = Driver_info(d_info)
  details_driver.vacant_driver_info()     #call method 
  details_driver.assigned_driver()        #call method
  d_info.mainloop()