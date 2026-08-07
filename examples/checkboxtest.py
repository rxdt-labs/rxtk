# Modified from https://tkdocs.com/tutorial/firstexample.html

import rxtk
from tkinter import ttk
import tkinter as tk
import pypagate as pg

root = tk.Tk()
root.title("Checkbox Test")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

check_btn = rxtk.Checkbutton(mainframe, width=7, text="Check Me")
check_btn.grid(column=2, row=1, sticky=(tk.W, tk.E))

rxtk.Label(mainframe, text=pg.as_str(check_btn.value)).grid(column=2, row=2, sticky=(tk.W, tk.E))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()
