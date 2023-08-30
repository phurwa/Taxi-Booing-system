from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
class Customer_info():
  # initialize window
  def __init__(self,cus):
    self.cus = cus
    self.cus.title("Customer Information")
    self.cus.geometry("590x350+410+120")

    # text_variable 
    self.var_id= StringVar()
    self.cus_table()

    # initialize frame1
    frame_1 = Frame(self.cus,bg='#D5F0DD')
    frame_1.place(x=0 , y=0, width = 590, height=60)

    # labels,entryfields and button
    lbl_search= Label(frame_1,text="Search Driver",font=('Arial',11,'bold'),fg='black',bg='#D5F0DD')
    lbl_search.place(x=20,y=15)

    self.entry_search = Entry(frame_1,textvariable=self.var_id, width=10,font=('Arial',12,'bold'),border=1,bg="light blue")
    self.entry_search.place(x=144,y=15)

    # button
    btn_search = Button(frame_1,text='Search',font=('Arial',13,'bold'),fg='white',bg='#5B83F6',border=1,padx=13,pady=1,activebackground='#5B83F6',activeforeground='white',cursor='hand2',command=self.view_searched_customer)
    btn_search.place(x=390,y=10)


# method to show scrollbar and treeview
  def cus_table(self):
    frame_2 = Frame(self.cus,bg='red')
    frame_2.place(x=0 , y=60, width = 590, height=290)

    scroll_win = Scrollbar(frame_2,orient= VERTICAL)    #initialize scrollbar

    self.tr_cuslist = ttk.Treeview(frame_2,height=10,columns=("Customer_id","FullName","Email","Address","Contact","payment_method"),xscrollcommand = scroll_win.set)
    scroll_win.pack(side=RIGHT, fill=Y)

    self.tr_cuslist.heading("Customer_id",text= "Id")
    self.tr_cuslist.heading("FullName",text= "FullName")
    self.tr_cuslist.heading("Email",text= "Email")
    self.tr_cuslist.heading("Address",text= "Address")
    self.tr_cuslist.heading("Contact",text= "Contact")
    self.tr_cuslist.heading("payment_method",text= "Payment Method")
    self.tr_cuslist['show'] = 'headings'

    self.tr_cuslist.column("Customer_id",width = 40)
    self.tr_cuslist.column("FullName",width = 100)
    self.tr_cuslist.column("Email",width = 110)
    self.tr_cuslist.column("Address",width = 100)
    self.tr_cuslist.column("Contact",width = 100)
    self.tr_cuslist.column("payment_method",width = 110)
    
    self.tr_cuslist.pack(fill=BOTH, expand=1)
    self.show_customer()        #display customer in tree view

# -----------------functions-----------------------------------------
  # method to connect database
  def connection(self):
    conn = mysql.connector.connect(host = 'localhost', user ='root',password ='Phurwa@807',database = 'pcps_python')
    return conn

  # method to display searched customer
  def view_searched_customer(self):

    # validation
    if self.var_id.get()=='':
      messagebox.showerror('Error','Search By Customer ID',parent=self.cus)
    else:
      try:
        conn = self.connection()
        my_cursor = conn.cursor()   #initialize cursor

        # qeury to fetch data of  searched customer
        my_cursor.execute("select customer_id,full_name,email,address,contact,payment_method from customer where customer_id = %s",(self.var_id.get(),))
        search_cus= my_cursor.fetchall()
        if len(search_cus) != 0:
          self.tr_cuslist.delete(*self.tr_cuslist.get_children())
          for row in search_cus:
            self.tr_cuslist.insert("", END,values = row)
        else:
          messagebox.showinfo('Message','Customer Not Found',parent=self.cus)
        self.var_id.set('')     #clear the field
      except Exception as e:
          messagebox.showerror("Error",f"Due to {str(e)}",parent=self.cus)

  # method to show all customers
  def show_customer(self):
    try:
      conn = self.connection()
      my_cursor = conn.cursor()   #initialize cursor

      # query to fetch data from customer
      my_cursor.execute("select customer_id,full_name,email,address,contact,payment_method from customer")
      cus_detail= my_cursor.fetchall()
      if len(cus_detail) != 0:
        self.tr_cuslist.delete(*self.tr_cuslist.get_children())
        for row in cus_detail:
          self.tr_cuslist.insert("", END,values = row)

    except Exception as e:
        messagebox.showerror("Error",f"Due to {str(e)}",parent=self.cus)

# main function and creating object
if __name__ == '__main__':
  cus = Tk()
  cus_d = Customer_info(cus)
  cus.mainloop()