from Tkinter import *
root = Tk()
V = StringVar()
S = Scrollbar(root)
lb = Listbox(root,yscrollcommand = S.set)
for item in range(100):
	lb.insert(END,str(item*100))
V.set(('100','200'))
print (V.get())
lb.pack()
root.mainloop()