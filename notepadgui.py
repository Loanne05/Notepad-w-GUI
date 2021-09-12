from tkinter.filedialog import *
from tkinter import *
import tkinter as tk

def saveFile():
    new_file = asksaveasfile(mode='w', filetype=[('text files', '.txt')])
    if new_file is None:
        return
    text = str(entry.get(1.0, END)) # 1.0 take all characters from beginning to the end
    new_file.write(text)
    new_file.close()

def openFile():
    #global content
    file = askopenfile(mode='r', filetype=[('text files', '*.txt')])
    entry.delete(1.0, END)
    if file is not NONE:
        content = file.read()
    entry.insert(INSERT, content)

def clearFile():
    entry.delete(1.0, END)

canvas = Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg="white")

top = Frame(canvas)
top.pack(padx=10, pady=5, anchor='nw') #north-west

b1 = Button(canvas, text="Open", bg="white", command=openFile) #.grid(row=0, sticky=E, padx=0)
b1.pack(in_=top, side=LEFT)

b2 = Button(canvas, text="Save", bg="white", command=saveFile) #.grid(row=0, sticky=E, padx=0)
b2.pack(in_=top, side=LEFT)

b3 = Button(canvas, text="Clear", bg="white", command=clearFile) #.grid(row=0, sticky=E, padx=0)
b3.pack(in_=top, side=LEFT)

b4 = Button(canvas, text="Exit", bg="white", command=exit) #.grid(row=0, sticky=E, padx=0)
b4.pack(in_=top, side=LEFT)

# Entry
entry = Text(canvas, wrap=WORD, bg="#FCF3E4", font=("poppins", 15))
entry.pack(padx=10, pady=5, expand=TRUE, fill=BOTH)

canvas.mainloop()


