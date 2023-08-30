from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from datetime import datetime  
from tkcalendar import Calendar, DateEntry
import mysql.connector

class Booking:
  #initialize window
  def __init__(self,book,email):      
    self.book = book
    self.book.title("Trip Booking")
    self.book.geometry("1400x700+0+0")
    self.book.state("zoomed")
    self.book.config(bg="white")

  # Initialize textvariables and lists
    self.var_booking_id = IntVar()
    self.var_pickup_place = StringVar()
    self.var_dropoff_place = StringVar()
    self.var_pickup_date = StringVar()
    self.var_dropoff_date = StringVar()
    self.var_pickup_time = StringVar()
    self.var_dropoff_time = StringVar()
    self.var_driver_id = IntVar()
    self.email= email
    self.var_time_list= ["12:00 AM", "12:30 AM", "1:00 AM", "1:30 AM", "2:00 AM", "2:30 AM", "3:00 AM", "3:30 AM", "4:00 AM", "4:30 AM", "5:00 AM", "5:30 AM", "6:00 AM", "6:30 AM", "7:00 AM", "7:30 AM", "8:00 AM", "8:30 AM", "9:00 AM", "9:30 AM", "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM", "12:00 PM", "12:30 PM", "1:00 PM", "1:30 PM", "2:00 PM", "2:30 PM", "3:00 PM", "3:30 PM", "4:00 PM", "4:30 PM", "5:00 PM", "5:30 PM", "6:00 PM", "6:30 PM", "7:00 PM", "7:30 PM", "8:00 PM", "8:30 PM", "9:00 PM", "9:30 PM", "10:00 PM", "10:30 PM", "11:00 PM", "11:30 PM"]

    self.view_table()

  
    # initialize frame1
    frame_1 = Frame(self.book,bg='black')
    frame_1.place(x=0 , y=0, width = 590, height=700)

    my_bg = Image.open(r'image\book_trip.png').resize((590,700))
    self.bg = ImageTk.PhotoImage(my_bg)
    lbl_bg = Label(frame_1, image= self.bg)
    lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

    # Create a TimeLabel object
    self.time_label = Label(frame_1, text="",font=("Arial",11,'bold'),bg='#4EC4B2',fg='black',width=34,height=1)
    self.time_label.place(x=130,y=5)

    self.update_time()    
    # -------------------------------------------------------------------------------

    # frame for logout fuction
    frame_3 = Frame(self.book,bg='#4EC4B2')
    frame_3.place(x=10 , y=20, width = 80, height=90)

    log_img = Image.open(r'image\logout.png').resize((60,60))
    self.l_img = ImageTk.PhotoImage(log_img)
   
    btn_logout = Button(frame_3,image=self.l_img,border=0,cursor= 'hand2',bg='#4EC4B2',activebackground='#4EC4B2',command= self.logout)
    btn_logout.place(x=5,y=5)

    lbl_logout = Label(frame_3,text= 'Logout',font=('Arial',11,'bold'),fg='red',bg='#4EC4B2')
    lbl_logout.place(x=9,y=63)
    # ------------------------------------------------------------------------------

    # frame for entry fields and buttons
    frame_2 = Frame(self.book,bg='#D5F0DD')
    frame_2.place(x=590 , y=0, width = 690, height=270)

      # --------labels-------------------------------
    lbl_pickup_place = Label(frame_2,text='Pickup Address',font=('Arial',13,'bold'),fg='black',bg='#D5F0DD')
    lbl_pickup_place.place(x=15,y=30)

    self.entry_pickup_place = ttk.Combobox(frame_2, textvariable=self.var_pickup_place, font=('Arial',11,'bold'),width=21,state='readonly',cursor='hand2')
    self.entry_pickup_place['values']= ('Select','Kathmandu','Lalitpur','Bouddha','Baneshwor','Bhaktapur','Dharan','Pokhara','Mustang','Jhapa','Illam','Butwal','Hetauda','Bagmati','Jhagdol')
    self.entry_pickup_place.current(0)
    self.entry_pickup_place.place(x=15,y=60)

    lbl_dropoff_place = Label(frame_2,text='Dropoff Address',font=('Arial',13,'bold'),fg='black',bg='#D5F0DD')
    lbl_dropoff_place.place(x=265,y=30)

    self.entry_dropoff_place = ttk.Combobox(frame_2, textvariable=self.var_dropoff_place, font=('Arial',11,'bold'),width=21,state='readonly',cursor='hand2')
    self.entry_dropoff_place['values']= ('Select','Patan','Thamel','Bouddha','Baneshwor','Pokhara','Mustang','Kathmandu','Lalitpur','Bhaktapur','Dharan','Jhapa','Illam','Butwal','Manang','Balkumari')
    self.entry_dropoff_place.current(0)
    self.entry_dropoff_place.place(x=265,y=60)

    lbl_pickup_date = Label(frame_2,text='Pickup Date',font=('Arial',13,'bold'),fg='black',bg='#D5F0DD')
    lbl_pickup_date.place(x=15,y=100) 
    
    self.entry_pickup_date=DateEntry(frame_2, textvariable=self.var_pickup_date, font=("Arail",13),bg="light blue",width=19)
    self.entry_pickup_date.place(x=15, y=130)

    lbl_dropoffdate = Label(frame_2,text='Dropoff Date',font=('Arial',13,'bold'),fg='black',bg='#D5F0DD')
    lbl_dropoffdate.place(x=265,y=100) 

    self.entry_dropoff_date=DateEntry(frame_2, textvariable=self.var_dropoff_date, font=("Arail",13),bg="light blue",width=19)
    self.entry_dropoff_date.place(x=265, y=130)

    lbl_pickup_time = Label(frame_2,text='Pickup Time',font=('Arial',13,'bold'),fg='black',bg='#D5F0DD')
    lbl_pickup_time.place(x=15,y=175) 

    self.entry_pickup_time = ttk.Combobox(frame_2, textvariable=self.var_pickup_time, values=self.var_time_list,font=('Arial',11,'bold'),width=21,state='readonly',cursor='hand2')
    self.entry_pickup_time.current(0)
    self.entry_pickup_time.place(x=15,y=205)

    lbl_dropoff_time = Label(frame_2,text='Drop off Time',font=('Arial',13,'bold'),fg='black',bg='#D5F0DD')
    lbl_dropoff_time.place(x=265,y=176) 

    self.entry_dropff_time = ttk.Combobox(frame_2, textvariable=self.var_dropoff_time, values=self.var_time_list,font=('Arial',11,'bold'),width=21,state='readonly',cursor='hand2')
    self.entry_dropff_time.current(0)
    self.entry_dropff_time.place(x=265,y=205)

    # buttons
    btn_view = Button(frame_2,text='View',font=('Arial',13,'bold'),fg='black',bg='orange',border=1,height=1,width=14,activebackground='orange',activeforeground='black',cursor= 'hand2',command=self.display_data)
    btn_view.place(x=520,y=40)

    btn_book = Button(frame_2,text='Book',font=('Arial',13,'bold'),fg='black',bg='orange',border=1,height=1,width=14,activebackground='orange',activeforeground='black',cursor= 'hand2',command=self.add_data)
    btn_book.place(x=520,y=95)

    btn_update = Button(frame_2,text='Update',font=('Arial',13,'bold'),fg='black',bg='orange',border=1,height=1,width=14,activebackground='orange',activeforeground='black',cursor= 'hand2',command=self.update_data)
    btn_update.place(x=520,y=150)

    btn_delete = Button(frame_2,text='Cancel',font=('Arial',13,'bold'),fg='black',bg='orange',border=1,height=1,width=14,activebackground='orange',activeforeground='black',cursor= 'hand2',command=self.delete_data)
    btn_delete.place(x=520,y=205)
