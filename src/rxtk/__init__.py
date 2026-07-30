try:
    import ttkbootstrap as ttk
except ModuleNotFoundError:
    from tkinter import ttk
import tkinter as tk
import pypagate as pg


def _register_kwargs(obj, **kwargs):
    """Take kwargs for a UI element (like Button) and do two things:
    1. Make on_change for each term update the object.
    2. Return a de-expression-ified kwargs to pass later to 
       super().__init__(...)
    """
    options = {}
    for key, val in kwargs.items():
        if isinstance(val, pg.Term) or isinstance(val, pg.Formula):
            @pg.on_change(val)
            def f(old, new):
                obj.config(**{key : new})
            options[key] = val.unwrap()
        else:
            options[key] = val
    return options
    

class Button(ttk.Button):
    def __init__(self, *args, **kwargs):
        options = _register_kwargs(self, **kwargs)
        super().__init__(*args, **options)

class Checkbutton(ttk.Checkbutton):
    def __init__(self, *args, **kwargs):
        options = _register_kwargs(self, **kwargs)
        super().__init__(*args, **options)

class Entry(ttk.Entry):
    def __on_change(self, event):
        self.value.change(event.widget.get())

    def __init__(self, *args, **kwargs):
        options = _register_kwargs(self, **kwargs)
        super().__init__(*args, **options)
        self.value = pg.Term(self.get())
        self.bind("<KeyRelease>", self.__on_change)


class Radiobutton(ttk.Radiobutton):
    def __init__(self, *args, **kwargs):
        options = _register_kwargs(self, **kwargs)
        super().__init__(*args, **options)

class Scale(ttk.Scale):
    def __init__(self, *args, **kwargs):
        options = _register_kwargs(self, **kwargs)
        super().__init__(*args, **options)

class Scrollbar(ttk.Scrollbar):
    def __init__(self, *args, **kwargs):
        options = _register_kwargs(self, **kwargs)
        super().__init__(*args, **options)

class Spinbox(ttk.Spinbox):
    def __init__(self, *args, **kwargs):
        options = _register_kwargs(self, **kwargs)
        super().__init__(*args, **options)

class Text(tk.Text):
    def __init__(self, *args, **kwargs):
        options = _register_kwargs(self, **kwargs)
        super().__init__(*args, **options)

class Label(ttk.Label):
    def __init__(self, *args, **kwargs):
        options = _register_kwargs(self, **kwargs)
        super().__init__(*args, **options)

class Comboxbox(ttk.Combobox):
    def __init__(self, *args, **kwargs):
        options = _register_kwargs(self, **kwargs)
        super().__init__(*args, **options)

class Notebook(ttk.Notebook):
    def __init__(self, *args, **kwargs):
        options = _register_kwargs(self, **kwargs)
        super().__init__(*args, **options)

class Progressbar(ttk.Progressbar):
    def __init__(self, *args, **kwargs):
        options = _register_kwargs(self, **kwargs)
        super().__init__(*args, **options)
