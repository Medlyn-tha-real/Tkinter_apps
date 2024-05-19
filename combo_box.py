from tkinter import *
# from PIL import Image, ImageTk


root = Tk()
root.geometry("500x500")
root.title("Registration Form")

# pic = Image.open("C:/Users/USER/Desktop/library/connect/foam.png")
# photo = ImageTk.PhotoImage(pic)
#
# lab = tkinter.Label(image=photo)
# lab.pack()

fn = StringVar()
ln = StringVar()
dob = IntVar()
var = StringVar()


def printt():
    first = fn.get()
    sec = ln.get()
    dob1 = dob.get()
    var1 = var.get()
    print(f"Your Fullname is {first} {sec}")
    print(f"Your age is {dob1}")
    print(f"You are from {var1}")



def exitt():
    exit()


label_0 = Label(root, text="Registration Form", fg="blue", relief="solid", width=20, font=("arial", 19, "bold"))
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


but_signup = Button(root, text="Signup", width=12, bg="brown", fg="white", command=printt).place(x=150, y=450)
but_exit = tkinter.Button(root, text="Quit", width=12, bg="brown", fg="white", command=exitt).place(x=280, y=450)

root.mainloop()


