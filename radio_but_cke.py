from tkinter import *
import sqlite3
import tkinter.messagebox
# from PIL import Image, ImageTk


root = Tk()
root.geometry("530x570")
root.title("Registration Form")

# imge = Image.open("C:/Users/USER/Desktop/library/connect/foam.png")
# photo = ImageTk.PhotoImage(imge)
#
# lab = tkinter.Label(image=photo)
# lab.pack()


fn = StringVar()
ln = StringVar()
dob = StringVar()
var = StringVar()
var_c1 = "Java"
var_c2 = "Python"
var_c3 = "JavaScript"
radio_var = StringVar()


def exitt():
    exit()


def abt():
    tkinter.messagebox.showinfo("Welcome to authors", "This is demo for menu fields. ")


def database():
    name1 = fn.get()
    last1 = ln.get
    date = dob.get()
    country = var.get()
    prog = var_c2
    gender = radio_var.get()
    con = sqlite3.connect("Form.db")
    with con:
        cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Students (Name TEXT,Last TEXT,DOB TEXT,country TEXT,Proggraming TEXT,Gender TEXT)")
    cursor.execute("INSERT INTO Students(Name,Last,DOB,country,Proggraming,Gender) VALUES(?,?,?,?,?,?)", (name1, last1, date, country, prog, gender))
    con.commit()


menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="File", menu=subm1)
subm1.add_command(label="Exit", command=exitt)

subm2 = Menu(menu)
menu.add_cascade(label="Option", menu=subm2)
subm2.add_command(label="About", command=abt)


'''def printt():
    first = fn.get()
    sec = ln.get()
    dob1 = dob.get()
    var1 = var.get()
    var3 = var1
    var3 = var_c2
    var3 = var_c3
    var4 = radio_var.get()
    
    print(f"Your Fullname is {first} {sec}.")
    print(f"Your age is {dob1}.")
    print(f"You are from {var1}.")
    print(f"Your language is {var3}.")
    print(f"You are a {var4}.")
    tkinter.messagebox.showinfo("Welcome", f"{first} {sec} is successfully signed up !!")'''


def second_wind():
    window = Tk()
    window.title("Welcome to second window")
    window.geometry("250x200")
    label_02 = Label(window, text="Registration successful", relief="solid", font=("arial", 12, "bold")).place(x=30, y=70)
    but_01 = Button(window, text="demo", width=12, bg="brown", fg="white", command=abt).place(x=80, y=110)


label_0 = Label(root, text="Registration Form", fg="blue", relief="solid", width=20, font=("arial", 20, "bold"))
label_0.place(x=90, y=150)


label_1 = Label(root, text="First Name: ", fg="blue", width=20, font=("bold", 10))
label_1.place(x=80, y=240)

entry_1 = Entry(root, textvar=ln)
entry_1.place(x=240, y=242)

label_2 = Label(root, text="Last Name: ", fg="blue", width=20, font=("bold", 10))
label_2.place(x=80, y=280)

entry_2 = Entry(root, textvar=fn)
entry_2.place(x=240, y=282)

label_3 = Label(root, text="DOB: ", width=20, fg="blue", font=("bold", 10))
label_3.place(x=60, y=320)

entry_3 = Entry(root, textvar=dob)
entry_3.place(x=240, y=322)

label_4 = Label(root, text="Country: ", width=20, fg="blue",  font=("bold", 10))
label_4.place(x=68, y=360)


list1 = ["Canada", "America", "London", "Switzerland", "Manchester", "Poland", "Nigeria"]
drop_list = OptionMenu(root, var, *list1)
var.set("Select country")
drop_list.config(width=15)
drop_list.place(x=235, y=360)

label_5 = Label(root, text="Pro Language: ", width=20, fg="blue",  font=("bold", 10))
label_5.place(x=88, y=400)

c1 = Checkbutton(root, text="Java", variable=var_c1).place(x=240, y=400)
c2 = Checkbutton(root, text="Python", variable=var_c1).place(x=295, y=400)
c3 = Checkbutton(root, text="JavaScript", variable=var_c1).place(x=365, y=400)

r1 = Radiobutton(root, text="Male", variable=radio_var, value="Male").place(x=240, y=440)
r2 = Radiobutton(root, text="Female", variable=radio_var, value="Female").place(x=300, y=442)


label_6 = Label(root, text="Gender: ", width=20, fg="blue",  font=("bold", 10))
label_6.place(x=68, y=440)

but_login = Button(root, text="Signup", width=12, bg="brown", fg="white", command=database).place(x=130, y=510)
root.bind("<Return>", database)


but_quit = Button(root, text="Quit", width=12, bg="brown", fg="white", command=exitt).place(x=280, y=510)
# but_login = tkinter.Button(root, text="Login", width=12, bg="brown", fg="white", command=second_wind).place(x=280, y=510)


root.mainloop()
