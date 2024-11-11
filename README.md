# EMCOMM-Print

This tool is intended to streamline HAM-Radio emergency communications where typically one HAM-Radio operator is working as a message broker for multiple stakeholders in "one location" using Winlink Express*. Printing messages quickly to a Receipt/POS-printer allows quick message distribution and easy destruction of the messages after use (Thermal Paper has tendency to ruin itself even in pocket) 

Tool itself is not Winlink specific but that is the scenario I use it for.  

This tool monitors a folder, called Incoming on disk for text files saved there and dumps them into a receipt/POS printer as soon as they land to that folder. After printing the file is moved to a Processed folder 

I have used a NETUM USB thermal printer with 58mm rolls in my setup https://www.amazon.de/-/en/Wireless-Bluetooth-Occupancy-Restaurants-Compatible/dp/B0854CCF75/

Any printer can be used as long as you get it working with Windows. 

Finnish version of instructions with pictures is available in our club website https://oh2abb.fi/kuittikirjoittimen-hyodyntaminen-viestiliikenneharjoituksissa/ 
73 de OH2FBJ  

# Setup

1) You need python for Windows https://www.python.org/downloads/windows/ , preferably 3.11.x 
2) You need to clone this repo 
3) Install the required dependencies if not already present (Should be included in the Python distribution already)
``` 
time
os
shutil
time
configparser

```
4) Create folders on desired location on your computer where you want to save the files and where the processed files are moved 
5) Update the file called config.txt with your desired folder locations as per example below
```python 
[emcomm-print]
incoming_dir = C:/EMCOMM/Incoming/
processed_dir = C:/EMCOMM/Processed/
```
6) Install drivers for the Receipt/POS-printer you are using
7) Open notepad in Page setup select the right paper type for your receipt/POS-printer in my case that is "ZPrinter Paper", set marginals to minimum (this might require some testing, I have found adding small top margin and 0.01 to right to work for me)
If you want you can use Header to designate messages with for example "CONFIDENTIAL" which will be then printed before the actual message. **DO NOT use the Footer field** in page setup, otherwise the print will be a mile long because notepad still thinks you can fit A4 worth of whitespace before the footer is printed 
![Notepad Page Setup](https://oh2abb.fi/emcomm-print-notepad.png)
9) Set the Receipt printer as default in Notepad 
8) If you want you can create a shortcut on desktop to start the Python script in background 
```` 
%systemroot%\System32\cmd.exe /c "pythonw C:\location\to\the\script\EMCOMM\emcomm-print.py"
````



## Usage
Start the application either by running a powershell/cmd window and command "python.exe emcomm-print.py" or using the shortcut method described above

Save message from Winlink to the folder you defined as incoming_dir 
Script scans the incoming folder every 1 second for new files and prints them out using notepad

## Example print
![Example Print](https://oh2abb.fi/emcomm-print.png)