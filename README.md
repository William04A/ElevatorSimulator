# ElevatorSimulator
An elevator simulator written in Python (for Windows)
# Information
A simple elevator simulator that gives you the control over an elevator. There are several modes described below. To learn how to install the program, see "Install" below.
# Install the simulator
1. First, dowload the **Latest release**, which is a Python (.py) file named something like "MainProgramPublic1.1". This file can be opened in Python, but it needs a little customization first.
2. Download **all** the sound files, which include floor number announcements, emergency mode messages and more. These sound files can be found in this repository.
3. Put the files in a folder named something. The easier would be to place it under C:\Users\(your username)\Downloads\ElevatorSounds. Replace "C:" with the letter of the drive that your folder is in and "(your username)" with your Windows username.
4. Now, place all the sound files in this folder.
5. Now it´s time to change some things in the main program. Find all codes containing this:
--------
        **winsound.PlaySound("C:\\Users\Username\Downloads\ElevatorSounds\\0.wav", winsound.SND_FILENAME)**
--------
Now, change the directory of each file to the directory that you have put all your sounds in. This is easy if you just replace all words that you need. **JUST CHANGE THE USER, DRIVE AND/OR FOLDERS IF YOU HAVENT´T RENAMED THE FILES!** You have to do this every time a directory/path like this is mentioned. You can find the code using this in the top of the code, in some def-blocks.
6. Run the code and enjoy.
--------
# Modes - Explained:
The program has different modes that can be applied to the elevator. Here is a list fo them:
**CALLFLOOR (Floor number)** - Make the elevator go to the mentioned floor. The standard code configuration has floors between 0 and 10.
**ELEVATORSTATUS** - Get the status of the elevator.
**EMERMODE** - Emergency mode - if the mode is on, no calls can be made to the elevator. To controll it, you can use the DOOROPEN and DOORCLOSE-commands.
**EMERMODEOFF** - Turn off the emergency mode.
**STANDBY (Seconds)** - Turn off the elevator (put it in standby) for a specific amount of seconds.
**DOOROPEN** - Open the elevator doors.
**DOORCLOSE** - Close the doors of the elevator.
**ANNOUNCEMENT** - Play an announcement in the elevator.
**AUTO** - Run the elevator automatically. Random calls and actions are generated. The **AUTO** command can only be turned off by turning off the program manually as it is in a while True-loop.

--------
# Credits:
To the makers and contributers of Python for making and developing this coding language.
To GitHub and all its contributors.
Sound: www.text2speech.org is the source for the elevator´s voice and the source for all the sound files you download.
-------
# Have fun with this elevator code!
