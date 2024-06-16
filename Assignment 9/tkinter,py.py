import pymysql
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox

r = Tk()
r.geometry("600x400")
r.title("Student Management System")
r.configure(bg="lightblue")

lid = Label(r, text="Student ID")
lid.place(x=20, y=20)
lname = Label(r, text="Name")
lname.place(x=20, y=60)
lem = Label(r, text="Email")
lem.place(x=20, y=100)
lmno = Label(r, text="Mobile No")
lmno.place(x=20, y=140)
lcity = Label(r, text="City")
lcity.place(x=20, y=180)

eid = Entry()
eid.place(x=120, y=20)
ename = Entry()
ename.place(x=120, y=60)
eem = Entry()
eem.place(x=120, y=100)
emno = Entry()
emno.place(x=120, y=140)
ecity = Entry()
ecity.place(x=120, y=180)

tree = ttk.Treeview(r, columns=('Student ID', 'Name', 'Email', 'Mobile No', 'City'), show='headings')
tree.heading('Student ID', text='Student ID')
tree.heading('Name', text='Name')
tree.heading('Email', text='Email')
tree.heading('Mobile No', text='Mobile No')
tree.heading('City', text='City')
tree.place(x=250, y=20, height=250)

def createconn():
    return pymysql.connect(host="localhost", database="first", user="root", password="1209", port=3306)

def insertdata():
    sid = eid.get()
    name = ename.get()
    email = eem.get()
    city = ecity.get()
    mno = emno.get()
    if sid == "" or name == "" or email == "" or city == "" or mno == "":
        messagebox.showwarning("Insert Status", "All Fields are mandatory")
    else:
        conn = createconn()
        cursor = conn.cursor()
        args = (sid, name, email, city, mno)
        query = "insert into student(sid,name,email,city,contact) values(%s,%s,%s,%s,%s)"
        cursor.execute(query, args)
        conn.commit()
        messagebox.showinfo("Insert Status", "Data Inserted Successfully")
        conn.close()
        displaydata()

def updatedata():
    sid = eid.get()
    name = ename.get()
    email = eem.get()
    city = ecity.get()
    mno = emno.get()
    if sid == "" or name == "" or email == "" or city == "" or mno == "":
        messagebox.showwarning("Update Status", "All Fields are mandatory")
    else:
        conn = createconn()
        cursor = conn.cursor()
        args = (name, email, city, mno, sid)
        query = "update student set name=%s, email=%s, city=%s, contact=%s where sid=%s"
        cursor.execute(query, args)
        conn.commit()
        messagebox.showinfo("Update Status", "Data Updated Successfully")
        conn.close()
        displaydata()

def searchdata():
    sid = eid.get()
    if sid == "":
        messagebox.showwarning("Search Status", "Student ID is mandatory.")
    else:
        conn = createconn()
        cursor = conn.cursor()
        args = (sid,)
        query = "select * from student where sid=%s"
        cursor.execute(query, args)
        result = cursor.fetchall()
        if result:
            for row in tree.get_children():
                tree.delete(row)
            for i in result:
                tree.insert('', 'end', values=i)
        else:
            messagebox.showinfo("Search Status", "No records found")
        conn.close()

def deletedata():
    sid = eid.get()
    if sid == "":
        messagebox.showwarning("Delete Status", "Student ID is Mandatory")
    else:
        conn = createconn()
        cursor = conn.cursor()
        args = (sid,)
        query = "delete from student where sid=%s"
        cursor.execute(query, args)
        conn.commit()
        messagebox.showinfo("Delete Status", "Data Deleted Successfully")
        conn.close()
        displaydata()

def displaydata():
    conn = createconn()
    cursor = conn.cursor()
    query = "select * from student"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in tree.get_children():
        tree.delete(row)
    for i in result:
        tree.insert('', 'end', values=i)
    conn.close()

bins = Button(r, text=" Insert ", bg="grey", command=insertdata)
bins.place(x=20, y=220)
bupd = Button(r, text=" Update ", bg="grey", command=updatedata)
bupd.place(x=100, y=220)
bdel = Button(r, text=" Delete ", bg="grey", command=deletedata)
bdel.place(x=190, y=220)
bsearch = Button(r, text="Search", bg="grey", command=searchdata)
bsearch.place(x=280, y=220)

displaydata()

mainloop()
