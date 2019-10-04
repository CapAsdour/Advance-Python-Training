from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
def newfile():
    global file
    master.title("Untitled - Notepad")
    file = None
    textarea.delete(1.0, END)
def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        master.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()
def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None
        else:
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()
            master.title(os.path.basename(file) + " - Notepad")
    else:
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()
def quitApp():
    master.destroy()
def cut():
    textarea.event_generate(("<<Cut>>"))
def copy():
    textarea.event_generate(("<<Copy>>"))
def paste():
    textarea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad", "Notepad by Satish Kumar Singh and Vishwajeet Kumar singh")
master=Tk()
master.title('Untitled - Notepad')
master.geometry('680x720')
master.wm_iconbitmap("")
textarea=Text(master, font='lucida 13')
file=None
textarea.pack(expand=True, fill=BOTH)
scroll=Scrollbar(textarea)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=scroll.set)
menu=Menu(master)
master.config(menu=menu)
filemenu=Menu(menu,tearoff=0)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New', command=newfile)
filemenu.add_command(label='Open', command=openfile)
filemenu.add_command(label='Save', command=savefile)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=quitApp)
editmenu=Menu(menu, tearoff=0)
menu.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Copy', command=copy)
editmenu.add_command(label='Cut', command=cut)
editmenu.add_command(label='Paste', command=paste)
helpmenu=Menu(menu, tearoff=0)
menu.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About Notepad', command=about)
master.mainloop()