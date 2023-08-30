from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
class Driver: 
  # initialize window
  def __init__(self,dd,email):
    self.dd = dd
    self.dd.title("Driver Dashboard")
    self.dd.geometry("1400x700+0+0")
    self.dd.state('zoomed')
    self.dd.config(bg='white')

    # textvairable and email parameter
    self.var_driver_id= StringVar()
    self.email=email
    self.view_table()

    # initialize frame for background image
    frame_0 = Frame(self.dd,bg='grey')
    frame_0.place(x=0 , y=0, width = 620, height=650)

    # image for bg
    my_bg = Image.open(r'C:\Users\asus\Desktop\book_taxi\image\d1.jpg').resize((620,650))
    self.bg = ImageTk.PhotoImage(my_bg)
    lbl_bg = Label(frame_0, image= self.bg)
    lbl_bg.place(x=0,y=0)

    # initialize frame1 
    frame_1 = Frame(self.dd,bg='light blue')
    frame_1.place(x=620, y=0, width = 645, height=100)

    # buttons
    btn_view = Button(frame_1,text='View',font=('Arial',13,'bold'),fg='white',bg='#F86F3C',border=0,padx=15,pady=2,activebackground='#F86F3C',activeforeground='white',cursor='hand2',command=self.view_upcoming_trip)
    btn_view.place(x=260,y=55)

    btn_completed = Button(frame_1,text='Completed',font=('Arial',13,'bold'),fg='white',bg='#F86F3C',border=1,padx=30,pady=2,activebackground='#F86F3C',activeforeground='white',cursor='hand2',command= self.complete_trip)
    btn_completed.place(x=470,y=20)

  # image for logout button
    log_img = Image.open(r'C:\Users\asus\Desktop\book_taxi\image\logout.png').resize((60,60))
    self.l_img = ImageTk.PhotoImage(log_img)

    # logout button
    btn_logout = Button(self.dd,image=self.l_img,border=0,cursor= 'hand2',bg='white',activebackground='white',command= self.logout)
    btn_logout.place(x=605,y=535)

    lbl_logout = Label(self.dd,text= 'Logout',font=('Arial',11,'bold'),fg='red',bg='white')
    lbl_logout.place(x=605,y=600)

  def view_table(self):
    frame_2 = Frame(self.dd,bg='red')
    frame_2.place(x=620 , y=101, width = 645, height=400)

   # scrollbar and treeview
    scroll_win = Scrollbar(frame_2,orient= VERTICAL)

    self.tr_booking = ttk.Treeview(frame_2,height=13,columns=("booking_id","pickup_address","dropoff_address","pickup_date","dropoff_date","pickup_time","dropoff_time","booking_status","user_id","driver_id"),xscrollcommand = scroll_win.set)
    scroll_win.pack(side=RIGHT, fill=Y)

    self.tr_booking.heading("booking_id",text= "ID")
    self.tr_booking.heading("pickup_address",text= "Pickup Address")
    self.tr_booking.heading("dropoff_address",text= "Dropoff Address")
    self.tr_booking.heading("pickup_date",text= "Pickup Date")
    self.tr_booking.heading("dropoff_date",text= "Dropoff Date")
    self.tr_booking.heading("pickup_time",text= "Pickup Time")
    self.tr_booking.heading("dropoff_time",text= "Dropoff Time")
    self.tr_booking.heading("booking_status",text= "Booking Status")
    self.tr_booking.heading("user_id",text= "CustomerID")
    self.tr_booking.heading("driver_id",text= "Driver ID")
    self.tr_booking['show'] = 'headings'

    self.tr_booking.column("booking_id",width = 30)
    self.tr_booking.column("pickup_address",width = 110)
    self.tr_booking.column("dropoff_address",width = 110)
    self.tr_booking.column("pickup_date",width = 110)
    self.tr_booking.column("dropoff_date",width = 110)
    self.tr_booking.column("pickup_time",width = 110)
    self.tr_booking.column("dropoff_time",width = 110)
    self.tr_booking.column("booking_status",width = 110)
    self.tr_booking.column("user_id",width = 100)
    self.tr_booking.column("driver_id",width = 100)
    
    self.tr_booking.pack(fill=BOTH, expand=1)

    # key binding
    self.tr_booking.bind("<ButtonRelease-1>",self.tree_click)   

# functions
  # method to logout
  def logout(self):
    ilogout= messagebox.askyesno("Confirmation","Are you sure? You want to logout!",parent=self.dd)
    if ilogout > 0:
      self.dd.destroy()   #destroy the window

  # method to connect database
  def connection(self):
    conn = mysql.connector.connect(host = 'localhost', user ='root',password ='Phurwa@807',database = 'pcps_python')
    return conn

  # treeview click data function
  def tree_click(self,event):
    data_view = self.tr_booking.focus()
    click_tree = self.tr_booking.item(data_view)
    row = click_tree['values']
    try:
      self.var_driver_id.set(row[9])
    except:
      pass

  # method to display booking data
  def view_upcoming_trip(self):
    try:
      conn = self.connection()
      my_cursor = conn.cursor(buffered=True)    #initialize cursor

      # query to fetch driver_id from email
      driver_id = my_cursor.execute("select driver_id from driver where email = '%s'" %(self.email))
      my_cursor.execute(driver_id)
      d_id = my_cursor.fetchone()[0]

      # query to fetch booking data
      my_cursor.execute("select booking_id,pickup_address,dropoff_address,pickup_date,dropoff_date,pickup_time,dropoff_time,booking_status,customer_id,driver_id from booking where booking_status='Confirmed' and driver_id = %s",(
                d_id,
      ))
      book_d= my_cursor.fetchall()
      if len(book_d) != 0:
        self.tr_booking.delete(*self.tr_booking.get_children())
        for row in book_d:
          self.tr_booking.insert("", END,values = row)

    except Exception as e:
        messagebox.showerror("Error",f"Due to {str(e)}",parent=self.dd)

  # method to complete trip
  def complete_trip(self):
    # validation
    if self.var_driver_id.get()=="":
      messagebox.showerror("Error","not suffcient details",parent=self.dd)
    else:
      try:
        conn = self.connection()    
        my_cursor = conn.cursor(buffered=True)    #initialize cursor

        # query to update driver_status of driver
        my_cursor.execute("update driver set driver_status=%s where driver_id = %s",(
            'Available',
            self.var_driver_id.get(),
                                                                                      ))
        my_cursor.execute("delete from booking where driver_id = %s",(
          self.var_driver_id.get(),
        ))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success','Trip Completed',parent=self.dd)

        self.view_table()   #display the booking data
        self.var_driver_id.set('')

      except Exception as e:
        messagebox.showerror("Error",f"Due to {str(e)}",parent=self.dd)

# main function and creating object
if __name__ == '__main__':
  dd = Tk()
  d_dash = Driver(dd)
  dd.mainloop()