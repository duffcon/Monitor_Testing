import tkinter
from tkinter import Button, Label, Checkbutton, IntVar, StringVar, Radiobutton, Entry, W, LEFT, OptionMenu
from tkinter.ttk import Combobox
import datetime
from subprocess import Popen, PIPE
import re
import math
import os.path
import sys



font = ("Courier", 10)
width = 10
sticky = W

hw_info_pattern = dict ({
    "Vendor": dict({ "Pattern": 'Vendor: (\w+)"*.*"*' , "Group": 1  }), 
    "Model": dict({ "Pattern": 'Model: "(.*)"', "Group": 1  }),
    "Serial": dict({ "Pattern": 'Serial ID: "(.*)"', "Group": 1  }),
    "Year": dict({ "Pattern": 'Year of Manufacture: (\d+)', "Group": 1  }),
    "HorizontalRes": dict({ "Pattern": 'Max. Resolution: (\d+)x(\d+)' , "Group": 1  }),
    "VerticalRes": dict({ "Pattern": 'Max. Resolution: (\d+)x(\d+)' , "Group": 2  }),
    "RefreshRate": dict({ "Pattern": '(?s:.*)Resolution: .*@(\d+)Hz' , "Group": 1  }),
    "Length": dict({ "Pattern":'Size: (\d+)x(\d+).*', "Group": 1  }),
    "Width": dict({ "Pattern":'Size: (\d+)x(\d+).*', "Group": 2 })
        })
ext_info_keys = ["Size", "Ports", "Date", "Type", "Price"]

info_keys = list() + list(hw_info_pattern.keys()) + ext_info_keys
port_keys = ["DP", "HDMI", "DVI", "VGA", "USB", "Ethernet", "AV", "Component", "S-Video"]
type_keys = ["LCD", "LED", "CRT", "TV"]
discount_keys = ["No Stand", "Scratch", "Spot"]

info_data = dict()
port_data = dict()
discount_data = dict()
monitor_data = list()

def portChange():
    pass

def monitorChange(monitor):
    pass

def addDiscount():
    pass

def exitProgram():
    pass

def restartProgram():
    pass

def printLast():
    pass

def startPrint():
    pass

def getInfo():
    pass





window = tkinter.Tk()


Button(window, font = font, text = "Extract", width=width, command=getInfo).grid(row=1, column=1, sticky = sticky)
Button(window, font = font, text = "Print Save", width=width, command=startPrint).grid(row=3, column=1, sticky = sticky)
Button(window, font = font, text = "Print Last", width=width, command=printLast).grid(row=4, column=1, sticky = sticky)
Button(window, font = font, text = "Restart", width=width, command=restartProgram).grid(row=6, column=1, sticky = sticky)
Button(window, font = font, text = "Exit", width=width, command=exitProgram).grid(row=7, column=1, sticky = sticky)


monitor_select = OptionMenu(window, StringVar(value = "SELECT"), "", command=monitorChange)
monitor_select.grid(row=1, column=2, sticky = W)

for i in range(0, len(info_keys)):
    info_data[info_keys[i]] = StringVar()
    Entry(window, font = font, textvariable = info_data[info_keys[i]]).grid(row=i+2, column=2, sticky = W)

for i in range(0, len(port_keys)):
    port_data[port_keys[i]] = IntVar()
    Checkbutton(window, font = font, text = port_keys[i], variable = port_data[port_keys[i]], command=portChange).grid(row=i, column=3, sticky = W)

for i in range(0, len(type_keys)):
    Radiobutton(window, font = font, text = type_keys[i], variable = info_data["Type"], value = type_keys[i]).grid(row=i, column=4, sticky = W)

for i in range(0, len(discount_keys)):
    discount_data[discount_keys[i]] = IntVar()
    Checkbutton(window, font = font, text = discount_keys[i], command=addDiscount).grid(row=i, column=5, sticky = W)


getInfo()

window.mainloop()