import pyglet,tkinter
pyglet.font.add_file('./dotbold.ttf')

root = tkinter.Tk()
MyLabel = tkinter.Label(root,text="test",font=('dotbold',25))
root.title("tTracker")
root.geometry("400x300+300+120")
MyLabel.pack()
root.mainloop()