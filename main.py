from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Db import Database

db=Database("Employee.db")
root=Tk()
root.title("Employee Management System")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

#Global Variable declaration:
name=StringVar()
age=StringVar()
doj=StringVar()
gender=StringVar()
email=StringVar()
contact=StringVar()
address=StringVar()

#Entries Frame:
entries_frame= Frame(root,bg="#535c68")
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame, text="Employee Management System", font=("Calibri",18,"bold"), bg= "#535c68",fg="white")
title.grid(row=0,columnspan= 2, padx=10,pady=20 )

# Name --> Label:
lblName=Label(entries_frame,text="Name", font=("Calibri",16),bg= "#535c68",fg="white")
lblName.grid (row=1,column=0, padx=10,pady=10,sticky="w")

#Name --> Text Box:
txtName=Entry(entries_frame, textvariable=name,font=("Calibri",16),width=30)
txtName.grid(row=1,column=1)

# Age --> Label:
lblAge=Label(entries_frame,text="Age", font=("Calibri",16),bg= "#535c68",fg="white")
lblAge.grid (row=1,column=2, padx=10,pady=10,sticky="w")

#Age --> Text Box:
txtAge=Entry(entries_frame, textvariable=age,font=("Calibri",16),width=30)
txtAge.grid(row=1,column=3)

#DOJ --> Label:
lbldoj=Label(entries_frame,text="D.O.J",font=("Calibri",16),bg= "#535c68",fg="white")
lbldoj.grid(row=2,column=0,padx=10,pady=10,sticky="w")

#DOJ --> Text Box:
txtdoj=Entry(entries_frame, textvariable=doj,font=("Calibri",16),width=30)
txtdoj.grid(row=2,column=1)

#E-Mail --> Label
lblmail=Label(entries_frame,text="E-Mail",font=("Calibri",16),bg= "#535c68",fg="white")
lblmail.grid(row=2,column=2,padx=10,pady=10,sticky="w")

#Email --> Text Box:
txtmail=Entry(entries_frame, textvariable=email,font=("Calibri",16),width=30)
txtmail.grid(row=2,column=3)

#Gender --> Label
lblgender=Label(entries_frame,text="Gender",font=("Calibri",16),bg= "#535c68",fg="white")
lblgender.grid(row=3,column=0,padx=10,pady=10,sticky="w")

#Gender -->Combo Box:
comboGender=ttk.Combobox(entries_frame, font=("Calibri",16),width=28,textvariable=gender,state="readonly")
comboGender['values']=("Male","Female")
comboGender.grid(row=3,column=1,padx=10,sticky="w")

#Contact --> Label
lblcontact=Label(entries_frame,text="Contact",font=("Calibri",16),bg= "#535c68",fg="white")
lblcontact.grid(row=3,column=2,padx=10,pady=10,sticky="w")

#Contact--> Text Box:
txtcontact=Entry(entries_frame, textvariable=contact,font=("Calibri",16),width=30)
txtcontact.grid(row=3,column=3)

#Address --> Label
lblAddress=Label(entries_frame,text="Address",font=("Calibri",16),bg= "#535c68",fg="white")
lblAddress.grid(row=4,column=0,padx=10,pady=10,sticky="w")

#Address --> Text Box -->full width
txtAddress=Text(entries_frame, width=85,height=5,font=("Calibri",16))
txtAddress.grid(row=5,column=0,columnspan=4,padx=10,sticky="w")

def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0,END)
    txtAddress.insert(END, row[7])




def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)

#creating Function:
def add_employee():
    if txtName.get()=="" or txtAge.get()=="" or txtdoj.get()=="" or txtmail.get()=="" or comboGender.get()=="" \
            or txtcontact.get()=="" or txtAddress.get(1.0, END) == "":
        messagebox.showerror("Error in Input", "Please fill all the details")
        return
    db.insert(txtName.get(),txtAge.get(),txtdoj.get(),txtmail.get(),comboGender.get(),txtcontact.get(),txtAddress.get(1.0, END))
    messagebox.showinfo("Success","Record Inserted")
    clearAll()
    displayAll()


def update_employee():
    if txtName.get()=="" or txtAge.get()=="" or txtdoj.get()=="" or txtmail.get()=="" or comboGender.get()=="" \
            or txtcontact.get()=="" or txtAddress.get(1.0, END) == "":
        messagebox.showerror("Error in Input", "Please fill all the details")
        return
    db.update(row[0],txtName.get(),txtAge.get(),txtdoj.get(),txtmail.get(),comboGender.get(),txtcontact.get(),txtAddress.get(1.0, END))
    messagebox.showinfo("Success","Record Updated")
    clearAll()
    displayAll()

def delete_employee():
    db.remove(row[0])
    clearAll()
    messagebox.showinfo("Success", "Record Deleted")
    displayAll()



def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0,END)




#Creating Button frame:
btn_frame=Frame(entries_frame,bg="#535c68")
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky="w")
btnAdd=Button(btn_frame,command=add_employee,text="Add Details",width=15,
              font=("Calibri",16,"bold"),fg="white",bg="#16a885",bd=0).grid(row=0,column=0)
btnEdit=Button(btn_frame,command=update_employee,text="Update Details",width=15,
               font=("Calibri",16,"bold"),fg="white",bg="#16a885",bd=0).grid(row=0,column=1,padx=10)
btnDelete=Button(btn_frame,command=delete_employee,text="Delete Details",width=15,
                 font=("Calibri",16,"bold"),fg="white",bg="#16a885",bd=0).grid(row=0,column=2,padx=10)
btnEdit=Button(btn_frame,command=clearAll,text="Clear All",width=15,
               font=("Calibri",16,"bold"),fg="white",bg="#16a885",bd=0).grid(row=0,column=3,padx=10)

# Table Frame:
tree_frame = Frame(root,bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1400, height=520)
style=ttk.Style()
style.configure("mysytle.Treeview", font=("Calibri", 18),
                rowheight=50) # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=("Calibri",18)) # Modify the font of the heading
tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),
                style= "mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=5)
tv.heading("2",text="Name")
tv.heading("3",text="Age")
tv.column("3",width=5)
tv.heading("4",text="D.O.J")
tv.column("4",width=10)
tv.heading("5",text="E-Mail")
tv.heading("6",text="Gender")
tv.column("6",width=10)
tv.heading("7",text="Contact")
tv.column("7",width=10)
tv.heading("8",text="Address")
tv['show']='headings'
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)


displayAll()
root.mainloop()

