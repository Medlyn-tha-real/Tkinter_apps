from tkinter import *
import tkinter.messagebox


tk = Tk()
tk.title("Tic Tac Toe")

playera = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()


def exitt():
    exit()


def abt():
    tkinter.messagebox.showinfo("Brown's World", '''Tic-Tac-Toe for all, the game for two is very easy to learn and interesting to play.
Created an designed by brown, thanks for trying this out and i hope you guys play smart. 
                                                                                    Have fun!!.''')


menu = tkinter.Menu(tk)
tk.config(menu=menu)


subm1 = tkinter.Menu(menu)
menu.add_cascade(label="File", menu=subm1)
subm1.add_command(label="Exit", command=exitt)

subm2 = tkinter.Menu(menu)
menu.add_cascade(label="Option", menu=subm2)
subm2.add_command(label="About", command=abt)


player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)


bclick = True
flag = 0


def delete():
    button1.configure(state=END(ALL))
    button2.configure(state=END(ALL))
    button3.configure(state=END(ALL))
    button4.configure(state=END(ALL))
    button5.configure(state=END(ALL))
    button6.configure(state=END(ALL))
    button7.configure(state=END(ALL))
    button8.configure(state=END(ALL))
    button9.configure(state=END(ALL))


def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


def btnClick(buttons):
    global bclick, flag, player2_name, player1_name, playerb, playera
    if buttons["text"] == " " and bclick:
        buttons["text"] = "X"
        bclick = False
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        checkForWin()
        flag += 1

    elif buttons["text"] == " " and not bclick:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already clicked!")


def checkForWin():
    if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
        button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
        button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
        button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
        button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
        button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
       button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playera)
        play_again = tkinter.messagebox.askquestion("Tic-Tac-Toe", "Play again?")
        if play_again == "yes":
            delete()
        elif play_again == "no":
            disableButton()

    elif flag == 8:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It's is a Tie")
        play_again = tkinter.messagebox.askquestion("Tic-Tac-Toe", "Play again?")
        if play_again == "yes":
            delete()
        elif play_again == "no":
            disableButton()

    elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
          button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
          button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
          button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
          button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or
          button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
          button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
          button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)
        play_again = tkinter.messagebox.askquestion("Tic-Tac-Toe", "Play again?")
        if play_again == "yes":
            delete()
        elif play_again == "no":
            disableButton()


# buttons = StringVar()


label = Label(tk, text=" Player 1:", font="Times 20 bold", bg="white", fg="black", height=1, width=8)
label.grid(row=1, column=0)

label = Label(tk, text=" Player 2:", font="Times 20 bold", bg="white", fg="black", height=1, width=8)
label.grid(row=2, column=0)

button1 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white", height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white", height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white", height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white", height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white", height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white", height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white", height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white", height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white", height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

tk.mainloop()





