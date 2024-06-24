from tkinter import *
from os import system
from CTkColorPicker import *
from tkinter.colorchooser import askcolor
from customtkinter import *

# Supported modes : Light, Dark, System
set_appearance_mode("System")
 
# Supported themes : green, dark-blue, blue
set_default_color_theme("green")   

bluetooth_adress = "XX:XX:XX:XX:XX:XX"

base_command = f"gatttool -i hci0 -b {bluetooth_adress} --char-write-req -a 0x0008 -n "
power_on = "7e0004f00001ff00ef"
power_off = "7e0004000000ff00ef"
set_color = "7e000503{red}{green}{blue}00ef"
set_brightness = "7e0001{brightness}00000000ef"

def add_keyboardmouseSupport(r, g, b):
    command = f"openrgb -d 0 -c {r}{g}{b} -d 1 -m Static -c {r}{g}{b}"
    system(command)

def choose_color():
    colors = askcolor(title="Tkinter Color Chooser")
    colors = colors[1].split('#')[1]
    red = colors[0:2]
    green = colors[2:4]
    blue = colors[4:6]
    new_color = set_color.format(red=red, green=green, blue=blue)
    system(base_command+ new_color)

def choose_color2():
    colors = askcolor(title="Tkinter Color Chooser")
    colors = colors[1].split('#')[1]
    red = colors[0:2]
    green = colors[2:4]
    blue = colors[4:6]
    new_color = set_color.format(red=red, green=green, blue=blue)
    system(base_command+ new_color)
    add_keyboardmouseSupport(red, green, blue)

def choose_color3():
    colors = askcolor(title="Tkinter Color Chooser")
    colors = colors[1].split('#')[1]
    red = colors[0:2]
    green = colors[2:4]
    blue = colors[4:6]
    add_keyboardmouseSupport(red, green, blue)

def change_brightness(value):
    value = int(value)
    brightness_text.configure(text="Brightness : "+str(value))
    system(base_command + set_brightness.format(brightness=value))

system("rfkill unblock bluetooth")

root = CTk()
root.title('Led Remote')
CTkButton(master=root, text="Power On", text_color="black", command=lambda: system(base_command+power_on)).pack(padx=30, pady=5)
CTkButton(master=root, text="Power Off", text_color="black", command=lambda: system(base_command+power_off)).pack(padx=30, pady=5)
CTkButton(master=root, text="Choose Color", text_color="black", command=choose_color).pack(padx=30, pady=5)

brightness_text = CTkLabel(master=root,text="Brightness : 50")
brightness_text.pack()
CTkSlider(master=root, command=change_brightness, from_=1, to=99, number_of_steps=99).pack(pady=5)


CTkButton(master=root, text="Keyboard & Mouse", text_color="black", command=choose_color3).pack(padx=30, pady=5)
CTkButton(master=root, text="All colors", text_color="black", command=choose_color2).pack(padx=30, pady=5)
system("rfkill block bluetooth")

root.mainloop()
