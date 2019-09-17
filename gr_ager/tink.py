from tkinter import Tk, BOTH
from tkinter.ttk import Frame


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.centerWindow()

    def initUI(self):
        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=True)

    def centerWindow(self):
        w = 290
        h = 150
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():
    root = Tk()
    root.geometry('550x350+300+300')
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
