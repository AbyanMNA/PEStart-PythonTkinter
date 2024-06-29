import os
import sys
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
from ctypes import windll
import aboutPEStart as PE
import infoPEStart as PE2

# Begin PE Start Menu for start
smWindow = Tk()
smWindow.iconbitmap(sys.executable)
smWindow.title("PE Start Menu")
smWindow_w, smWindow_h = 400, 300
smWindow_wscr, smWindow_hscr = smWindow.winfo_screenwidth(), smWindow.winfo_screenheight()
x_smW = (smWindow_wscr/2) - (smWindow_w/2)
y_smW = (smWindow_hscr/2) - (smWindow_h/2)
smWindow.geometry(
"%dx%d+%d+%d" %(smWindow_w, smWindow_h, x_smW, y_smW)
)
smWindow.maxsize(400, 300)
smWindow.resizable(False, False)

# Power function
def wpeutilPower(chosePower):
    os.system(f"wpeutil {chosePower}")
# Definitive function
def executeStart(str_EXECMD):
    os.system(f"start {str_EXECMD}")

# Button Image
img_button1 = PhotoImage(file="icon\\exit_24.png")
img_button2 = PhotoImage(file="icon\\shutdown_24.png")
img_button3 = PhotoImage(file="icon\\archive_24.png")
img_button4 = PhotoImage(file="icon\\conhost_24.png")
img_button5 = PhotoImage(file="icon\\pwshell_24.png")
img_button6 = PhotoImage(file="icon\\setup_24.png")
img_button7 = PhotoImage(file="icon\\diskset_24.png")
img_button10 = PhotoImage(file="icon\\info_24.png")

# Button and label
labelHead1 = Label(smWindow, anchor="w", width=400, justify=LEFT, text="Power")
labelHead1.grid(column=0, row=0, padx=2, columnspan=400)
button1 = Button(
    text="Exit & Restart",
    image=img_button1,
    compound=LEFT,
    command=smWindow.destroy)
button1.grid(column=0, row=1, padx=2)
button1 = Button(
    text="Shutdown",
    image=img_button2,
    compound=LEFT,
    command=lambda: wpeutilPower("shutdown"))
button1.grid(column=1, row=1, padx=2)

labelHead1 = Label(smWindow, anchor="w", width=400, justify=LEFT, text="Terminal")
labelHead1.grid(column=0, row=2, padx=2, columnspan=400)
button1 = Button(
    text="CMD",
    image=img_button4,
    compound=LEFT,
    command=lambda: executeStart("cmd.exe"))
button1.grid(column=0, row=3, padx=2)
button1 = Button(
    text="Powershell",
    image=img_button5,
    compound=LEFT,
    command=lambda: executeStart("powershell.exe"))
button1.grid(column=1, row=3, padx=2)

labelHead1 = Label(smWindow, anchor="w", width=400, justify=LEFT, text="Utilities")
labelHead1.grid(column=0, row=4, padx=2, columnspan=400)
button1 = Button(
    text="File Manager",
    image=img_button3,
    compound=LEFT,
    command=lambda: executeStart("%WINDIR%\\APP\\7-Zip\\7zFM.exe"))
button1.grid(column=0, row=5, padx=2)
button1 = Button(
    text="DISKPART",
    image=img_button7,
    compound=LEFT,
    command=lambda: executeStart("DISKPART.exe"))
button1.grid(column=1, row=5, padx=2)
button1 = Button(
    text="NTSetup", # WinNTSetup by JFX ~ ENDGAME
    image=img_button6,
    compound=LEFT,
    command=lambda: executeStart("%WINDIR%\\APP\\WinNTSetup\\WinNTSetup_x64.exe"))
button1.grid(column=2, row=5, padx=2)

labelHead1 = Label(smWindow, anchor="w", width=400, justify=LEFT, text="Other")
labelHead1.grid(column=0, row=6, padx=2, columnspan=400)
button1 = Button(
    text="What's PE?",
    image=img_button10,
    compound=LEFT,
    command=PE2.messageInfoBoxPE)
button1.grid(column=0, row=7, padx=2)
button1 = Button(
    text="About",
    image=img_button10,
    compound=LEFT,
    command=PE.aboutPEStart)
button1.grid(column=1, row=7, padx=2)

smWindow.mainloop()
