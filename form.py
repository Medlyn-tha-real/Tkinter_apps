from tkinter import *
import tkinter.messagebox


def success():
    tkinter.messagebox.showinfo("Complete", f"Hi {username_info}, you registered successfully!!")


def register_user():
    global username_info
    username_info = username.get()
    password_info = password.get()
    file = open(username_info+".txt", "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    # Label(screen1, text="Registration Success!", fg="green", font=("Calibri", 11)).place(x=85, y=160)
    success()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    # Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).place(x=110, y=130)


def login():
        print("Login session started")


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text="Notes 1.0", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()


main_screen()


