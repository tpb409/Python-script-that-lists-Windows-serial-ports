
# python 3.7.0
# Program that displays available PC COM Ports
# Using tkinter for a GUI
#
# Started Aug 24, 2018
# Uploaded to GIT Sept 17,2018
#
#

from tkinter import *
from tkinter import ttk
import serial
import serial.tools.list_ports

# -----
# -----Create main window - Called: window ----------------------
window = Tk()
window.minsize(450, 200)
window.maxsize(700, 500)
window.geometry("500x300+600+300")  # Size and Location of the window called window
window.title("Port-ID")
window.iconbitmap("life.ico")

# ----- End main window - window -------------------------------------------------------
# -----

def blink_green():
    window.label_text_output = Label(window, relief = RAISED, bg='green', text="  ")  # <----- Display Ports ----
    window.label_text_output.place(x=150, y=102)

def blink_red():
    window.label_text_output = Label(window, relief = RAISED, bg='red', text="  ")  # <----- Display Ports ----
    window.label_text_output.place(x=150, y=102)
# ----- Method - Exit app- Exit button ---------------------------------------------------------
def button_quit_event():
    quit(33)  # <----- Quit and return 33 -------------------


# ----- Mehtod = Show COM ports - Refresh button -------------------
#
def port_id():
    comlist = serial.tools.list_ports.comports()
    ports = []
    for element in comlist:
        ports.append(element.device)
    ports = str(ports)

# ----- Create a frame to enclose the ports label
#

    frame = ttk.Frame(window)
    frame['width'] = 200
    frame['height'] = 50
    frame['borderwidth'] = 2
    frame['relief'] = 'sunken'
    frame.place(x=175, y=80)

# ----- Create a label which displays the ports  

    window.label_text_output = ttk.Label(window,text= ports)    # <----- Display Ports ----
    window.label_text_output.place(x=180, y=100)

# ----- Red Green blinking indicator when the app is refreshing

    blink_red()
    window.after(500, blink_red)
    blink_green()

    window.after(1000, port_id)     # <----- Loop after 2 seconds -----------------

# ----- Create button - Refresh ---------------------------------------
#
button_info = ttk.Button(window,text="Refreash", command=port_id)
button_info.place(x=50, y=100)

# - Create a menubar -------------------------------------------------
# ----- Create a toplevel menu ----------------------------------
menubar = Menu(window)
menubar.add_command(label="Exit", command= button_quit_event)
menubar.add_command(label="Refresh", command= port_id)
window.config(menu=menubar)     # <----- Display the menu ------------

port_id()            # <----- Show ports when app starts ------------

mainloop()






