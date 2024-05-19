from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry("500x530")
root.title("Convert World")


def exitt():
    exit()


def abt():
    tkinter.messagebox.showinfo("Brown's dream World", '''Created and designed by Brown, here is the best forum for checking currencies rates.
Let's know if you have any new idea or suggestion that can make the forum a more suitable and convenient place for all.\n
                                    Thanks for servicing with us.''')


var = tkinter.StringVar()
var1 = tkinter.StringVar()
am = tkinter.IntVar()
# ans = tkinter.IntVar()


def currency_converter():
    one = var.get()
    two = var1.get()
    three = am.get()

    def to_naira():
        united = three * 362.23
        euro = three * 407.16
        canada = three * 271.69
        pound = three * 446.76
        yen = three * 3.44

        if one == "U.S dollar" and two == "Naira":
            tkinter.messagebox.showinfo("Output", f"{united}")
        elif one == "Euro" and two == "Naira":
            tkinter.messagebox.showinfo("Output", f"{euro}")
        elif one == "Canadian dollar" and two == "Naira":
            tkinter.messagebox.showinfo("Output", f"{canada}")
        elif one == "Pounds" and two == "Naira":
            tkinter.messagebox.showinfo("Output", f"{pound}")
        elif one == "Yen" and two == "Naira":
            tkinter.messagebox.showinfo("Output", f"{yen}")

    def to_yen():
        united = three * 105.40
        euro = three * 118.48
        canada = three * 79.06
        pound = three * 130.94
        Naira = three * 0.29

        if one == "USD" and two == "Yen":
            tkinter.messagebox.showinfo("Output", f"{united}")
        elif one == "Euro" and two == "Yen":
            tkinter.messagebox.showinfo("Output", f"{euro}")
        elif one == "Canadian dollar" and two == "Yen":
            tkinter.messagebox.showinfo("Output", f"{canada}")
        elif one == "Pounds" and two == "Yen":
            tkinter.messagebox.showinfo("Output", f"{pound}")
        elif one == "Naira" and two == "Yen":
            tkinter.messagebox.showinfo("Output", f"{Naira}")

    def to_dollars():
        euro = three * 1.124
        canada = three * 0.751
        pounds = three * 1.228
        Naira = three * 0.0028
        yen = three * 0.009440

        if one == "Euro" and two == "U.S dollar":
            tkinter.messagebox.showinfo("Output", f"{euro}")
        elif one == "Canadian dollar" and two == "U.S dollar":
            tkinter.messagebox.showinfo("Output", f"{canada}")
        elif one == "Pounds" and two == "U.S dollar":
            tkinter.messagebox.showinfo("Output", f"{pounds}")
        elif one == "Naira" and two == "U.S dollar":
            tkinter.messagebox.showinfo("Output", f"{Naira}")
        elif one == "Yen" and two == "U.S dollar":
            tkinter.messagebox.showinfo("Output", f"{yen}")

    def to_pounds():
        united = three * 0.815
        euro = three * 0.915
        canada = three * 0.612
        Naira = three * 0.0023
        yen = three * 0.007693

        if one == "U.S dollar" and two == "Pounds":
            tkinter.messagebox.showinfo("Output", f"{united}")
        elif one == "Euro" and two == "Pounds":
            tkinter.messagebox.showinfo("Output", f"{euro}")
        elif one == "Canadian dollar" and two == "Pounds":
            tkinter.messagebox.showinfo("Output", f"{canada}")
        elif one == "Naira" and two == "Pounds":
            tkinter.messagebox.showinfo("Output", f"{Naira}")
        elif one == "Yen" and two == "Pounds":
            tkinter.messagebox.showinfo("Output", f"{yen}")

    def to_canada():
        united = three * 1.331
        euro = three * 1.496
        pounds = three * 1.635
        Naira = three * 0.0037
        yen = three * 0.012578

        if one == "U.S dollar" and two == "Canadian dollar":
            tkinter.messagebox.showinfo("Output", f"{united}")
        elif one == "Euro" and two == "Canadian dollar":
            tkinter.messagebox.showinfo("Output", f"{euro}")
        elif one == "Pounds" and two == "Canadian dollar":
            tkinter.messagebox.showinfo("Output", f"{pounds}")
        elif one == "Naira" and two == "Canadian dollar":
            tkinter.messagebox.showinfo("Output", f"{Naira}")
        elif one == "Yen" and two == "Canadian dollar":
            tkinter.messagebox.showinfo("Output", f"{yen}")

    def to_euro():
        united = three * 0.89
        canada = three * 0.668
        pounds = three * 1.093
        Naira = three * 0.0025
        yen = three * 0.008426

        if one == "U.S dollar" and two == "Euro":
            tkinter.messagebox.showinfo("Output", f"{united}")
        elif one == "Canadian dollar" and two == "Euro":
            tkinter.messagebox.showinfo("Output", f"{canada}")
        elif one == "Pounds" and two == "Euro":
            tkinter.messagebox.showinfo("Output", f"{pounds}")
        elif one == "Naira" and two == "Euro":
            tkinter.messagebox.showinfo("Output", f"{Naira}")
        elif one == "Yen" and two == "Euro":
            tkinter.messagebox.showinfo("Output", f"{yen}")

    if one != "" and two == "Naira":
        to_naira()
    elif one != "" and two == "Yen":
        to_yen()
    elif one != "" and two == "U.S dollar":
        to_dollars()
    elif one != "" and two == "Pounds":
        to_pounds()
    elif one != "" and two == "Canadian dollar":
        to_canada()
    elif one != "" and two == "Euro":
        to_euro()
    else:
        tkinter.messagebox.showinfo("Error", "No field should be blank!!")
    # except (_tkinter.TclError):
    #     tkinter.messagebox.showinfo("Error", "No field should be blank!!")


