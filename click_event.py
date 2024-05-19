import tkinter
window = tkinter.Tk()
window.geometry("450x400")
window.title("Registration Form")


def printt():
    print("Demo tkinter")

def exit1():
    exit()


label1 = tkinter.Label(window, text="Registration Form", relief="solid", width=20, font=("arial", 19, "bold"))
label1.place(x=70, y=53)

label2 = tkinter.Label(window, text="FirstName", width=20, font=("arial", 10, "bold"))
label2.place(x=80, y=130)

label3 = tkinter.Label(window, text="LastName", width=20, font=("arial", 10, "bold"))
label3.place(x=80, y=170)

button1 = tkinter.Button(window, text="Login", width=12, bg="brown", fg="white", command=printt)
button1.place(x=120, y=300)

button2 = tkinter.Button(window, text="Quit", width=12, bg="brown", fg="white", command=exit1)
button2.place(x=250, y=300)

window.mainloop()

