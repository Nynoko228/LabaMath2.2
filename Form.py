import tkinter as tk
from matplotlib.mathtext import math_to_image
from io import BytesIO
from PIL import ImageTk, Image
from Scrolling import ScrollableImage


class Application(tk.Frame):
    def __init__(self, f, master=None):
        self.master = master
        tk.Frame.__init__(self, master)
        self.pack()
        self.fin = f
        self.createWidgets()



    def createWidgets(self):
        image = []
        image_window = []
        for i in range(len(self.fin)):
            # Creating buffer for storing image in memory
            buffer = BytesIO()
            # Writing png image with our rendered greek alpha to buffer
            math_to_image(self.fin[i], buffer, dpi=250, format='png')
            # Remoting bufeer to 0, so that we can read from it
            buffer.seek(0)
            # Creating Pillow image object from it
            pimage = Image.open(buffer)
            # Creating PhotoImage object from Pillow image object
            image += [ImageTk.PhotoImage(pimage)]
        image_window = (ScrollableImage(self.master, image=image, scrollbarwidth=9,
                                           width=1300, height=1000))
        image_window.pack()
