from tkinter import Tk, Label, PhotoImage, LEFT, RIGHT, SUNKEN
root = Tk()

xandrix =PhotoImage(file="xandrix300x300.gif")
xandrixLabel=Label(root, image=xandrix, borderwidth=3, relief=SUNKEN)
xandrixLabel.pack(side=LEFT)

text =Label(root, font=('bold italic', 20), text="Xandrix Jill Paguntalan \n Davao City, January 2003")
text.pack(side=RIGHT)
root.mainloop()