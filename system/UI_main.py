from tkinter import *


class win:
    def __init__(self):
        self.me = Tk()
        self.me.title('sxy system')

    def resize(self, x, y):
        self.me.geometry(x + 'x' + y)

    def close(self):
        self.me.quit()

    def add_Button(self, x, y, title, cmd):
        Btn = Button(self.me, text=title, command=cmd)
        Btn.pack()

    def add_Button_1(self):
        def n_1(): self.me.quit()

        Btn = Button(self.me, text='退出', command=n_1)
        Btn.pack()
