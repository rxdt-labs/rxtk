# rxtk

Reactive bindings to Python `tkinter` module. (WIP)

# Quickstart

(NOTE: Not yet on PyPI so this does not work quite yet!)

Install with [pip](https://pypi.org/project/pip/):

```bash
pip install rxtk
# Or with ttkbootstrap themes:
pip install rxtk[bootstrap]
```

Install with [uv](https://docs.astral.sh/uv/)

```bash
uv add rxtk
# Or with ttkbootstrap themes:
uv add rxtk[bootstrap]
```

# What is it?

rxtk is a thin wrapper over [tkinter](https://docs.python.org/3/library/tkinter.html) (and optionally [ttkbootstrap](https://ttkbootstrap.readthedocs.io/en/latest/) so using the reactive [pypagate](https://github.com/rxdt-labs/pypagate) is easier than ever before. Consider this feet-to-meeters application from [tkdocs.com](https://tkdocs.com/tutorial/firstexample.html):

```py
from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(round(0.3048 * value, 4))
    except ValueError:
        pass

root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
```

It would be much nicer if there was no need to press the button to calculate the meters and just have it automatically update no? Furthermore, it would be nice not to worry about recalculation of anything. Everything just auto-updated based on the input. That's where rxtk and pypagate come into play:

```py
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
```

What happened? No button, `meters` is a formula that autochanges (and *so does the `Label` using `meters`). Everything just works!

# Documentation

(Coming soon)
