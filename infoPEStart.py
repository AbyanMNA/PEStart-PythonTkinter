import os
import sys
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
from ctypes import windll

def messageInfoBoxPE():
    tkinter.messagebox.showinfo("Info PE Start Launcher", """Windows PE is uncomplete rescue kit Windows-based. Some mistake about Windows PE. Windows PE original build with WinAIK or WinADK. Can build with \"builder\" under WinRE.WIM but problem in bluescreen, *DIED.""")
    return messageWarnBoxPE()
def messageWarnBoxPE():
    tkinter.messagebox.showwarning("Info PE Start Launcher", "Maximum usage is 72 hours, that's hard or not yet to configure")