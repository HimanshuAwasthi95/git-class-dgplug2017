from tkinter import *


class Calculator:
    def __init__(self):

        window = Tk()
        window.title("calculator")

        self.string = StringVar()
        entry = Entry(window, textvariable=self.string)
        entry.grid(row=0, column=0, columnspan=6)
        entry.focus()

        values = ["7", "8", "9", "/", "Clear", "<-", "4", "5", "6", "*", "(", ")", "1",
                  "2", "3", "-", "=", "0", ".", "%", "+"]

        i = 0
        row = 1
        col = 0

        for txt in values:

            padx = 10
            pady = 10

            if i == 6:
                row = 2
                col = 0

            if i == 12:
                row = 3
                col = 0

            if i == 17:
                row = 4
                col = 0

            if txt == "=":

                btm = Button(window, height=2, width=4, padx=23, pady=23, text=txt,
                             command=lambda txt=txt: self.equals())
                btm.grid(row=row, column=col, columnspan=2, rowspan=2, padx=1, pady=1)

            elif txt == "Clear":

                btm = Button(window, height=2, width=4, padx=padx, pady=pady, text=txt,
                             command=lambda txt=txt: self.clearTxt())
                btm.grid(row=row, column=col, padx=1, pady=1)


            elif txt == "<-":

                btm = Button(window, height=2, width=4, padx=padx, pady=pady, text=txt,
                             command=lambda txt=txt: self.delete())
                btm.grid(row=row, column=col, padx=1, pady=1)

            else:

                btm = Button(window, height=2, width=4, padx=padx, pady=pady, text=txt,
                             command=lambda txt=txt: self.addChar(txt))
                btm.grid(row=row, column=col, padx=1, pady=1)

            col = col + 1
            i = i + 1

        window.mainloop()

    def clearTxt(self):

        self.string.set(" ")

    def equals(self):

        result = " "

        try:

            result = eval(self.string.get())
        except:
            result = "Error"

        self.string.set(result)

    def addChar(self, char):
        self.string.set(self.string.get() + (str(char)))

    def delete(self):
        self.string.set(self.string.get()[0:-1])


Calculator()
