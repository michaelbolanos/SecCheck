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


- Project Created:  12/11/20


## Technologies
This program was written to practice Python with some practical application in mind.


## Wiki

Wiki
[Wiki](https://github.com/michaelbolanos/SecCheck/wiki)



## Just run the apps
If you just want to run the Apps the programs by themselves are in the Apps directory

https://github.com/michaelbolanos/SecCheck/tree/main/Apps - Apps
[SecCheck_Apps](https://github.com/michaelbolanos/SecCheck/tree/main/Apps)

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

Many people learn best doing things hands on.  My meager programming skills have gotten me to this point.  I have always wanted to write cross platform apps, so this is my meager attempt while I study more Python.  It gives me a way to practice deploying my code to Github and collaborate with others.

Mastering Python has eluded me due to (blah, blah blah,) no excuses, just practice now.  So I'm working on this:

[Google IT Automation with Python](https://www.coursera.org/professional-certificates/google-it-automation)

I am going through the materials and quizzes and making progress.  I try and practice code at least 2-4 hours everyday now, that also involves watching YouTube, reading up on individual topics, trying stuff in my IDE (PyCharm), and Idle sometimes.  

I made a simple GUI (with PySimpleGUI, and Tkinter), and with Pyinstaller I created an EXE for Windows and an app for Mac (need to output for Linux.)

## To do or not to do

- Add some buttons with additional modules
- More security checking
- Why is Bitdefender complaining? (this could be useful)
- Better colors, people like a pretty GUI
- Run Windows Bitdefender scan e.g. MpCmdRun.exe -Scan -ScanType 2 - note caused max cpu utilization 12-21-20
