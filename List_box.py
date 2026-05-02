from tkinter import *

screen=Tk()
screen.geometry("300x400")
# Listbox 
food=Label(screen,text="Food items")
food.pack()

Listbox1=Listbox(screen,height=10,width=10,bg="skyblue",fg="black",activestyle="dotbox")
Listbox1.pack()
Listbox1.insert(1,"Bread")
Listbox1.insert(2,"Pasta")
Listbox1.insert(3,"Pizza")
Listbox1.insert(4,"Banana")
Listbox1.insert(5,"Carrot")

# Spinbox
sb=Spinbox(screen,from_=0, to=10)
sb.pack()

screen.mainloop()