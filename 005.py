from tkinter import *
import math
from drawRGB import *


master = Tk()
def callback():
	col = ColorRGB(parseToInt(e1.get()), parseToInt(e2.get()), parseToInt(e3.get()))
	e1.delete(0, END)
	e1.insert(0, col.red)
	e2.delete(0, END)
	e2.insert(0, col.green)
	e3.delete(0, END)
	e3.insert(0, col.blue)
	w.delete("all")
	kubik = RGBCube(w, st, col)
	kubik2 = AHSLCube(w, st2, col.getAHSLmodel())
   # print (e1.get())
    
b = Button(master, text="OK", command=callback)
b.grid(row = 4, column = 0, columnspan = 5)

r = Label(master, text="Red",)
r.grid(row = 0, column = 0, sticky=E)

g = Label(master, text="Green")
g.grid(row = 1, column = 0, sticky=E)

bl = Label(master, text="Blue")
bl.grid(row = 2, column = 0, sticky=E)


e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=0, column=1, columnspan=1, sticky=W)
e2.grid(row=1, column=1, columnspan=1, sticky=W)
e3.grid(row=2, column=1, columnspan=1, sticky=W)


f = open('coord.crd', 'w')
w = Canvas(master, width=780, height=500)
w.grid(row = 5, column = 0, columnspan = 4)
st = Coord(30,100)
st2 = Coord(400, 140)
col = ColorRGB(92, 203, 70)
kubik = RGBCube(w, st, col)
kubik2 = AHSLCube(w, st2, col.getAHSLmodel())
mainloop()
# Place RGB cube on canvas
'''
for m in range(1, 1000):
	print (" --------------------------------")
	print (m)
	print (" --------------------------------")
	for i in range(0,255):
		w.delete('all')
		col = ColorRGB(i, i, i)
		kubik.colorToCoords(w, col)
		#print (i)
		#w.delete("all")
		#kubik.deleteAll(w)
		master.update()
	

'''
'''
kubik = RGBCube(34, w)
#w.delete("all")
mainloop()
	
'''
