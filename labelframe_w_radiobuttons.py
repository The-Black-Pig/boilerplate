#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk


def showcountry():
    print("You chose", ctry1.get())


mycolor = "#d9d9d9"

root = Tk()
root.geometry("590x400+0+0")
root.resizable(True, True)
root.configure(bg=mycolor)
root.title("Radiobutton Boilerplate")

s = ttk.Style()
s.theme_use("alt")

l_frame = ttk.LabelFrame(root, text="Choose Country")
l_frame.grid(row=0, column=0, padx=20, pady=20)

ctry1 = StringVar()
r_btn1 = ttk.Radiobutton(l_frame, text="France", variable=ctry1, value="France", command=showcountry)
r_btn1.grid(row=0, column=0, sticky=W, padx=5, pady=5)

r_btn2 = ttk.Radiobutton(l_frame, text="Germany", variable=ctry1, value="Germany", command=showcountry)
r_btn2.grid(row=1, column=0, sticky=W, padx=5, pady=5)

r_btn3 = ttk.Radiobutton(l_frame, text="United Kingdom", variable=ctry1, value="United Kingdom", command=showcountry)
r_btn3.grid(row=2, column=0, sticky=W, padx=5, pady=5)

r_btn4 = ttk.Radiobutton(l_frame, text="United States", variable=ctry1, value="United States", command=showcountry)
r_btn4.grid(row=3, column=0, sticky=W, padx=5, pady=5)

root.mainloop()
