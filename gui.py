from tkinter import *

root = Tk()
root.title('Calculator')
e = Entry(root, width=35)
e.grid(row=0, column=0, columnspan=3,padx=10, pady=0)
#e.pack()
e.insert(0, '')

def btn_add():
	return None
	
def clear():
	return None
	
def num_eval():
	return None

# Buttons 

btn_1 = Button(root, text='1',  command=btn_add)

btn_2 = Button(root, text='2',  command=btn_add)

btn_3 = Button(root, text='3',  command=btn_add)

btn_4 = Button(root, text='4',  command=btn_add)

btn_5 = Button(root, text='5',  command=btn_add)

btn_6 = Button(root, text='6',  command=btn_add)

btn_7 = Button(root, text='7',  command=btn_add)

btn_8 = Button(root, text='8',  command=btn_add)

btn_9 = Button(root, text='9', command=btn_add)

btn_0 = Button(root, text='0',  command=btn_add)

btn_plus = Button(root, text='+',  command=btn_add)

btn_minus = Button(root, text='-',  command=btn_add)

btn_multi = Button(root, text='×',  command=btn_add)

btn_div = Button(root, text='÷', command=btn_add)

btn_clear = Button(root, text='AC',  command=clear)

btn_eval = Button(root, text='=',  command=num_eval)

# grids

btn_1.grid(row=0, column=0)
btn_2.grid(row=0, column=1)
btn_3.grid(row=0, column=2)


btn_4.grid(row=1, column=0)
btn_5.grid(row=1, column=1)
btn_6.grid(row=1, column=2)


btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)


btn_plus.grid(row=3, column=0)
btn_minus.grid(row=3, column=1)
btn_multi.grid(row=3, column=2)


btn_div.grid(row=4, column=0)
btn_clear.grid(row=4, column=1)
btn_eval.grid(row=4, column=2)

root.mainloop()