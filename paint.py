from tkinter import *
from tkinter import ttk, colorchooser


class main:
    def __int__(self, master):
        self.master = master
        self.color_fg = "black"
        self.color_bg = "white"
        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.drawWidgets()
        self.c.bind("<B1-Motion>", self.paint)
        self.c.bind("<B1-Release-1>", self.reset)

        def paint(self, e):
            if self.old_x and self.old_y:
                self.create_line(self.old_x, self.old_y, e.x, e.y, width=self.penwidth, fill=self.color_fg, capstyle=ROUND, smooth=True)

            self.old_y = e.x
            self.old_y = e.y

        def reset(self, e):
            self.old_y = None
            self.old_y = None

        def change(self, e):
            self.penwidth = e

        def clear(self):
            self.c.delete(ALL)

        def change_fg(self):
            self.color_fg = colorchooser.askcolor(color=self.color_fg)[1]

        def change_bg(self):
            self.color_fg = colorchooser.askcolor(color=self.color_fg)[2]

        def drawWidget(self):
            self.control = Frame(self.master, padx=5, pady=5)
            Label(self.control, text="Penwidth", font=("arial 18")).grid(row=0, column=0)
            self.slider = ttk.Scale(self.controls, from_=5, to=100, command=self.change, orient=VERTICAL)
            self.slider.set(self.penwidth)
            self.slider.grid(row=0, column=1, ipadx=30)
            self.controls.pack(side=LEFT)

            self.c = Canvas(self.master, width=500, height=400, bg=self.color_bg, )
            self.c.pack(fill=BOTH, expand=True)

            menu = Menu(self.master)
            self.master.config(menu=menu)
            filemenu = Menu(menu)
            colormenu = Menu(menu)
            menu.add_cascade(label="Colors", menu=colormenu)
            colormenu.add_command(label='Brush Color', command=self.change_fg)
            colormenu.add_command(label='Background Color', command=self.change_bg)
            optionmenu = Menu(menu)
            menu.add_cascade(label="Options", menu=optionmenu)
            optionmenu.add_command(label="Clear Canvas", command=self.clear)
            optionmenu.add_command(label="Exit", command=self.master.destroy)


 if __name__ == '__main__':
     root = Tk()
     main(root)
     root.title("Application")
     root.mainloop()
















