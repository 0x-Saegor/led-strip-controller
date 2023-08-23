# Led Strip Remote Controller Linux

Home Assistant integration for LED STRIP NAME ELK BLEDOM with android/iphone [mobile app duoCo Strip](https://play.google.com/store/apps/details?id=shy.smartled&hl=es&gl=US) or [mobile app Lantern Lotus](https://play.google.com/store/apps/details?id=wl.smartled&hl=es&gl=US).

This script has been created using [this github page](https://github.com/dave-code-ruiz/elkbledom#elkbledom-ha-integration) and [this webpage](https://linuxthings.co.uk/blog/control-an-elk-bledom-bluetooth-led-strip), it can remotely control any ELK-BLEDOM duoCo Bluetooth LED strip.
For more details on how it works visit these pages.

## Setup

Install customtkinter from `pip3 install customtkinter` in your terminal.
You may also need tkinter : `pip3 install tkinter`.

## Get the bluetooth adress

To be able to talk to the LED strip I first needed to find its Bluetooth address, that can be done using `sudo hcitool lescan` which will keep on displaying the addresses of any device which is ready for a connection. In my case, the address is BE:FF:F0:30:07:EC. CTRL-C will stop the lescan.

![image](https://github.com/Arthurdufinister/led-strip-controller/assets/95881999/731b6406-e2a4-44da-af63-6cba96d2511e)

## Add it to the code

Edit the `bluetooth_adress = "XX:XX:XX:XX:XX:XX"` line and set it up with yours.

![image](https://github.com/Arthurdufinister/led-strip-controller/assets/95881999/2a390204-20d2-4873-b2b1-ce6459319b41)

## Start

Go into the directory where the python file is located and open a terminal.
Type `python3 led_remote.py`



You can customize the style of the window being opened from editing lines 6 and 9.


```
# Supported modes : Light, Dark, System
set_appearance_mode("System")
 
# Supported themes : green, dark-blue, blue
set_default_color_theme("green")  ```
