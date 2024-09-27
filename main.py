# main.py

import tkinter as tk
from moduals.tkinter_app import ConversionApp

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="lavender")
    root.attributes('-topmost',True) # turn this into a checkbox later
    app = ConversionApp(root)
    root.mainloop()