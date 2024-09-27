# main.py

import tkinter as tk
from moduals.tkinter_app import ConversionApp

if __name__ == "__main__":
    root = tk.Tk()
    app = ConversionApp(root)
    root.mainloop()