from tkinter import *
import random
root = Tk()
bg = "black"
root.config(background=bg)

num1, num2, color, color_name = 0, 0, "", ""

#button function
def check():
	global num1, num2, color, color_name
	guess = entry_box.get()
	if guess == color:
		incorrect_label["text"] = ""
		correct_label["text"] = f"""Correct, the colour was
{color}"""
		
	else:
		correct_label["text"] = ""
		incorrect_label["text"] = f"""Incorrect, the color was
{color}"""
	
	num1 = random.randint(1, 21)
	color = colors[num1]
	num2 = random.randint(1, 21)
	color_name = colors[num2]
	color_label["text"] = color_name
	color_label["fg"] = color
	

#declaring the color dictionary
colors = {
0 : "red",
1 : "yellow",
2 : "blue",
3 : "orange",
4 : "magenta",
5 : "violet",
6 : "green",
7 : "cyan",
8 : "brown",
9 : "silver",
10 : "grey",
11 : "pink",
12: "lime",
13 : "indigo",
14 : "white",
15 : "turquoise",
16 : "crimson",
17 : "coral",
18 : "orchid",
19 : "azure",
20 : "teal",
21 : "chocolate"
}

#creating the layout
c = Label(root, text="C", bg=bg, fg="cyan", font=("Comic Sans MS", 32)).place(relx=0.14, rely=0.2, anchor=CENTER)
o = Label(root, text="O", bg=bg, fg="lime", font=("Comic Sans MS", 32)).place(relx=0.26, rely=0.2, anchor=CENTER)
l = Label(root, text="L", bg=bg, fg="pink", font=("Comic Sans MS", 32)).place(relx=0.38, rely=0.2, anchor=CENTER)
o = Label(root, text="O", bg=bg, fg="red", font=("Comic Sans MS", 32)).place(relx=0.5, rely=0.2, anchor=CENTER)
u = Label(root, text="U", bg=bg, fg="orange", font=("Comic Sans MS", 32)).place(relx=0.62, rely=0.2, anchor=CENTER)
r = Label(root, text="R", bg=bg, fg="yellow", font=("Comic Sans MS", 32)).place(relx=0.74, rely=0.2, anchor=CENTER)
s = Label(root, text="S", bg=bg, fg="magenta", font=("Comic Sans MS", 32)).place(relx=0.86, rely=0.2, anchor=CENTER)

name = Label(root, text="Name", bg=bg, fg="red", font=("Comic Sans MS", 14)).place(relx=0.3, rely=0.3, anchor=CENTER)
the = Label(root, text="The", bg=bg, fg="green", font=("Comic Sans MS", 14)).place(relx=0.48, rely=0.3, anchor=CENTER)
colour = Label(root, text="Colour", bg=bg, fg="blue", font=("Comic Sans MS", 14)).place(relx=0.67, rely=0.3, anchor=CENTER)

entry_box = Entry(root)
entry_box.place(relx=0.5, rely=0.7, anchor=CENTER)

submit_button = Button(root, text="Submit", bg="cyan", fg="magenta", activebackground="yellow", command=check)
submit_button.place(relx=0.5, rely=0.75, anchor=CENTER)

color_label = Label(root, text="", bg=bg, font=("Comic Sans MS", 30))
color_label.place(relx=0.5, rely=0.5, anchor=CENTER)

correct_label = Label(root, text="", bg=bg, fg="lime", font=("Comic Sans MS", 12))
correct_label.place(relx=0.5, rely=0.37, anchor=CENTER)

incorrect_label = Label(root, text="", bg=bg, fg="red", font=("Comic Sans MS", 12))
incorrect_label.place(relx=0.5, rely=0.37, anchor=CENTER)

#implementing the logic
def main():
	global num1, num2, color, color_name
	num1 = random.randint(1, 21)
	color = colors[num1]
	num2 = random.randint(1, 21)
	color_name = colors[num2]
	color_label["text"] = color_name
	color_label["fg"] = color

main()

root.mainloop()
