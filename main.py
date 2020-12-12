import tkinter as tk
import tkinter.font as font
import signature


def openNewWindow(window):
    # Toplevel object which will
    # be treated as a new window
    newWindow = tk.Toplevel(window)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("200x200")

    # A Label widget to show in toplevel
    tk.Label(newWindow, text="This is a new window").pack()


def openSigWindow():
    signature.callSignature()


class Application():

    def __init__(self):
        window = tk.Tk()
        window.title('Air Signature')
        window.state("normal")
        window.config(bg= '#D9CB8D')
        buttonFont = font.Font(family='Courier', size=25, weight='bold')
        tk.Button(text='Draw Your Signature', height=4, width=25, bg='grey', font=buttonFont, command=openSigWindow).place(x=380, y=125)
        tk.Button(text='Save Your Signature', height=4, width=25, bg='grey', font=buttonFont).place(x=80, y=375)
        tk.Button(text='Free Draw', height=4, width=25, bg='grey', font=buttonFont).place(x=680, y=375)
        window.mainloop()


Application()
