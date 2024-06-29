import os
import sys
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
from ctypes import windll

w = Tk()
w.title("That's Rea Sanka!")
w.attributes("-alpha",0.0)
w.maxsize(0,0)
w.lift()
w.iconbitmap(sys.executable)

# First, check accessbility
if tkinter.messagebox.askokcancel(
"Enterprise (Azur Lane) ask",
"Use mouse, touchpad, and/or touchscreen?\nHint: Check first. If broken or no have it, press ESC or Alt+F4 to use keyboard"):
    tkinter.messagebox.showinfo(
    "Alright, Furuya",
    "Use On Screen Keyboard if keybord broken or no have")
    w.destroy()
    import PETaskbar
else:
    tkinter.messagebox.showinfo(
    "That's okay, Furuya",
    "It will use basic windowed than overrided window")
    w.destroy()
    import PEWindow