# ----------------------------------------------------------------------------------------
    # date time method 
  def update_time(self):
    self.time_label.config(text=datetime.now().strftime("""Date: %B %d,%Y      Time: %I:%M:%S %p"""))
    self.time_label.after(1000, self.update_time)


  def view_table(self):
    # frame for tree view
    frame_4 = Frame(self.book,bg='grey')
    frame_4.place(x=590 , y=270, width = 690, height=380)

   # ------------scrollbar and treeview--------------------------------
    scroll_win = Scrollbar(frame_4,orient= VERTICAL)

    self.tr_booking = ttk.Treeview(frame_4,height=15,columns=("booking_id","pickup_address","dropoff_address","pickup_date","dropoff_date","pickup_time","dropoff_time","booking_status","user_id"),xscrollcommand = scroll_win.set)
    scroll_win.pack(side=RIGHT, fill=Y)

    self.tr_booking.heading("booking_id",text= "booking_id")
    self.tr_booking.heading("pickup_address",text= "pickup_address")
    self.tr_booking.heading("dropoff_address",text= "dropoff_address")
    self.tr_booking.heading("pickup_date",text= "pickup_date")
    self.tr_booking.heading("dropoff_date",text= "dropoff_date")
    self.tr_booking.heading("pickup_time",text= "pickup_time")
    self.tr_booking.heading("dropoff_time",text= "dropoff_time")
    self.tr_booking.heading("booking_status",text= "booking_status")
    self.tr_booking.heading("user_id",text= "user_id")

    self.tr_booking['show'] = 'headings'

    self.tr_booking.column("booking_id",width = 100)
    self.tr_booking.column("pickup_address",width = 110)
    self.tr_booking.column("dropoff_address",width = 110)
    self.tr_booking.column("pickup_date",width = 110)
    self.tr_booking.column("dropoff_date",width = 110)
    self.tr_booking.column("pickup_time",width = 110)
    self.tr_booking.column("dropoff_time",width = 110)
    self.tr_booking.column("booking_status",width = 110)
    self.tr_booking.column("user_id",width = 110)

    self.tr_booking.pack(fill=BOTH, expand=1)
    self.tr_booking.bind("<ButtonRelease-1>",self.tree_click)

