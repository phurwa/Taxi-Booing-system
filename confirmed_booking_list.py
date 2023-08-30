from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
class Confimed_bookings:
  # initialize window
  def __init__(self,confirm):
    self.confirm = confirm
    self.confirm.title("Confirmed Bookings")
    self.confirm.geometry("500x350+410+120")
    
    # initialize frame1
    frame_1 = Frame(self.confirm,bg='#D5F0DD')
    frame_1.place(x=0 , y=0, width = 500, height=50)
    self.booking_table()


# scrollbar and treeview
  def booking_table(self):
    frame_2 = Frame(self.confirm,bg='red')
    frame_2.place(x=0 , y=50, width = 500, height=290)

    scroll_win = Scrollbar(frame_2,orient= VERTICAL)

    self.tr_booking_list = ttk.Treeview(frame_2,height=10,columns=("booking_id","pickup_place","dropoff_place","Customer_id","Driver_id",),xscrollcommand = scroll_win.set)
    scroll_win.pack(side=RIGHT, fill=Y)

    self.tr_booking_list.heading("booking_id",text= "Id")
    self.tr_booking_list.heading("pickup_place",text= "Pickup Place")
    self.tr_booking_list.heading("dropoff_place",text= "Dropoff Place")
    self.tr_booking_list.heading("Customer_id",text= "Customer Id")
    self.tr_booking_list.heading("Driver_id",text= "Driver Id")
    self.tr_booking_list['show'] = 'headings'

    self.tr_booking_list.column("booking_id",width = 40)
    self.tr_booking_list.column("pickup_place",width = 110)
    self.tr_booking_list.column("dropoff_place",width = 110)
    self.tr_booking_list.column("Customer_id",width = 100)
    self.tr_booking_list.column("Driver_id",width = 100)
    
    
    self.tr_booking_list.pack(fill=BOTH, expand=1)
    self.show_confrim_booking()     #display booking data

# functions
  #method to connect to database
  def connection(self):
    conn = mysql.connector.connect(host = 'localhost', user ='root',password ='Phurwa@807',database = 'pcps_python')
    return conn
  
  # method to display all confirmed bookings
  def show_confrim_booking(self):
    try:
      conn = self.connection()
      my_cursor = conn.cursor()     #initialize cursor

      # query to fetch booking data 
      my_cursor.execute("select booking_id,pickup_address,dropoff_address,customer_id,driver_id from booking where booking_status = 'Confirmed'")
      book_d= my_cursor.fetchall()
      if len(book_d) != 0:
        self.tr_booking_list.delete(*self.tr_booking_list.get_children())
        for row in book_d:
          self.tr_booking_list.insert("", END,values = row)

    except Exception as e:
        messagebox.showerror("Error",f"Due to {str(e)}",parent=self.confirm)

# main function and creating object
if __name__ == '__main__':
  confirm = Tk()
  c_book = Confimed_bookings(confirm)
  confirm.mainloop()