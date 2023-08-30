from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from datetime import datetime
from confirm_trip import Assign_driver
from view_driver import Driver_info
from view_customer import Customer_info
from confirmed_booking_list import Confimed_bookings
class Admin_dashboard:
  # initialize window
  def __init__(self,adm):
    self.adm= adm
    self.adm.title("Admin Dashboard")
    self.adm.geometry("1400x700+0+0")
    self.adm.state('zoomed')

    # initialize frame1
    frame_1 = Frame(self.adm,bg='light blue')
    frame_1.place(x=0 , y=0, width = 225, height=700)

    #image for admin
    ad_img = Image.open(r'image\gg.png').resize((100,100))
    self.lg_img = ImageTk.PhotoImage(ad_img)

    lbl_lg_img = Label(frame_1, image= self.lg_img,bg='light blue')
    lbl_lg_img.place(x=50,y=40)

    lbl_logout = Label(frame_1,text= 'Logout',font=('Arial',11,'bold'),fg='red',bg='light blue')
    lbl_logout.place(x=82,y=605)

  # image for logout button
    log_img = Image.open(r'image\logout.png').resize((60,60))
    self.l_img = ImageTk.PhotoImage(log_img)
   
    # buttons
    btn_logout = Button(frame_1,image=self.l_img,border=0,cursor= 'hand2',bg='light blue',activebackground='light blue',command= self.logout)
    btn_logout.place(x=78,y=545)

    btn_bookings = Button(frame_1,text='Manage Trip',font=('Arial',13,'bold'),fg='black',bg='orange',border=1,height=1,width=16,activebackground='orange',activeforeground='black',cursor= 'hand2',command=self.manage_trip_window)
    btn_bookings.place(x=25,y=200)

    btn_customers = Button(frame_1,text='Customer Info',font=('Arial',13,'bold'),fg='black',bg='orange',border=1,height=1,width=16,activebackground='orange',activeforeground='black',cursor= 'hand2',command=self.customer_info_window)
    btn_customers.place(x=25,y=250)

    btn_drivers = Button(frame_1,text='Driver Info',font=('Arial',13,'bold'),fg='black',bg='orange',border=1,height=1,width=16,activebackground='orange',activeforeground='black',cursor= 'hand2',command=self.driver_info_window)
    btn_drivers.place(x=25,y=300)

    btn_confirmed_trip = Button(frame_1,text='Confirmed Trip',font=('Arial',13,'bold'),fg='black',bg='orange',border=1,height=1,width=16,activebackground='orange',activeforeground='black',cursor= 'hand2',command=self.confired_booking_window)
    btn_confirmed_trip.place(x=25,y=350)

  # initialize frame_2 for background image
    frame_2 = Frame(self.adm,bg='black')
    frame_2.place(x=225 , y=0, width = 1200, height=700)

    my_bg = Image.open(r'image\ad.jpg').resize((1100,700))
    self.bg = ImageTk.PhotoImage(my_bg)
    lbl_bg = Label(frame_2, image= self.bg)
    lbl_bg.place(x=0,y=0)

    # Create a TimeLabel object
    self.time_label = Label(frame_2, text="",font=("Arial",11,'bold'),bg='white',fg='black',width=34,height=1)
    self.time_label.place(x=350,y=5)

    self.update_time()

  # method to logout
  def logout(self):
    ilogout= messagebox.askyesno("Confirmation","Are you sure? You want to logout!",parent=self.adm)
    if ilogout > 0:
      self.adm.destroy()

  # method to open confirm trip window
  def manage_trip_window(self):
    self.manage_win = Toplevel(self.adm)
    self.m_trip= Assign_driver(self.manage_win)

  # method to open view driver window
  def driver_info_window(self):
    self.d_window = Toplevel(self.adm)
    self.driv_wind= Driver_info(self.d_window)

  # method to open view customer window
  def customer_info_window(self):
    self.c_window = Toplevel(self.adm)
    self.cus_detail= Customer_info(self.c_window)

  # method to open confirmed booking window
  def confired_booking_window(self):
    self.confirmed_b = Toplevel(self.adm)
    self.b_confirm= Confimed_bookings(self.confirmed_b)

  # date time method 
  def update_time(self):
    self.time_label.config(text=datetime.now().strftime("""Date: %B %d,%Y      Time: %I:%M:%S %p"""))
    self.time_label.after(1000, self.update_time)

  
# main function and creating object
if __name__ == '__main__':
  adm = Tk()
  main_admin = Admin_dashboard(adm)
  adm.mainloop()