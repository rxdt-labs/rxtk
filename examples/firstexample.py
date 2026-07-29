# Modified from https://tkdocs.com/tutorial/firstexample.html

import rxtk
from tkinter import ttk
import tkinter as tk
import pypagate as pg

root = tk.Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

feet_entry = rxtk.Entry(mainframe, width=7, text="0")
feet_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

handle_empty = {'' : float("inf")}
handle_inf = {float("inf") : 0}
meters = pg.as_str(pg.as_int(0.3048 * pg.as_float(feet_entry.value, handle_empty), handle_inf))
rxtk.Label(mainframe, text=meters).grid(column=2, row=2, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=tk.W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=tk.E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=tk.W)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()

root.mainloop()