# -----------------functions-----------------------------------------
  # connect_database function
  def connection(self):
    conn = mysql.connector.connect(host = 'localhost', user ='root',password ='Phurwa@807',database = 'pcps_python')
    return conn

  # logout fuction
  def logout(self):
    ilogout= messagebox.askyesno("Confirmation","Are you sure? You want to logout!",parent=self.book)
    if ilogout > 0:
      self.book.destroy()


  # treeview click data function
  def tree_click(self,event):
    data_view = self.tr_booking.focus()
    click_tree = self.tr_booking.item(data_view)
    row = click_tree['values']
    try:
      self.var_booking_id.set(row[0])
      self.var_pickup_place.set(row[1]),
      self.var_dropoff_place.set(row[2]),
      self.var_pickup_date.set(row[3]),
      self.var_dropoff_date.set(row[4]),
      self.var_pickup_time.set(row[5]),
      self.var_dropoff_time.set(row[6]), 
    except:
      pass
# -----------------------------------------------------------------
  
  # add new data
  def add_data(self):
    print(self.email)
    if self.var_pickup_place.get() == "":
      messagebox.showerror("Error", "Please Enter Pickup Address",parent=self.book)
    elif self.var_dropoff_place.get() == "":
      messagebox.showerror("Error", "Please Enter Drop off Address",parent=self.book)
    elif self.var_pickup_date.get() == "":
      messagebox.showerror("Error", "Please Enter Pickup Date",parent=self.book)
    elif self.var_dropoff_date.get() == "":
      messagebox.showerror("Error", "Please Enter Drop off Date",parent=self.book)
    elif self.var_pickup_time.get() == "":
      messagebox.showerror("Error", "Please Enter Pick up Time",parent=self.book)
    elif self.var_dropoff_time.get() == "":
      messagebox.showerror("Error", "Please Enter Drop off Time",parent=self.book)
    else:
      try:
        conn = self.connection()
        my_cursor = conn.cursor()
        user_id = my_cursor.execute("select customer_id from customer where email = '%s'" %(self.email))
        my_cursor.execute(user_id)
        cu_id = my_cursor.fetchone()[0]
        my_cursor.execute('insert into booking values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                      self.var_booking_id.get(),
                                                                      self.var_pickup_place.get(),
                                                                      self.var_dropoff_place.get(),
                                                                      self.var_pickup_date.get(),
                                                                      self.var_dropoff_date.get(),
                                                                      self.var_pickup_time.get(),
                                                                      self.var_dropoff_time.get(),
                                                                      'Pending',
                                                                      cu_id, 
                                                                      self.var_driver_id.get()                                                              
                                                                                ))      
        conn.commit()
        conn.close()
        messagebox.showinfo('Success','Trip Booked Successfully',parent=self.book)
        self.reset()    #clear the fields
        self.display_data()
      except Exception as e:
        messagebox.showerror("Error",f"Due to {str(e)}",parent=self.book)

  # method to display in treeview
  def display_data(self):
    try:
      conn = self.connection()
      my_cursor = conn.cursor(buffered=True)    #initialize cursor
      
      #query to fetch customer id 
      u_id = my_cursor.execute("select customer_id from customer where email = '%s'" %(self.email))
      my_cursor.execute(u_id)
      u_id = my_cursor.fetchone()[0]

      #query to fetch bookings
      my_cursor.execute("select * from booking where booking_status = 'Pending' and customer_id ='%s'"%(u_id))
      book_data= my_cursor.fetchall()
      if len(book_data) != 0:
        self.tr_booking.delete(*self.tr_booking.get_children())
        for row in book_data:
          self.tr_booking.insert("", END,values = row)

      conn.commit()
      conn.close()

    except Exception as e:
        messagebox.showerror("Error",f"Due to {str(e)}",parent=self.book)
      