menu = tkinter.Menu(root)
root.config(menu=menu)


subm1 = tkinter.Menu(menu)
menu.add_cascade(label="File", menu=subm1)
subm1.add_command(label="Exit", command=exitt)

subm2 = tkinter.Menu(menu)
menu.add_cascade(label="Option", menu=subm2)
subm2.add_command(label="About", command=abt)


label_0 = tkinter.Label(root, text="Convert World", fg="Green", width=20, relief="solid", font=("arial", 23, "bold"))
label_0.place(x=50, y=70)

label_1 = tkinter.Label(root, text="Currency Mode: ", width=20, fg="blue",  font=("bold", 12))
label_1.place(x=80, y=192)

list1 = ["Canadian dollar", "Pounds", "Yen", "Naira", "Euro", "U.S dollar"]
drop_list_1 = tkinter.OptionMenu(root, var, *list1)
var.set("Select currency")
drop_list_1.config(width=15)
drop_list_1.place(x=250, y=190)

label_2 = tkinter.Label(root, text="Amount: ", width=20, fg="blue",  font=("bold", 12))
label_2.place(x=55, y=260)

entry_2 = tkinter.Entry(root, textvar=am)
entry_2.place(x=250, y=264)

label_3 = tkinter.Label(root, text="Convert to: ", width=20, fg="blue",  font=("bold", 12))
label_3.place(x=62, y=323)

list2 = ["Canadian dollar", "Pounds", "Yen", "Naira", "Euro", "U.S dollar"]
drop_list_2 = tkinter.OptionMenu(root, var1, *list2)
var1.set("Select currency")
drop_list_2.config(width=15)
drop_list_2.place(x=245, y=320)

# entry_3 = tkinter.Entry(root, textvar=ans)
# entry_3.place(x=180, y=400)


but_signup = tkinter.Button(root, text="Convert", width=12, bg="blue", fg="white", command=currency_converter).place(x=130, y=420)
but_exit = tkinter.Button(root, text="Quit", width=12, bg="blue", fg="white", command=exitt).place(x=280, y=420)


root.mainloop()
