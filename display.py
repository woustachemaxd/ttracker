import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
import pyglet, os
pyglet.font.add_file('whyte.ttf')
def convert():
    mile_in = entry_int.get()
    km = mile_in * 1.609344
    output_string.set(f"{km:.2f} km")

window = ttk.Window(themename='darkly')

window.title("tTracker")
window.geometry("400x300+300+120")
# window.overrideredirect(True)

title_label = ttk.Label(master = window, text="tTracker", font = ('whyte', 24))
title_label.pack(pady=20)

input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable=entry_int, width=10)
button = ttk.Button(master = input_frame, text="Convert", command= convert)
entry.pack(side= 'left', padx = 10)
button.pack(side= 'left')
input_frame.pack(pady=20)

output_string = tk.StringVar()
output = ttk.Label(master = window, text="Output", font=('whyte', 24), textvariable=output_string)
output.pack(padx=10, pady=10)

window.mainloop()