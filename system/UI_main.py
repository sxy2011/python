from tkinter import *


class win:
    def __init__(self):
        self.me = Tk()
        self.me.title('sxy system')
        self.me.geometry('400x400')
        canvas = Canvas(self.me, width=400, height=400, bd=0, highlightthickness=0)
        canvas.pack()
        self.add_Button_1()
        self.me.mainloop()

    def resize(self, x, y):
        self.me.geometry(x + 'x' + y)

    def close(self):
        self.me.quit()

    def add_Button(self, x, y, title, cmd):
        Btn = Button(self.me, text=title, command=cmd)
        Btn.pack()

    def add_Button_1(self):
        Btn = Button(self.me, text='退出', command=self.me.quit)
        Btn.pack(side='bottom')
