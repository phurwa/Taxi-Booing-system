from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

# Define a class for the Assign Driver window
class Assign_driver:
   # Initialize the window
  def __init__(self,trip):
    self.trip = trip
    self.trip.title("Assign Driver and confirm booking")
    self.trip.geometry("700x500+300+80")

  # Initialize textvariables and list
    self.var_user_id = StringVar()
    self.var_driver_id = StringVar()
    self.var_booking_id = IntVar()
    self.drive_list = []
    self.view_table()
    self.show_driver_id()


  # Create a frame for labels, entry fields, combobox, and buttons
    frame_1 = Frame(self.trip,bg='#D5F0DD')
    frame_1.place(x=0 , y=0, width = 700, height=130)

  # Create labels and entry fields
    lbl_userID = Label(frame_1,text='Selected Customer',font=('Arial',12,'bold'),fg='black',bg='#D5F0DD')
    lbl_userID.place(x=10,y=15)

    self.entry_userID = Entry(frame_1, textvariable=self.var_user_id, width=9,font=('Arial',12,'bold'),border=1,bg="light blue",state='disabled')
    self.entry_userID.place(x=170,y=16)

    lbl_driverID = Label(frame_1,text='Availabe Drivers',font=('Arial',12,'bold'),fg='black',bg='#D5F0DD')
    lbl_driverID.place(x=420,y=15)


    # Create a combobox for selecting a driver
    self.cmb_driver_list=ttk.Combobox(frame_1, textvariable=self.var_driver_id,values=self.drive_list,state='readonly',font=("Arial",10,'bold'))
    self.cmb_driver_list.place(x=555,y=16,width=120, height=25)

    # Create a button for assigning a driver
    btn_assign = Button(frame_1,text='Assign Driver',font=('Arial',13,'bold'),fg='white',bg='#F86F3C',border=1,padx=30,pady=4,activebackground='#F86F3C',activeforeground='white',cursor='hand2',command=self.assign)
    btn_assign.place(x=250,y=80)

  # Create a frame and treeview for displaying bookings
  def view_table(self):
    # frame for tree view
    frame_2 = Frame(self.trip,bg='grey')
    frame_2.place(x=0 , y=130, width = 700, height=350)

   # ------------scrollbar and treeview--------------------------------
    scroll_win = Scrollbar(frame_2,orient= VERTICAL)

    self.tr_booking = ttk.Treeview(frame_2,height=13,columns=("booking_id","pickup_address","dropoff_address","pickup_date","dropoff_date","pickup_time","dropoff_time","booking_status","user_id","driver_id"),xscrollcommand = scroll_win.set)
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
    self.tr_booking.heading("driver_id",text= "driver_id")
    self.tr_booking['show'] = 'headings'

    self.tr_booking.column("booking_id",width = 100)
    self.tr_booking.column("pickup_address",width = 110)
    self.tr_booking.column("dropoff_address",width = 110)
    self.tr_booking.column("pickup_date",width = 110)
    self.tr_booking.column("dropoff_date",width = 110)
    self.tr_booking.column("pickup_time",width = 110)
    self.tr_booking.column("dropoff_time",width = 110)
    self.tr_booking.column("booking_status",width = 110)
    self.tr_booking.column("user_id",width = 80)
    self.tr_booking.column("driver_id",width = 80)
    
    self.tr_booking.pack(fill=BOTH, expand=1)
    self.tr_booking.bind("<ButtonRelease-1>",self.tree_focus)
    self.display_bookings()

# -----------------functions-----------------------------------------
  # connect_database function
  def connection(self):
    conn = mysql.connector.connect(host = 'localhost', user ='root',password ='Phurwa@807',database = 'pcps_python')
    return conn

  # treeview click data function
  def tree_focus(self,event):
    data_view = self.tr_booking.focus()
    click_tree = self.tr_booking.item(data_view)
    row = click_tree['values']
    try:
      self.var_user_id.set(row[8]),    
      self.var_booking_id.set(row[0]),
    except:
      pass

# -----------------------------------------------------------------

  # display in treeview
  def display_bookings(self):
    try:
      conn = self.connection()
      my_cursor = conn.cursor()

      #query to display bookings in treeview
      my_cursor.execute("select * from booking where booking_status = 'Pending'")
      book_data= my_cursor.fetchall()
      if len(book_data) != 0:
        self.tr_booking.delete(*self.tr_booking.get_children())
        for row in book_data:
          self.tr_booking.insert("", END,values = row)

      conn.commit()
      conn.close()

    except Exception as e:
        messagebox.showerror("Error",f"Due to {str(e)}",parent=self.trip)

# method to show driver id in combobox
  def show_driver_id(self):

    #exception handeling
    try:
      conn = self.connection()
      my_cursor = conn.cursor()  
      my_cursor.execute("select driver_id from driver where driver_status = 'Available' and request_status ='Approved' ")
      d_full=my_cursor.fetchall()
      if len(d_full)>0:
        del self.drive_list[:]
        self.drive_list.append("Select")
        for i in d_full:
          self.drive_list.append(i[0])    #add driver_id inside the list
    except Exception as e:
        messagebox.showerror("Error",f"Due to {str(e)}",parent=self.trip)

  # method to assign driver to the bookings
  def assign(self):
    #validation 
    if self.var_user_id.get()=="" or self.var_driver_id.get()=='' or self.var_driver_id.get()=='Select':
      messagebox.showerror("Error","not suffcient details",parent=self.trip)
    else:
      try:
        conn = self.connection()
        my_cursor = conn.cursor(buffered=True)

        #query to confirm trip
        my_cursor.execute("update booking set booking_status = %s,driver_id = %s where customer_id = %s and booking_id =%s",(
            'Confirmed',
            self.var_driver_id.get(),
            self.var_user_id.get(),
            self.var_booking_id.get()
                                                                                                  ))
        # query to update driver 
        my_cursor.execute("update driver set driver_status =  %s where driver_id = %s",(
            'Assigned',
            self.var_driver_id.get(),
          ))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success','Driver Assigned and Booking Confirmed Successfully',parent=self.trip)

        self.show_driver_id()   #display available driver id
        self.cmb_driver_list.configure(values=self.drive_list)    #update the combobox 
        self.view_table()
        self.var_driver_id.set('Select')
        

      except Exception as e:
        messagebox.showerror("Error",f"Due to {str(e)}",parent=self.trip)
      


# main function and creating object
if __name__ == '__main__':
  trip = Tk()                 
  tt = Assign_driver(trip)    
  trip.mainloop()             