from tkinter import *

me = Tk()
me.geometry("354x460")
me.title("CALCULATOR")
me_label = Label(me, text="CALCULATOR", bg="dark grey", font=("Times", 30, "bold"))
me_label.pack(side=TOP)
me.config(background="dark grey")

text_in = StringVar()
operator = ""


def click_but(number):          # lambda:click_but(1)
    global operator
    operator = operator + str(number)
    text_in.set(operator)


def equate_but():
    global operator
    equate = str(eval(operator))
    text_in.set(equate)
    operator = ''


def clear_but():
    text_in.set('')


me_text = Entry(me, font=("Courier", 12, "bold"), textvar=text_in, width=25, bd=5, bg="powder blue")
me_text.pack()

but1 = Button(me, padx=14, pady=14, bd=4, bg="white", command=lambda: click_but(1), text="1", font=("Courier New", 16, "bold"))
but1.place(x=10, y=100)

but2 = Button(me, padx=14, pady=14, bd=4, bg="white", command=lambda: click_but(2), text="2", font=("Courier New", 16, "bold"))
but2.place(x=10, y=170)

but3 = Button(me, padx=14, pady=14, bd=4, bg="white", command=lambda: click_but(3), text="3", font=("Courier New", 16, "bold"))
but3.place(x=10, y=240)

but4 = Button(me, padx=14, pady=14, bd=4, bg="white", command=lambda: click_but(4), text="4", font=("Courier New", 16, "bold"))
but4.place(x=75, y=100)

but5 = Button(me, padx=14, pady=14, bd=4, bg="white", command=lambda: click_but(5), text="5", font=("Courier New", 16, "bold"))
but5.place(x=75, y=170)

but6 = Button(me, padx=14, pady=14, bd=4, bg="white", command=lambda: click_but(6), text="6", font=("Courier New", 16, "bold"))
but6.place(x=75, y=240)

but7 = Button(me, padx=14, pady=14, bd=4, bg="white", command=lambda: click_but(7), text="7", font=("Courier New", 16, "bold"))
but7.place(x=140, y=100)

but8 = Button(me, padx=14, pady=14, bd=4, bg="white", command=lambda: click_but(8), text="8", font=("Courier New", 16, "bold"))
but8.place(x=140, y=170)

but9 = Button(me, padx=14, pady=14, bd=4, bg="white", command=lambda: click_but(9), text="9", font=("Courier New", 16, "bold"))
but9.place(x=140, y=240)

but0 = Button(me, padx=14, pady=14, bd=4, bg="white", command=lambda: click_but(0), text="0", font=("Courier New", 16, "bold"))
but0.place(x=10, y=310)

but_dot = Button(me, padx=47, pady=14, bd=4, bg="white", command=lambda: click_but("."), text=".", font=("Courier New", 16, "bold"))
but_dot.place(x=75, y=310)

but_dot1 = Button(me, padx=14, pady=14, bd=4, bg="white", command=lambda: click_but("+"), text="+", font=("Courier New", 16, "bold"))
but_dot1.place(x=205, y=100)

but_dot2 = Button(me, padx=14, pady=14, bd=4, bg="white", command=lambda: click_but("-"), text="-", font=("Courier New", 16, "bold"))
but_dot2.place(x=205, y=170)

but_dot3 = Button(me, padx=14, pady=14, bd=4, bg="white", command=lambda: click_but("*"), text="*", font=("Courier New", 16, "bold"))
but_dot3.place(x=205, y=240)

but_dot4 = Button(me, padx=14, pady=14, bd=4, bg="white", command=lambda: click_but("/"), text="/", font=("Courier New", 16, "bold"))
but_dot4.place(x=205, y=310)

but_dot5 = Button(me, padx=14, pady=119, bd=4, bg="white", command=clear_but, text="CE", font=("Courier New", 16, "bold"))
but_dot5.place(x=270, y=100)

but_dot6 = Button(me, padx=151, pady=14, bd=4, bg="white", command=equate_but, text="=", font=("Courier New", 16, "bold"))
but_dot6.place(x=10, y=380)

me.mainloop()





















































































