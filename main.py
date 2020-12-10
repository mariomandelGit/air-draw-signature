import tkinter as tk
import tkinter.font as font
from PIL import Image


class Application():
    def __init__(self):
        window = tk.Tk()
        window.title('Air Signature')
        window.state("zoomed")
        window.config(bg= '#D9CB8D')
        buttonFont = font.Font(family='Courier', size=25, weight='bold')
        tk.Button(text='Draw Your Signature', height=4, width=25, bg='grey', font=buttonFont).place(x=380, y=125)
        tk.Button(text='Save Your Signature', height=4, width=25, bg='grey', font=buttonFont).place(x=80, y=375)
        tk.Button(text='Free Draw', height=4, width=25, bg='grey', font=buttonFont).place(x=680, y=375)
        window.mainloop()


Application()
