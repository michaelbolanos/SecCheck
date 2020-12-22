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
[Github Pages](https://michaelbolanos.github.io/SecCheck/) although, you might already be here

## Project level 

Novice.

## About the author


Author:   Michael Bolanos

Michael Bolanos is a freelance IT & Security Consultant

The purpose of this project is to gather some code and make progress in learning Python programming.

## Background

Many people learn best doing things hands on.  My meager programming skills have gotten me to this point.  I have always wanted to write cross platform apps for security. So, this is my meager attempt.  It gives me a way to practice Python, deploying my code, and pushing it to Github to collaborate with others.

I found some motivation here:  [Google IT Automation with Python](https://www.coursera.org/professional-certificates/google-it-automation)

I made a simple GUI (with PySimpleGUI, and Tkinter), and with Pyinstaller I created an EXE for Windows and an app for Mac (need to output for Linux.)

## To do or not to do

- Add some buttons with additional modules
- More security checking
- Bitdefender complaining, Unknown Publisher (this could be useful)
- Better colors, people like a pretty GUI
- Run Windows Bitdefender scan e.g. MpCmdRun.exe -Scan -ScanType 2 - note caused max cpu utilization 12-21-20
Maybe enable CPU throttling https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-antivirus/command-line-arguments-microsoft-defender-antivirus
- Currently using Github Pages to distribute binary images, consider using releases instead or only.