# ------------------------------------------------------------------------------------
  # update the booking_data
  def update_data(self):
    update_messeage= messagebox.askyesno("Confirmation","Are you sure? You want to Update the Trip!",parent=self.book)
    if update_messeage > 0:
      try:
        conn = self.connection()
        my_cursor = conn.cursor(buffered=True)

        # query to update trip
        my_cursor.execute("update booking set pickup_address = %s,dropoff_address = %s,pickup_date = %s,dropoff_date=%s,pickup_time=%s,dropoff_time=%s where booking_id = %s",(
          self.var_pickup_place.get(),
          self.var_dropoff_place.get(),
          self.var_pickup_date.get(),
          self.var_dropoff_date.get(),
          self.var_pickup_time.get(),
          self.var_dropoff_time.get(),
          self.var_booking_id.get()
                                                                                                                  ))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success','Trip Updated Successfully',parent=self.book)
        self.reset()    #clear the fields
        self.display_data()
      except Exception as e:
        messagebox.showerror("Error",f"Due to {str(e)}",parent=self.book)
# ----------------------------------------------------------------------------------
  # delete data
  def delete_data(self):
  
    cancel_messeage= messagebox.askyesno("Confirmation","Are you sure? You want to Cancel the Trip!",parent=self.book)
    if cancel_messeage > 0:
      try:
          conn = self.connection()
          my_cursor = conn.cursor(buffered=True)      #initialize cursor

          # query to delete booking 
          my_cursor.execute("delete from booking where booking_id = %s",(
            self.var_booking_id.get(),
          ))
          conn.commit()
          conn.close()
          messagebox.showinfo("Message","Trip Cancelled Successfully",parent=self.book)
          self.reset()    #clear the fields
          self.view_table()
      except Exception as e:
          messagebox.showerror("Error",f"Due to {str(e)}",parent=self.book)
# --------------------------------------------------
  # method to clear fields
  def reset(self):
      self.var_pickup_place.set('Select')
      self.var_dropoff_place.set('Select')
      self.var_pickup_date.set('')
      self.var_dropoff_date.set('')
      self.var_pickup_time.set('Select')
      self.var_dropoff_time.set('Select')


# main function and creating object
if __name__ == '__main__':
  book = Tk()
  bb = Booking(book)
  book.mainloop()