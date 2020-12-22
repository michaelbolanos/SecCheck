We appreciate your support

<a href="https://paypal.me/offthegridit">
    <img src="https://img.shields.io/badge/$-donate-ff69b4.svg?maxAge=2592000&amp;style=flat">
  </a>


## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Wiki](#wiki)
* [Just run the apps](#just-run-the-apps)
* [Loop](#Loop)
* [About the author](#about-the-author)
* [To do or not to do](#to-do-or-not-to-do)

## General info
SecCheck is a Python program to display a user's workstation statistics in a GUI.

v.1.0-v.2.2

There may be some security checks implemented in this program.

Inherently, Windows 10 already detects the .EXE as malware so there is an implied security checker as a byproduct..

- Detected as malware in Windows 10 Defender (false positive)
- You must tell Windows to just run the program if Bitdefender is on keep an eye out for notifications
- This is only a security aid and does not offer protection


- Project Created:  12/11/20


## Technologies
This program was written to practice Python with some practical application in mind.


## Wiki

Wiki pages to content your heart
[Wiki](https://github.com/michaelbolanos/SecCheck/wiki)



## Just run the apps
If you just want to run the Apps the programs by themselves are in the Apps directory

Apps (Releases)
[SecCheck_Releases](https://github.com/michaelbolanos/SecCheck/releases)

Normally you will run these apps from the Downloads folder

## Loop
If you want to see a fancy version of this project on
[github.io.mb/SecCheck](https://michaelbolanos.github.io/SecCheck/) although, you might already be here

## Project level 

Novice.

## About the author


Author:   Michael Bolanos

Michael Bolanos is a freelance IT & Security Consultant

The purpose of this project is to gather some code and make progress in learning Python programming.

## Background

Many people learn best doing things hands on.  My meager programming skills have gotten me to this point.  I have always wanted to write cross platform apps for security. So, this is my meager attempt.  It gives me a way to practice Python, deploying my code, and pushing it to Github to collaborate with others.

I found some motivation here:  [Google IT Automation with Python](https://www.coursera.org/professional-certificates/google-it-automation)

I am going through the materials and quizzes and making progress.  I practice code at least 2-4 hours everyday, that also involves watching YouTube (sometimes), reading up on individual topics, trying stuff in my IDE (PyCharm), and Idle sometimes.  

I made a simple GUI (with PySimpleGUI, and Tkinter), and with Pyinstaller I created an EXE for Windows and an app for Mac (need to output for Linux.)

## To do or not to do

- Add some buttons with additional modules
- More security checking
- Bitdefender complaining, Unknown Publisher (this could be useful)
- Better colors, people like a pretty GUI
- Run Windows Bitdefender scan e.g. MpCmdRun.exe -Scan -ScanType 2 - note caused max cpu utilization 12-21-20
Maybe enable CPU throttling https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-antivirus/command-line-arguments-microsoft-defender-antivirus
- Currently using Github Pages to distribute binary images, consider using releases instead or only.


```

## Snippet

# Author:  Michael Bolanos
#
#
# Import the PySimpleGUI for Gui, might change to Tkinter
#
# Import sys for OS checker
# Import urllib for IP Checker
# Import platform for System Information
# Import wmi for checking Windows disk space
#
#
import PySimpleGUI as sg, urllib.request, os, platform, sys
from tkinter import *
import webbrowser
import wmi


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
def otg_all_disks_for_windows():
    conn = wmi.WMI()
    for disk in conn.Win32_LogicalDisk():
        if disk.size != None:
            print(disk.Caption, "is {0:.2f}% free".format(100*float(disk.FreeSpace)/float(disk.Size)))
            return str(disk.Caption, "is {0:.2f}% free".format(100*float(disk.FreeSpace)/float(disk.Size)))

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
# End of program```

