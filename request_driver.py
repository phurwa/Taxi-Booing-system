from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Request_list:
  # initialize window
  def __init__(self,request):
    self.request = request
    self.request.title("Driver Information")
    self.request.geometry("568x500+440+80")

    # textvariables
    self.var_driver_id= StringVar()
    self.search_d_id = StringVar()
    self.view_table()

    # initialize frame1
    frame_1 = Frame(self.request,bg='#D5F0DD')
    frame_1.place(x=0 , y=0, width = 568, height=90)

    # labels, entryfields
    lbl_driver_id = Label(frame_1,text='Driver Id:',font=('Arial',12,),fg='black',bg='#D5F0DD')
    lbl_driver_id.place(x=380,y=7)

    lbl_search= Label(frame_1,text="Search Driver",font=('Arial',11,'bold'),fg='black',bg='#D5F0DD')
    lbl_search.place(x=5,y=15)

    self.entry_search = Entry(frame_1,textvariable=self.search_d_id, width=8,font=('Arial',12,'bold'),border=1,bg="light blue")
    self.entry_search.place(x=122,y=15)

    self.entry_driver_id = Entry(frame_1, textvariable=self.var_driver_id, width=9,font=('Arial',12,'bold'),border=1,bg="light blue",state='disabled')
    self.entry_driver_id.place(x=460,y=7)

    # image for reload button
    reload_img = Image.open(r'image\reload.png').resize((30,30))
    self.img_re = ImageTk.PhotoImage(reload_img)

    # buttons
    btn_reqload = Button(frame_1,image=self.img_re,border=0,cursor= 'hand2',bg='#D5F0DD',activebackground='#D5F0DD',command= self.show_request)
    btn_reqload.place(x=255,y=45)

    btn_approve = Button(frame_1,text='Approve',font=('Arial',13,'bold'),fg='white',bg='#F86F3C',border=1,padx=30,pady=2,activebackground='#F86F3C',activeforeground='white',cursor='hand2',command=self.confirm_driver)
    btn_approve.place(x=397,y=45)

    btn_search = Button(frame_1,text='Search',font=('Arial',13,'bold'),fg='white',bg='#F86F3C',border=1,padx=10,pady=0,activebackground='#F86F3C',activeforeground='white',cursor='hand2',command=self.view_searched_drivers)
    btn_search.place(x=50,y=50)

  # method to display treeview and scrollbar
  def view_table(self):
    # frame for treeview and scrollbar
    frame_2 = Frame(self.request,bg='red')
    frame_2.place(x=0 , y=90, width = 568, height=420)

    # scrollbar and treeview
    scroll_win = Scrollbar(frame_2,orient= VERTICAL)

    self.tr_request_list = ttk.Treeview(frame_2,height=13,columns=("driver_id","FullName","Email","Address","Contact","Lisence","request_status"),xscrollcommand = scroll_win.set)
    scroll_win.pack(side=RIGHT, fill=Y)

    self.tr_request_list.heading("driver_id",text= "ID")
    self.tr_request_list.heading("FullName",text= "FullName")
    self.tr_request_list.heading("Email",text= "Email")
    self.tr_request_list.heading("Address",text= "Address")
    self.tr_request_list.heading("Contact",text= "Contact")
    self.tr_request_list.heading("Lisence",text= "Lisence")
    self.tr_request_list.heading("request_status",text= "request_status")
    self.tr_request_list['show'] = 'headings'

    self.tr_request_list.column("driver_id",width = 40)
    self.tr_request_list.column("FullName",width = 100)
    self.tr_request_list.column("Email",width = 110)
    self.tr_request_list.column("Address",width = 100)
    self.tr_request_list.column("Contact",width = 100)
    self.tr_request_list.column("Lisence",width = 100)
    self.tr_request_list.column("request_status",width = 100)
    
    self.tr_request_list.pack(fill=BOTH, expand=1)
    # key binding 
    self.tr_request_list.bind("<ButtonRelease-1>",self.tree_click)    

    self.show_request()   #display 


  # method to connect database
  def connection(self):
    conn = mysql.connector.connect(host = 'localhost', user ='root',password ='Phurwa@807',database = 'pcps_python')
    return conn

  # treeview click data function
  def tree_click(self,event):
    data_view = self.tr_request_list.focus()
    click_tree = self.tr_request_list.item(data_view)
    row = click_tree['values']
    self.var_driver_id.set(row[0])

  # method to display driver in tree view
  def show_request(self):
    try:
      conn = self.connection()
      my_cursor = conn.cursor()     #initialize cursor

      # query to fetch driver data with request_status not approved
      my_cursor.execute("select driver_id,full_name,email,address,contact,license_no,request_status from driver where request_status = 'Not Approved'")
      vac_driv= my_cursor.fetchall()
      if len(vac_driv) != 0:
        self.tr_request_list.delete(*self.tr_request_list.get_children())
        for row in vac_driv:
          self.tr_request_list.insert("", END,values = row)

    except Exception as e:
        messagebox.showerror("Error",f"Due to {str(e)}",parent=self.request)

  # method to diplay searched drivers
  def view_searched_drivers(self):
    if self.search_d_id.get()=='':
      # validation
      messagebox.showerror('Error','Search By Driver ID',parent=self.request)
    else:
      try:
        conn = self.connection()
        my_cursor = conn.cursor()       #initialize cursor

        # query to fetch driver data 
        my_cursor.execute("select driver_id,full_name,email,address,contact,license_no,driver_status from driver where request_status='Not Approved' and driver_id = %s",(self.search_d_id.get(),))
        search_driv= my_cursor.fetchall()
        if len(search_driv) != 0:
          self.tr_request_list.delete(*self.tr_request_list.get_children())
          for row in search_driv:
            self.tr_request_list.insert("", END,values = row)
        else:
          messagebox.showinfo('Message','Driver Not Found',parent=self.request)
        self.search_d_id.set('')    #clear fields
      except Exception as e:
          messagebox.showerror("Error",f"Due to {str(e)}",parent=self.request)

  # method to approve driver
  def confirm_driver(self):
    if self.var_driver_id.get()=="":
      # validation
      messagebox.showerror("Error","not suffcient details",parent=self.request)
    else:
      try:
        conn = self.connection()
        my_cursor = conn.cursor(buffered=True)      #initialize cursor

        # query to update request status of driver
        my_cursor.execute("update driver set request_status = %s where driver_id = %s",(
            'Approved',
            self.var_driver_id.get(),
                                                                                                  ))
        conn.commit()
        conn.close()      #close connection
        messagebox.showinfo('Success','Driver Approved Successfully ',parent=self.request)
        self.var_driver_id.set('')      #clear field

      except Exception as e:
        messagebox.showerror("Error",f"Due to {str(e)}",parent=self.request)

# main method and creating object
if __name__ == '__main__':
  request = Tk()
  list_d = Request_list(request)
  list_d.show_request()   #call method using object
  request.mainloop()
