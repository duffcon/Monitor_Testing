import tkinter
from tkinter import Button, Label, Checkbutton, IntVar, StringVar, Radiobutton, Entry, W, LEFT, OptionMenu
from tkinter.ttk import Combobox
import datetime
from subprocess import Popen, PIPE
import re
import math
import os.path
import sys
import webbrowser


font = ("Courier", 10)
width = 15
sticky = W

label_layout = "./layouts/layout.glabels"
barcode_layout = "./layouts/barcode.glabels"
discount_layout = "./layouts/discount.glabels"
printer_name = "LabelWriter-450"


vendor_dict = dict({"DEL": "Dell",
                    "LEN": "Lenovo",
                    "SPT": "Sceptre",
                    "HWP": "HP",
                    "ACI": "Asus",
                    "ACR": "Acer",
                    "GSM": "LG",
                    "SAM":"Samsung",
                    "VSC": "ViewSonic",
                    "AOC": "AOC"
                    })
hw_info_patterns = dict ({
    "VNDR": dict({ "Pattern": 'Vendor: (\w+)"*.*"*' , "Group": 1  }), 
    "Model": dict({ "Pattern": 'Model: "(.*)"', "Group": 1  }),
    "Serial": dict({ "Pattern": 'Serial ID: "(.*)"', "Group": 1  }),
    "Year": dict({ "Pattern": 'Year of Manufacture: (\d+)', "Group": 1  }),
    "HorizontalRes": dict({ "Pattern": 'Max. Resolution: (\d+)x(\d+)' , "Group": 1  }),
    "VerticalRes": dict({ "Pattern": 'Max. Resolution: (\d+)x(\d+)' , "Group": 2  }),
    "RefreshRate": dict({ "Pattern": '(?s:.*)Resolution: .*@(\d+)Hz' , "Group": 1  }),
    "Length": dict({ "Pattern":'Size: (\d+)x(\d+).*', "Group": 1  }),
    "Width": dict({ "Pattern":'Size: (\d+)x(\d+).*', "Group": 2 })
        })
ext_info_keys = ["Vendor", "Size", "Ports", "Date", "Type", "Price"]
info_keys = list(hw_info_patterns.keys()) + ext_info_keys
port_keys = ["DP", "HDMI", "DVI", "VGA", "USB", "Ethernet", "AV", "Component", "S-Video"]
type_keys = ["LCD", "LED", "CRT", "TV"]

info_data = dict()
port_data = dict()
discount_data = dict()
discount_data = dict()
monitor_data = list()


def getPrice():
    return 39

