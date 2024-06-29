import os
import sys
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
from ctypes import windll
import aboutPEStart as PEA

# Begin Taskbar PE for start
taskbar = Tk()
taskbar.overrideredirect(1)
taskbar.iconbitmap(sys.executable)
taskbar.title("PE Startup Taskbar")
taskbar.minsize(taskbar.winfo_screenwidth(), 0)
taskbar.maxsize(taskbar.winfo_screenwidth(), 42)
taskbar.resizable(False, False)
taskbar.geometry("+0+0")

# Power function
def wpeutilShutdown():
    os.system("wpeutil Shutdown")
# Definitive function
def executeStart(str_EXECMD):
    os.system(f"start {str_EXECMD}")
def powerShStart():
    os.system("powershell")

# Button
img_button1 = PhotoImage(file="icon\\exit_24.png")
button1 = Button(image=img_button1, command=taskbar.destroy)
button1.grid(column=0, row=0, padx=3)

img_button2 = PhotoImage(file="icon\\shutdown_24.png")
button2 = Button(image=img_button2, command=lambda: wpeutilShutdown())
button2.grid(column=1, row=0, padx=3)

img_button3 = PhotoImage(file="icon\\archive_24.png")
button3 = Button(image=img_button3, command=lambda: executeStart("%WINDIR%\\APP\\7-Zip\\7zFM.exe"))
button3.grid(column=2, row=0, padx=3)

img_button4 = PhotoImage(file="icon\\conhost_24.png")
button4 = Button(image=img_button4, command=lambda: executeStart("\"Windows Preinstalled Environment\""))
button4.grid(column=3, row=0, padx=3)

img_button5 = PhotoImage(file="icon\\pwshell_24.png")
button5 = Button(image=img_button5, command=lambda: powerShStart())
button5.grid(column=4, row=0, padx=3)

img_button6 = PhotoImage(file="icon\\setup_24.png")
button6 = Button(image=img_button6, command=lambda: executeStart("%WINDIR%\\APP\\WinNTSetup\\WinNTSetup_x64.exe"))
button6.grid(column=5, row=0, padx=3)

img_button10 = PhotoImage(file="icon\\info_24.png")
button10 = Button(image=img_button10, command=PEA.aboutPEStart)
button10.grid(column=9, row=0, padx=3)

# img_button10 = PhotoImage(file="icon\\info_24.png")
# button10 = Button(text="About", image=img_button10, compound=LEFT, command=PEA.aboutPEStart, width=5)
# button10.grid(column=9, row=0)


taskbar.mainloop()
