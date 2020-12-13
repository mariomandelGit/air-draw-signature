import tkinter as tk
import tkinter.font as font
import signature
import draw


def openSigWindow(window):
    window.destroy()
    signature.callSignature()


def openSigInstructionsWindow(window):
    window.destroy()
    # Toplevel object which will
    # be treated as a new window
    newWindow = tk.Tk()

    newWindow.state("normal")
    # sets the title of the
    # Toplevel widget
    newWindow.title("Air Signature Instructions")
    newWindow.config(bg='#D9CB8D')
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
    InstructionHeader = font.Font(family='Courier', size=18, weight='bold')
    InstructionFont = font.Font(family='Courier', size=14, weight='bold')
    # A Label widget to show in toplevel
    tk.Label(newWindow, text="This page will explain how to use the Air Signature tool.\n\n", font=InstructionHeader,
             bg='#D9CB8D').pack()
    tk.Label(newWindow, text="First of all, you'll need a blue item to draw with that will be easily recognizable to "
                             "the camera...\n\n", font=InstructionFont, bg='#D9CB8D').pack()
    tk.Label(newWindow, text="Also make sure to remove any other blue objects within the view of the camera.\n\n",
             font=InstructionFont, bg='#D9CB8D').pack()
    tk.Label(newWindow, text="Once the program opens, the camera will track the blue object and that is what you will "
                             "use to write.\n\n", font=InstructionFont, bg='#D9CB8D').pack()
    tk.Label(newWindow, text="Then, to start your signature, bring the blue object to the portion of the screen that "
                             "says \"clear all\".\n\n", font=InstructionFont, bg='#D9CB8D').pack()
    tk.Label(newWindow, text="This will clear the screen to give you a clean canvas to write your signature on.\n\n",
             font=InstructionFont, bg='#D9CB8D').pack()
    tk.Label(newWindow, text="Finally, it is time to write your signature using the blue object as your pen.\n\n",
             font=InstructionFont, bg='#D9CB8D').pack()
    tk.Label(newWindow, text="Once you're finished, if you would like to save your signature you may either press "
                             "the\nsave button from the original page or press CTRL+S on your keyboard to save.\n\n",
             font=InstructionFont, bg='#D9CB8D').pack()
    tk.Button(newWindow, text="Click here to start process", command=lambda: openSigWindow(newWindow)).pack()
    newWindow.mainloop()


def openDrawWindow(window):
    window.destroy()
    draw.callDraw()


def openDrawInstructionsWindow(window):
    window.destroy()
    # Toplevel object which will
    # be treated as a new window
    newWindow = tk.Tk()

    newWindow.state("normal")
    # sets the title of the
    # Toplevel widget
    newWindow.title("Draw Instructions")
    newWindow.config(bg='#D9CB8D')
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
    InstructionHeader = font.Font(family='Courier', size=18, weight='bold')
    InstructionFont = font.Font(family='Courier', size=14, weight='bold')
    # A Label widget to show in toplevel
    tk.Label(newWindow, text="This page will explain how to use the draw tool.\n\n", font=InstructionHeader,
             bg='#D9CB8D').pack()
    tk.Label(newWindow, text="First of all, you'll need a blue item to draw with that will be easily recognizable to "
                             "the camera...\n\n", font=InstructionFont, bg='#D9CB8D').pack()
    tk.Label(newWindow, text="Also make sure to remove any other blue objects within the view of the camera.\n\n",
             font=InstructionFont, bg='#D9CB8D').pack()
    tk.Label(newWindow, text="Once the program opens, the camera will track the blue object and that is what you will "
                             "use to write.\n\n", font=InstructionFont, bg='#D9CB8D').pack()
    tk.Label(newWindow, text="Now you're free to draw! Draw whatever you would like, use CTRL+S to save your drawing,"
                             "\n or move the object to the clear all section for a clean canvas\n\n",
             font=InstructionFont, bg='#D9CB8D').pack()
    tk.Button(newWindow, text="Click here to start process", command=lambda: openDrawWindow(newWindow)).pack()
    newWindow.mainloop()

class Application():

    def __init__(self):
        window = tk.Tk()
        window.title('Air Signature')
        window.state("normal")
        window.config(bg='#D9CB8D')
        buttonFont = font.Font(family='Courier', size=25, weight='bold')
        tk.Button(text='Draw Your Signature', height=4, width=25, bg='grey', font=buttonFont,
                  command=lambda: openSigInstructionsWindow(window)).place(side=tk.RIGHT)
        tk.Button(text='Free Draw', height=4, width=25, bg='grey', font=buttonFont).place(side=tk.LEFT)
        window.mainloop()


Application()
