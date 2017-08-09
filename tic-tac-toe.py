# First game in python
# tic-tac-toe game
# use tkinter module

from tkinter import *
import tkinter.messagebox

root = Tk()
root.title('tic tac toe')

button_click = True


def tictactoe(buttons):

    global button_click

    if button1['text'] == 'x' and button2['text'] == 'x' and button3['text'] == 'x':

        tkinter.messagebox.showinfo('winner X', 'player x won the game')
    elif buttons['text'] == " " and button_click == True:
        buttons['text'] = 'x'
        button_click = False

    elif buttons['text'] == " " and button_click == False:
        buttons['text'] = '0'
        button_click = True

    if button1['text'] == 'x' and button4['text'] == 'x' and button7['text'] == 'x':

        tkinter.messagebox.showinfo('winner X', 'player x won the game')
    elif buttons['text'] == " " and button_click == True:
        buttons['text'] = 'x'
        button_click = False

    elif buttons['text'] == " " and button_click == False:
        buttons['text'] = '0'
        button_click = True
    if button1['text'] == 'x' and button5['text'] == 'x' and button9['text'] == 'x':

        tkinter.messagebox.showinfo('winner X', 'player x won the game')
    elif buttons['text'] == " " and button_click == True:
        buttons['text'] = 'x'
        button_click = False

    elif buttons['text'] == " " and button_click == False:
        buttons['text'] = '0'
        button_click = True
    if button7['text'] == 'x' and button5['text'] == 'x' and button3['text'] == 'x':

        tkinter.messagebox.showinfo('winner X', 'player x won the game')
    elif buttons['text'] == " " and button_click == True:
        buttons['text'] = 'x'
        button_click = False

    elif buttons['text'] == " " and button_click == False:
        buttons['text'] = '0'
        button_click = True

    if button3['text'] == 'x' and button6['text'] == 'x' and button9['text'] == 'x':

        tkinter.messagebox.showinfo('winner X', 'player x won the game')
    elif buttons['text'] == " " and button_click == True:
        buttons['text'] = 'x'
        button_click = False

    elif buttons['text'] == " " and button_click == False:
        buttons['text'] = '0'
        button_click = True

    if button2['text'] == 'x' and button5['text'] == 'x' and button8['text'] == 'x':

        tkinter.messagebox.showinfo('winner X', 'player x won the game')
    elif buttons['text'] == " " and button_click == True:
        buttons['text'] = 'x'
        button_click = False

    elif buttons['text'] == " " and button_click == False:
        buttons['text'] = '0'
        button_click = True

    if button4['text'] == 'x' and button5['text'] == 'x' and button6['text'] == 'x':

        tkinter.messagebox.showinfo('winner X', 'player x won the game')
    elif buttons['text'] == " " and button_click == True:
        buttons['text'] = 'x'
        button_click = False

    elif buttons['text'] == " " and button_click == False:
        buttons['text'] = '0'
        button_click = True

    if button7['text'] == 'x' and button8['text'] == 'x' and button9['text'] == 'x':

        tkinter.messagebox.showinfo('winner X', 'player x won the game')
    elif buttons['text'] == " " and button_click == True:
        buttons['text'] = 'x'
        button_click = False

    elif buttons['text'] == " " and button_click == False:
        buttons['text'] = '0'
        button_click = True

    if button1['text'] == '0' and button2['text'] == '0' and button3['text'] == '0':

        tkinter.messagebox.showinfo('winner Y', 'player 0 won the game')
    elif buttons['text'] == " " and button_click == True:
        buttons['text'] = 'x'
        button_click = False

    elif buttons['text'] == " " and button_click == False:
        buttons['text'] = '0'
        button_click = True

    if button1['text'] == '0' and button4['text'] == '0' and button7['text'] == '0':
        tkinter.messagebox.showinfo('winner Y', 'player 0 won the game')
    elif buttons['text'] == " " and button_click == True:
        buttons['text'] = 'x'
        button_click = False

    elif buttons['text'] == " " and button_click == False:
        buttons['text'] = '0'
        button_click = True

    if button1['text'] == '0' and button5['text'] == '0' and button9['text'] == '0':
        tkinter.messagebox.showinfo('winner Y', 'player 0 won the game')
    elif buttons['text'] == " " and button_click == True:
        buttons['text'] = 'x'
        button_click = False

    elif buttons['text'] == " " and button_click == False:
        buttons['text'] = '0'
        button_click = True

    if button7['text'] == '0' and button5['text'] == '0' and button3['text'] == '0':
        tkinter.messagebox.showinfo('winner Y', 'player 0 won the game')
    elif buttons['text'] == " " and button_click == True:
        buttons['text'] = 'x'
        button_click = False

    elif buttons['text'] == " " and button_click == False:
        buttons['text'] = '0'
        button_click = True

    if button3['text'] == '0' and button6['text'] == '0' and button9['text'] == '0':
        tkinter.messagebox.showinfo('winner Y', 'player 0 won the game')
    elif buttons['text'] == " " and button_click == True:
        buttons['text'] = 'x'
        button_click = False

    elif buttons['text'] == " " and button_click == False:
        buttons['text'] = '0'
        button_click = True

    if button2['text'] == '0' and button5['text'] == '0' and button8['text'] == '0':
        tkinter.messagebox.showinfo('winner Y', 'player 0 won the game')
    elif buttons['text'] == " " and button_click == True:
        buttons['text'] = 'x'
        button_click = False

    elif buttons['text'] == " " and button_click == False:
        buttons['text'] = '0'
        button_click = True

    if button4['text'] == '0' and button5['text'] == '0' and button6['text'] == '0':
        tkinter.messagebox.showinfo('winner Y', 'player 0 won the game')
    elif buttons['text'] == " " and button_click == True:
        buttons['text'] = 'x'
        button_click = False

    elif buttons['text'] == " " and button_click == False:
        buttons['text'] = '0'
        button_click = True

    if button7['text'] == '0' and button8['text'] == '0' and button9['text'] == '0':

        tkinter.messagebox.showinfo('winner Y', 'player 0 won the game')
    elif buttons['text'] == " " and button_click == True:
        buttons['text'] = 'x'
        button_click = False

    elif buttons['text'] == " " and button_click == False:
        buttons['text'] = '0'
        button_click = True

    if button1['text'] != ' ' and button2['text'] != ' ' and button3['text'] != ' ' and button4['text'] != ' ' and button5['text'] != ' ' and button6['text'] != ' ' and button7['text'] != ' ' and button8['text'] != ' ' and button9['text'] != ' ':
        tkinter.messagebox.showinfo('No Winner', 'khichadi pak gai')

    
