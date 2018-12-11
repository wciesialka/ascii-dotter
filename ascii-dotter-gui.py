#ascii-dotter-gui
#William Ciesialka

from PIL import Image
import os
import re
from ascii_dotter import AsciiDotter
import tkinter as tk

class AsciiDotterGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.thresh = tk.DoubleVar()
        self.athresh = tk.DoubleVar()
        self.thresh.set(0.5)
        self.athresh.set(1.0)

        self.create_widgets()

    def create_widgets(self):
        print("==Creating widgets==")

        self.exit = tk.Button(self, text="EXIT", fg="red", command=self.master.destroy)
        self.exit.pack(side='bottom')

        self.b_choose = tk.Button(self, text="Choose Image",command=self.choose_image)
        self.b_choose.pack()

        self.thresh_slider = tk.Scale(self, from_=0.0, to=1.0, resolution=0.01, orient = tk.HORIZONTAL, label = "Value Threshold", variable=self.thresh)
        self.thresh_slider.pack()

        self.athresh_slider = tk.Scale(self, from_=0.0, to=1.0, resolution=0.01, orient = tk.HORIZONTAL, label = "Alpha Threshold", variable=self.athresh)
        self.athresh_slider.pack()

        self.b_process = tk.Button(self, text="Process", command=self.process)
        self.b_process.pack()

    def choose_image(self):
        print("Hello world!")

    def process(self):
        print("Hello world!")

def main():
    print("==Running ascii-dotter-gui==")
    root = tk.Tk()
    app = AsciiDotterGUI(master=root)
    app.mainloop()

if __name__=="__main__":
    main()
