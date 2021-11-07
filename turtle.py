from turtle import  *
import random


#virus
'''
turtle.speed(250)
turtle.color('white')
turtle.bgcolor('black')

i = 200
while i > 0:
	turtle.left(i)
	turtle.forward(i*3)
	i = i - 1
	
turtle.done()



import  math
import  io
import  cv2
import  urllib.request
import tkinter.font as font
from tkinter import  *
from tkinter import  filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("Text Editor-Untiltled")
root.geometry("300x250+300+300")
root.minsize(width=400, height=400)
root.configure(background="#102538")
heading_font = font.Font(family='Helvetica', size=12, weight='bold')
edit_font = font.Font(family='Tahoma', size=9, weight='bold',underline=10)
default_img= ImageTk.PhotoImage(Image.open("default.jpg"))
src = "default.jpg"
default_src = "https://as1.ftcdn.net/v2/jpg/03/76/74/78/1000_F_376747823_L8il80K6c2CM1lnPYJhhJZQNl6ynX1yj.jpg"
image_opener = urllib.request.URLopener()
image_opener.retrieve(default_src, src)

def dumb():
	pass

def open_image():
	root.filename = filedialog.askopenfilename(title="select", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
	Label(root, text=root.filename).pack()
	image = ImageTk.PhotoImage(Image.open(root.filename))
	src = root.filename
	Label(image=image).pack()
	
	
main_menu = Menu(root)
file = Menu(main_menu)
edit = Menu(main_menu)
tools = Menu(main_menu)
formats = Menu(main_menu)

file.add_command(label='new', command=dumb)
file.add_command(label='open', command=open_image)
file.add_command(label='save as', command=dumb)
file.add_command(label='rename', command=dumb)
main_menu.add_cascade(label='file', menu=file)

heading = Label(root, text="Photo editor", fg="#FFF", bg="#242526", padx=10, pady=10, width=20,font=heading_font, borderwidth=1,height=2, relief=SUNKEN)

image_frame = Frame(root, width=50)
image_field = Label(image=default_img)

edit_frame = Frame(root, relief=SUNKEN,width=50,bg='#242526',borderwidth=1,height=10)
brightness = Scale(edit_frame, from_=0, to=100, orient=HORIZONTAL)
saturation = Scale(edit_frame,from_=0, to=100, orient=HORIZONTAL)
contrast = Scale(edit_frame,from_=0, to=100, orient=HORIZONTAL)
blur = Scale(edit_frame, from_=0, to=100, orient=HORIZONTAL)
warmness = Scale(edit_frame,from_=0, to=100, orient=HORIZONTAL)
sepia = Scale(edit_frame,from_=0, to=100, orient=HORIZONTAL)

brightness_label = Label(edit_frame, font=edit_font,text="Brightness")
saturation_label = Label(edit_frame, font=edit_font, text="Saturation")
contrast_label = Label(edit_frame, font=edit_font, text="Contrast")
blur_label = Label(edit_frame, font=edit_font, text="blur")
warmness_label = Label(edit_frame, font=edit_font, text="Warmness")
sepia_label = Label(edit_frame, font=edit_font, text="Sepia")

root.config(menu=main_menu)
heading.pack(expand=True)
image_frame.pack(expand=True, fill=X)
image_field.pack()
edit_frame.pack(expand=True, fill=X)
edit_frame.grid_rowconfigure(0, weight=1)
edit_frame.grid_columnconfigure(0, weight=1)
brightness_label.pack(expand=True, fill=X)
brightness.pack(expand=True, fill=X)
contrast_label.pack(expand=True, fill=X)
contrast.pack(expand=True, fill=X)
saturation_label.pack(expand=True, fill=X)
saturation.pack(expand=True, fill=X)
blur_label.pack(expand=True, fill=X)
blur.pack(expand=True, fill=X)
warmness_label.pack(expand=True, fill=X)
warmness.pack(expand=True, fill=X)
sepia_label.pack(expand=True, fill=X)
sepia.pack(expand=True, fill=X)

root.mainloop()
'''
# triangle
screen = turtle.Screen()
screen.bgcolor('white')
t = turtle.Turtle()
t.speed(0)

colors = ["firebrick", "dark cyan"]

for i in range(150):
	t.color(random.choice(colors))
	t.forward(i*5)
	t.left(120)
	
t.up()
t.goto(-120,200)
t.down()
t.hideturtle()
turtle.done()
