# dymo printer

dymo printer will not work right away

https://github.com/Kyle-Falconer/DYMO-SDK-for-Linux

```
sudo apt-get install git libcups2-dev libcupsimage2-dev gcc g++ automake
cd ~/
git clone https://github.com/Kyle-Falconer/DYMO-SDK-for-Linux.git
cd DYMO-SDK-for-Linux
aclocal
automake --add-missing
autoconf
./configure
make
sudo make install
```


get printer name
```
lpstat -p -d
```

->
```
device for LabelWriter-450: usb://DYMO/LabelWriter%20450?serial=01010112345600
```
