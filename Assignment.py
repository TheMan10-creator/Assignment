from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


try:
    con = mysql.connector.connect(host='localhost', user='root', password="9866950525a", database='assign')
    cur = con.cursor()
except mysql.connector.Error as e:
    print(e)

class Student_info:
    def add_info(self):
        fname = self.firsten.get()
        lname = self.len.get()
        Address = self.Adden.get()
        Age = int(self.ageen.get())
        contact = self.contact.get()
        degree = self.degree.get()
        query = 'insert into new_table values(%s,%s,%s,%s, %s, %s)'
        values = (fname, lname, Address, Age, contact, degree)
        cur.execute(query,values)
        print('1 row inserted')
        con.commit()
        self.show()
        self.clear()

    def show(self):
        query='select * from new_table'
        cur.execute(query)
        rows=cur.fetchall()

        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())

        for row in rows:
            self.student_table.insert('',END,values=row)


    def clear(self):
        self.firsten.delete(0,END)
        self.len.delete(0,END)
        self.Adden.delete(0,END)
        self.ageen.delete(0,END)
        self.contact.delete(0,END)
        self.degree.delete(0,END)

    def update(self):

        d1 = self.firsten.get()
        d2 = self.len.get()
        d3 = self.Adden.get()
        d4 = self.ageen.get()
        contact = self.contact.get()
        degree = self.degree.get()

        query='update new_table set fname=%s, lname=%s, Address=%s, contact=%s, degree=%s where Age=%s'
        values=(d1, d2, d3, contact, degree, d4)
        cur.execute(query,values)
        con.commit()
        self.clear()
        self.show()


    def pointer(self,event):
        point=self.student_table.focus()
        content=self.student_table.item(point)
        row=content['values']
        self.clear()
        self.firsten.insert(0,row[0])
        self.len.insert(0, row[1])
        self.Adden.insert(0, row[2])
        self.ageen.insert(0, row[3])
        self.contact.insert(0, row[4])
        self.degree.insert(0, row[5])

    def delete(self):
        selected_item = self.student_table.selection()
        self.student_table.delete(selected_item)

        age=self.ageen.get()
        query = 'delete from new_table where Age=%s'
        values=(age,)
        cur.execute(query,values)
        con.commit()
        self.clear()

    def __init__(self, root):

        self.root = root

        #--------label---------
        self.firstnframe = Label(self.root, text='First Name')
        self.firstnframe.grid(row=0, column=0, padx=15, pady=15)

        self.lnamef = Label(self.root,text='Last Name')
        self.lnamef.grid(row=1, column=0, padx=15, pady=15)

        self.lblAdd = Label(self.root,text="Address")
        self.lblAdd.grid(row=2, column=0, padx=15, pady=15)

        self.lblage = Label(self.root,text='Age')
        self.lblage.grid(row=3, column=0, padx=15, pady=15)

        self.lbldegree = Label(self.root, text='Degree')
        self.lbldegree.grid(row=4, column=0, padx=15, pady=15)

        self.lblcontact = Label(self.root, text='Contact')
        self.lblcontact.grid(row=5, column=0, padx=15, pady=15)

        #---------Entry---------
        self.firsten = Entry(self.root)
        self.firsten.grid(row=0, column=1, padx=15, pady=15)

        self.len = Entry(self.root)
        self.len.grid(row=1, column=1, padx=15, pady=15)

        self.Adden = Entry(self.root)
        self.Adden.grid(row=2, column=1, padx=15, pady=15)

        self.ageen = Entry(self.root)
        self.ageen.grid(row=3, column=1, padx=15, pady=15)

        self.degree = Entry(self.root)
        self.degree.grid(row=4, column=1, padx=15, pady=15)

        self.contact = Entry(self.root)
        self.contact.grid(row=5, column=1, padx=15, pady=15)



        #------------frame---------
        self.btn_frame = Frame(self.root, bd=4, bg='black', relief=RIDGE)
        self.btn_frame.place(x=20, y=360, width=500, height=70)

        self.table_frame = Frame(self.root, bd=4, bg='black', relief=RIDGE)
        self.table_frame.place(x=20, y=500, width=700, height=350)

        #-------scrollbar--------
        self.scroll_x = Scrollbar(self.table_frame, orient=HORIZONTAL)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        #----------Table---------
        self.student_table=ttk.Treeview(self.table_frame, columns=('fname', 'lname', 'Address', 'Age', 'Contact',
                                                                   'Degree'),
                                        xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.student_table.heading('fname',text='Full Name')
        self.student_table.heading('lname', text='Last Name')
        self.student_table.heading('Address', text='Address')
        self.student_table.heading('Age', text='Age')
        self.student_table.heading('Contact', text='Contact')
        self.student_table.heading('Degree', text='Degree')

        self.student_table.pack(fill=BOTH,expand=True)

        self.student_table['show']='headings'

        self.student_table.column('fname',width=150)
        self.student_table.column('lname', width=150)
        self.student_table.column('Address', width=150)
        self.student_table.column('Age', width=150)
        self.student_table.column('Contact', width=150)
        self.student_table.column('Degree', width=150)
        self.show()

        self.student_table.bind('<ButtonRelease-1>',self.pointer)

        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)


        #-----------button--------
        self.addbtn=Button(self.btn_frame, text='Add',command=self.add_info, width=12,height=2)
        self.addbtn.grid(row=5, column=0,padx=5)

        self.upbtn=Button(self.btn_frame,text='Update',command=self.update,width=12,height=2)
        self.upbtn.grid(row=5,column=2,padx=5)
        self.deletebtn=Button(self.btn_frame,text='Delete',command=self.delete,width=12,height=2)
        self.deletebtn.grid(row=5,column=4,padx=5)
        self.clearbtn=Button(self.btn_frame,text='Clear',command=self.clear,width=12,height=2)
        self.clearbtn.grid(row=5,column=6,padx=5)


        self.detail_frame=Frame(self.root,bd=4,relief=RIDGE)
        self.detail_frame.place(x=290,y=30,width=500,height=200)

        self.lblsearch=Label(self.detail_frame,text='Search By',font=('arial',10))
        self.lblsearch.grid(row=0,column=0,pady=5)

        self.searchcombo=ttk.Combobox(self.detail_frame,font=('arial',10),state='readonly')
        self.searchcombo['values']=('fname','lname','Address','Age', 'Degree', 'Contact')
        self.searchcombo.set("fname")
        self.searchcombo.grid(row=0,column=1,pady=10,padx=20)

        self.sortcombo = ttk.Combobox(self.detail_frame, font=('arial', 10), state='readonly')
        self.sortcombo['values'] = ('fname', 'lname', 'Address', 'Age', 'Degree', 'Contact')
        self.sortcombo.set('fname')
        self.sortcombo.grid(row=2, column=1, pady=10, padx=20)

        self.searchlbl=Label(self.detail_frame,text= 'Search text',font=('arial',10))
        self.searchlbl.grid(row=1,column=0,pady=5)

        self.searchentry=Entry(self.detail_frame,width=20)
        self.searchentry.grid(row=1,column=1,pady=10,padx=10)

        self.searchbtn=Button(self.detail_frame,text='Search',command=self.search, font=('arial',10),width=8)
        self.searchbtn.grid(row=1,column=3,pady=10,padx=10)

        self.sortbtn = Button(self.detail_frame, text='Sort',command=self.sort, font=('arial', 10), width=8)
        self.sortbtn.grid(row=2, column=3, pady=10, padx=10)

    def bubbleSort(self, arr):
        n = len(arr)
        if self.sortcombo.get() == 'fname':
            column = 0
        elif self.sortcombo.get() == 'lname':
            column = 1
        elif self.sortcombo.get() == 'Address':
            column = 2
        elif self.sortcombo.get() == 'Age':
            column = 3
        elif self.sortcombo.get() == 'Degree':
            column = 4
        elif self.sortcombo.get() == 'Contact':
            column = 5
        else:
            return

        for i in range(n):

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j][column] > arr[j + 1][column]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

    def sort(self):
        query = 'select * from new_table'
        cur.execute(query)
        rows = cur.fetchall()

        self.bubbleSort(rows)

        self.student_table.delete(*self.student_table.get_children())

        for row in rows:
            self.student_table.insert('', END, values=row)

    def search(self, mylist=None):
        if not mylist:
            query = 'select * from new_table'
            cur.execute(query)
            rows = cur.fetchall()
        else:
            rows = mylist
        found = []
        target = self.searchentry.get()
        if self.searchcombo.get() == 'fname':
            column = 0
        elif self.searchcombo.get() == 'lname':
            column = 1
        elif self.searchcombo.get() == 'Address':
            column = 2
        elif self.searchcombo.get() == "Age":
            column = 3
        elif self.sortcombo.get() == 'Degree':
            column = 4
        elif self.sortcombo.get() == 'Contact':
            column = 5
        else:
            return
        for value in rows:
            if target == value[column]:
                found.append(value)

        self.student_table.delete(*self.student_table.get_children())

        for row in found:
            self.student_table.insert('', END, values=row)

        return found


if __name__ == '__main__':
    root = Tk()
    root.geometry('800x850+0+0')
    root.title('Student Form')
    root.configure(bg='green')
    gui = Student_info(root)
    root.mainloop()