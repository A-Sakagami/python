from tkinter import *
from tkinter import ttk
import calc

FORMS = Tk()
FORMS.title = "四則演算デモ"

mainframe = ttk.Frame(FORMS, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
FORMS.columnconfigure(0, weight=1)
FORMS.rowconfigure(0, weight=1)



