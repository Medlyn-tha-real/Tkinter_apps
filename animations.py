from tkinter import *
import time
root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()


# def animate(event):
canvas.create_polygon(10, 10, 10, 60, 50, 35, fill="blue")
for i in range(0, 60):
    canvas.move(1, 5, 0)
    root.update()
    time.sleep(0.03)






# canvas.bind("<Return>", animate)



root.mainloop()

















