from tkinter import *


root=Tk()
root.geometry('700x700+400+400')
root.title('Rishabh Arts Admin Panel')
img_label = tk.Label(root)
img_label.img = tk.PhotoImage(file='Logo.png')
img_label.config(image=img_label.img)
img_label.pack()
welcom=Label(root,text="Quiz Database").pack()






root.mainloop()