buttons = StringVar()
button1 = Button(root, text=' ', font=('Arial 30 bold'), height=4, width=8, command=lambda: tictactoe(button1))
button1.grid(row=1, column=0, sticky=S + N + E + W)

button2 = Button(root, text=' ', font=('Arial 30 bold'), height=4, width=8, command=lambda: tictactoe(button2))
button2.grid(row=1, column=1, sticky=S + N + E + W)

button3 = Button(root, text=' ', font=('Arial 30 bold'), height=4, width=8, command=lambda: tictactoe(button3))
button3.grid(row=1, column=2, sticky=S + N + E + W)

button4 = Button(root, text=' ', font=('Arial 30 bold'), height=4, width=8, command=lambda: tictactoe(button4))
button4.grid(row=2, column=0, sticky=S + N + E + W)

button5 = Button(root, text=' ', font=('Arial 30 bold'), height=4, width=8, command=lambda: tictactoe(button5))
button5.grid(row=2, column=1, sticky=S + N + E + W)

button6 = Button(root, text=' ', font=('Arial 30 bold'), height=4, width=8, command=lambda: tictactoe(button6))
button6.grid(row=2, column=2, sticky=S + N + E + W)

button7 = Button(root, text=' ', font=('Arial 30 bold'), height=4, width=8, command=lambda: tictactoe(button7))
button7.grid(row=3, column=0, sticky=S + N + E + W)

button8 = Button(root, text=' ', font=('Arial 30 bold'), height=4, width=8, command=lambda: tictactoe(button8))
button8.grid(row=3, column=1, sticky=S + N + E + W)

button9 = Button(root, text=' ', font=('Arial 30 bold'), height=4, width=8, command=lambda: tictactoe(button9))
button9.grid(row=3, column=2, sticky=S + N + E + W)

root.mainloop()
