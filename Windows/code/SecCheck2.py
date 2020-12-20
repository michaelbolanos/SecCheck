# Author:  Michael Bolanos
#
# Date created:
# Last Edited: 12-20-17 7:44AM
#
#
# Import the PySimpleGUI for Gui, might change to Tkinter
#
# Import sys for OS checker
# Import urllib for IP Checker
# Import platform for System Information
# Import wmi for checking Windows disk space
#

# To create the app and exe use Pyinstaller with the following options:
#
#       OSX: pyinstaller --windowed --onefile --icon otgtree.icns SecCheck2.py
#       Windows: pyinstaller --windowed --onefile --icon otgtree.icns SecCheck2.py
#       Linux:  TBD
#
import PySimpleGUI as sg, urllib.request, os, platform, sys
from tkinter import *
import webbrowser
# import wmi

# =============================================================================

# This theme is Green with Yellow
#
sg.theme('DarkGreen7')    # Keep things interesting for your users

# Function for OS Checker
#

def get_platform():
    platforms = {
        'linux1': 'Some kind of Linux',
        'linux2': 'Some kind of other Linux',
        'darwin': 'Apple OS X',
        'win32': 'Microsoft Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]

# =============================================================================
# Check the WAN IP
#
external_ip = urllib.request.urlopen('http://ident.me').read().decode('utf8')

my_system = platform.uname()


# Button for Remote Support Link
#
remote_support_window = Tk(className="Python Remote support by offthegridit")
new = 1
url = "https://offthegridit.com/remote-support"

remote_support_window.geometry("400x49")

#set window color
remote_support_window['bg']='green'

# =============================================================================
# Function disk space
#



# def otg_all_disks_for_windows():
#    conn = wmi.WMI()
#    for disk in conn.Win32_LogicalDisk():
#        if disk.size != None:
#            print(disk.Caption, "is {0:.2f}% free".format(100*float(disk.FreeSpace)/float(disk.Size)))
#            return str(disk.Caption, "is {0:.2f}% free".format(100*float(disk.FreeSpace)/float(disk.Size)))

# call the function for disk space to output to console
# otg_all_disks_for_windows()

# print the disk space


# =============================================================================
# Function to open second window and display link to offthegridit support
#
def openweb():
    webbrowser.open(url,new=new)

Btn = Button(remote_support_window, text = "This opens the offthegridit Remote Support Link",command=openweb)
Btn.pack()


# =============================================================================
# Window for displaying our app "PySimpleGUI"
#
# This is Testing 1 is still being tested 12-19-20 MJB
#
# conn = wmi.WMI()
# disk_space = disk.Caption

layout = [[sg.Text("              This window stays open until you close it" + "\n\n" + "All rights reserved.  ©offthegridit" +
                    "\n\n\n" +
                    "\n\n" +
                    "Your external/WAN IP Address is:  " + external_ip +
                    "\n\n" +
                    " Your operating system is: " + (get_platform()) +
                    "\n\n" +
# From Testing 1
#                    " Your disk space is "  + "don't know yet :-(" + otg_all_disks_for_windows(disk.Caption) +
                    "\n\n" +
                    "Please enter your credentials")],
          [sg.Input(key='-IN-')],
          [sg.Button('Authenticate with offthegridit Security Protocol'), sg.Button("Close Connection")]]

window = sg.Window('Security Check by offthegridit', layout)


# =============================================================================
# Our Event Loop
#
while True:
    event, values = window.read()
    print("Hello Again " + get_platform())
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Close Connection':
        break

# root.mainloop()

window.close()
# =============================================================================
# End of program