def sendCommand(c):
    p = Popen(c, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(b"")
    rc = p.returncode
    if p.returncode != 0:
        print(err)
        return 0
    output = str(output, 'utf-8')
    return output

def getHwInfo():
    m = sendCommand(['hwinfo', '--monitor'])
    m = m.split("\n\n")
    return m  

def getDiagonal(l, w):
    a = int(l) ** 2
    b = int(w) ** 2
    c = math.sqrt(a + b)
    # 25.4 mm = 1 in
    c = c / 25.4
    return round(c)

def getPath(m):
    return "./database/" + m["Vendor"] + "_" + m["Model"] + ".mon"
     
def getDate():
    now = datetime.datetime.now()
    s = (str(now.day) +  " " + now.strftime("%b") + " " + str(now.year))
    return s

def parseFile(path, m):
    f = open(path, "r")
    s = f.read()
    lines = s.split("\n")
    for l in lines:
        temp = l.split(",")
        if len(temp) == 2:
            m[temp[0]] = temp[1]
       

def extraHwParse(m):
    m["Type"] = type_keys[0]
    m["Ports"] = ""
    m["Size"] = getDiagonal(m["Length"], m["Width"])
    # price = getPrice(info_data["Size"].get(), info_data["Length"].get(), info_data["Width"].get(), info_data["Type"].get())
    price = getPrice()
    m["Price"] = str(price) + ".95"
    m["Date"] = getDate()

def hwInfoParse(info_string, m):
    for key in hw_info_patterns.keys():
        match = re.search(hw_info_patterns[key]["Pattern"],info_string)
        if match == None:
            continue
        m[key] = match.group(hw_info_patterns[key]["Group"])
    model = m["Model"]
    model = model.split(" ")[-1]
    m["Model"] = model
    m["Vendor"] = vendor_dict.get(m["VNDR"], '?')
    extraHwParse(m)

    path = getPath(m)
    if os.path.exists(path):
        parseFile(path, m)


def portChange():
    s = ""
    for p in port_keys:
        if port_data[p].get() == 1:
            s += p + " "
    info_data["Ports"].set(s)

def webSearch():
    url = "https://www.ebay.com/sch/i.html?_from=R40"
    url += "&_nkw=" + info_data["Vendor"].get()
    url += "+" + info_data["Model"].get()
    url += "+" + info_data["Size"].get()
    url += "+monitor"
    url += "&_LH_Sold=1&_LH_Complete=1&rt=nc&LH_Sold=1&LH_Complete=1"
    ff = webbrowser.get('firefox')
    ff.open(url, new = 0, autoraise=True)
    
def monitorChange(monitor):
    monitor = monitor.split(" ")
    for key in info_keys:
        info_data[key].set(monitor_data[int(monitor[0])][key])

    
def addDiscount():
    pass

def saveMonitor():
    path = "./database/" + info_data["Vendor"].get() + "_" + info_data["Model"].get() + ".mon"
    f = open(path, "w")
    for key in info_data.keys():
        if key in ["Date", "Price"]:
            continue
        f.write(key + "," + info_data[key].get() + "\n")
    f.close()

def saveLabelData():
    path = "./layouts/label_input.txt"
    f_out = "./labels/label.pdf"

    f = open(path, "w+")
    for key in info_data.keys():
        f.write(key + ";")
    f.write("\n")
    for key in info_data.keys():
        f.write(info_data[key].get() + ";")
    f.close()

    sendCommand(['glabels-3-batch', '-i', path, '-o', f_out, label_layout])

def saveBarcodeData():
    path = "./layouts/barcode_input.txt"
    f_out = "./labels/barcode.pdf"
    f = open(path, "w+")
    ratio = int(info_data["Length"].get()) / int(info_data["Width"].get())
    if ratio < 1.4:
        shape = 'S'
    else:
        shape = 'W'
    s =  info_data["Size"].get() + info_data["Type"].get() + shape + ";"
    s = s.upper()
    f.write(s)

    f.write(info_data["Price"].get() + ";")

    s = ""
    for key in info_data.keys():
        f.write(info_data[key].get() + " ")
    f.write(s)
    f.close()

    sendCommand(['glabels-3-batch', '-i', path, '-o', f_out, barcode_layout])


def printLabel():
    sendCommand(['lpr', '-P', printer_name, "./labels/label.pdf"])
    sendCommand(['lpr', '-P', printer_name, "./labels/barcode.pdf"])
    

def printCurrent():
    saveLabelData()
    saveBarcodeData()
    printLabel()

def printSave():
    saveMonitor()
    saveLabelData()
    saveBarcodeData()
    printLabel()

def getInfo():
    global monitor_data
    global monitor_select
    info_strings = getHwInfo()
    monitor_list = list()
    for i in range(0, len(info_strings)):
        monitor_data.append(dict())
        hwInfoParse(info_strings[i], monitor_data[i])
        monitor_list.append(str(i) + " " + monitor_data[i]["Vendor"] + " " + monitor_data[i]["Model"])
    
    monitor_select.destroy()
    monitor_select = OptionMenu(window, StringVar(value = "Monitor: "), *monitor_list, command=monitorChange)
    monitor_select.config(font = font, width = width)
    monitor_select.grid(row=1, column=2, sticky = W)

        
def exitProgram():
    exit()

def restartProgram():
    python = sys.executable
    os.execl(python, python, * sys.argv)

window = tkinter.Tk()

button_list = [
                ["Extract", getInfo],
                ["", None],
                ["Print Save", printSave],
                ["Print", printCurrent],
                ["Print Last", printLabel],
                ["", None],
                ["Ebay", webSearch],
                ["", None],
                ["Restart", restartProgram],
                ["Exit", exitProgram]
]
for i in range(len(button_list)):
    if button_list[i][0] != "":
        Button(window, font = font, width = width, text = button_list[i][0], command=button_list[i][1]).grid(row = i, column = 1, sticky = sticky)

monitor_select = OptionMenu(window, StringVar(value = "SELECT"), "", command=monitorChange)
monitor_select.grid(row=0, column=2, sticky = W)

for i in range(0, len(info_keys)):
    info_data[info_keys[i]] = StringVar()
    Entry(window, font = font, width = width+5, textvariable = info_data[info_keys[i]]).grid(row=i+2, column=2, sticky = W)

for i in range(0, len(port_keys)):
    port_data[port_keys[i]] = IntVar()
    Checkbutton(window, font = font, text = port_keys[i], variable = port_data[port_keys[i]], command=portChange).grid(row=i, column=3, sticky = W)

for i in range(0, len(type_keys)):
    Radiobutton(window, font = font, text = type_keys[i], variable = info_data["Type"], value = type_keys[i]).grid(row=i, column=4, sticky = W)


getInfo()

window.mainloop()