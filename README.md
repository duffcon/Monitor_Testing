# hwinfo

install
```
sudo apt install hwinfo
```

list connected monitors
```
hwinfo --monitor --short
```

->
```
monitor:                                                        
                       DELL P1917S
```


get info about monitor

resolution, model number, size, ect...

```
hwinfo --monitor
```

->

```
20: None 01.0: 10002 LCD Monitor
  [Created at monitor.125]
  Unique ID: wkFv.H9Umskd85kF
  Parent ID: VCu0.lXk6gYCFb95
  Hardware Class: monitor
  Model: "DELL P1917S"
  Vendor: DEL "DELL"
  Device: eisa 0xd092 "DELL P1917S"
  Serial ID: "9PX3G7721N0B"
  Resolution: 720x400@70Hz
  Resolution: 640x480@60Hz
  Resolution: 640x480@75Hz
  Resolution: 800x600@60Hz
  Resolution: 800x600@75Hz
  Resolution: 1024x768@60Hz
  Resolution: 1024x768@75Hz
  Resolution: 1280x1024@75Hz
  Resolution: 1152x864@75Hz
  Resolution: 1280x1024@60Hz
  Size: 375x300 mm
  Year of Manufacture: 2017
  Week of Manufacture: 26
  Detailed Timings #0:
     Resolution: 1280x1024
     Horizontal: 1280 1328 1440 1688 (+48 +160 +408) +hsync
       Vertical: 1024 1025 1028 1066 (+1 +4 +42) +vsync
    Frequencies: 108.00 MHz, 63.98 kHz, 60.02 Hz
  Driver Info #0:
    Max. Resolution: 1280x1024
    Vert. Sync Range: 56-76 Hz
    Hor. Sync Range: 30-81 kHz
    Bandwidth: 108 MHz
  Config Status: cfg=new, avail=yes, need=no, active=unknown
  Attached to: #10 (VGA compatible controller)
```