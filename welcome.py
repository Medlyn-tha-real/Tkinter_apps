from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")


label1 = Label(window, text="Welcome to Tkinter", fg='blue', bg='yellow', relief='solid', font=("arial", 18, "bold"))
# label1.pack(fill='both', pady=2, padx=2, expand=True)
label1.pack()

button1 = Button(window, text='Demo', fg='white', bg='brown', relief='raised', font=("arial", 12, 'bold'))
button1.place(y=110, x=110)                  # options of relief: groove, ridge, sunken, raised

window.mainloop()


























# import tkinter
# from tkinter.constants import *
# tk = tkinter.Tk()
# frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
# frame.pack(fill=BOTH,expand=1)
# label = tkinter.Label(frame, text="Hello, World")
# label.pack(fill=X, expand=1)
# button = tkinter.Button(frame,text="Exit",command=tk.destroy)
# button.pack(side=BOTTOM)
# tk.mainloop()











