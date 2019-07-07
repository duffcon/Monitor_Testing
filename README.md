# python subprocess

will be using python 3


install pip

```
sudo apt install python-pip
```

make python3 "default" temp
```
alias python=python3
```

permanent
```
sudo nano ~/.bashrc
```
alt + /
add:
```
alias python=python3
```
ctl + x
y
enter


echo command, pass hello and world
```
echo hello world
```

output
```
hello world
```

in python

```py
# file.py
from subprocess import Popen, PIPE

p = Popen(['echo', 'hello', 'world'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
output, err = p.communicate(b"")
rc = p.returncode

# print (rc)
print(output)
```

```
python file.py
```

arguments / parameters with python
```py
# file.py
from subprocess import Popen, PIPE
import sys

# print(sys.argv)
# -> s['file.py', 'hello', 'world']

# create list to pass to Popen 
command = list()
command.append('echo')
for i in range(1, len(sys.argv)):
    command.append(sys.argv[i])
# print(command)
# ->['echo', 'hello', 'world']

p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
output, err = p.communicate(b"")
rc = p.returncode

print(output)
```

```
python file.py hello world
```

hwinfo command

```py
from subprocess import Popen, PIPE
from time import sleep

p = Popen(['hwinfo', '--monitor'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
output, err = p.communicate(b"")
rc = p.returncode
if rc != 0:
    print("hwinfo error code")
    exit()
lines = str(output, 'utf-8')
lines = lines.split("\n")
for l in lines:
    l = l.strip() 
    print(l)
```

```
20: None 00.0: 10002 LCD Monitor
[Created at monitor.125]
Unique ID: rdCR.azUbeamkX1C
Parent ID: VCu0.lXk6gYCFb95
Hardware Class: monitor
Model: "X322BV-HDR"
Vendor: SPT
Device: eisa 0x0cb7 "X322BV-HDR"
Resolution: 720x400@70Hz
Resolution: 640x480@60Hz
Resolution: 800x600@60Hz
Resolution: 1024x768@60Hz
Resolution: 1024x768@60Hz
Resolution: 1280x768@60Hz
Resolution: 1360x768@60Hz
Size: 698x392 mm
Year of Manufacture: 2013
Week of Manufacture: 15
Detailed Timings #0:
Resolution: 1360x768
Horizontal: 1360 1424 1536 1792 (+64 +176 +432) +hsync
Vertical:  768  771  777  795 (+3 +9 +27) +vsync
Frequencies: 85.50 MHz, 47.71 kHz, 60.02 Hz
Year of Manufacture: 2013
Week of Manufacture: 15
Detailed Timings #1:
Resolution: 1280x768
Horizontal: 1280 1328 1360 1440 (+48 +80 +160) -hsync
Vertical:  768  771  778  790 (+3 +10 +22) +vsync
Frequencies: 68.25 MHz, 47.40 kHz, 59.99 Hz
Driver Info #0:
Max. Resolution: 1360x768
Vert. Sync Range: 59-61 Hz
Hor. Sync Range: 15-68 kHz
Bandwidth: 85 MHz
Config Status: cfg=new, avail=yes, need=no, active=unknown
Attached to: #10 (VGA compatible controller)

```

info can be parsed