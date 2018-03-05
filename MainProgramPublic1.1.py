import time
import random
import winsound
#Customize the file directory to where you have put the sound files!
def floorsound():
    if currentfloor == 0:
        winsound.PlaySound("C:\\Users\Username\Downloads\ElevatorSounds\\0.wav", winsound.SND_FILENAME)
    if currentfloor == 1:
        winsound.PlaySound("C:\\Users\Username\Downloads\ElevatorSounds\\1.wav", winsound.SND_FILENAME)
    if currentfloor == 2:
        winsound.PlaySound("C:\\Users\Username\Downloads\ElevatorSounds\\2.wav", winsound.SND_FILENAME)
    if currentfloor == 3:
        winsound.PlaySound("C:\\Users\Username\Downloads\ElevatorSounds\\3.wav", winsound.SND_FILENAME)
    if currentfloor == 4:
        winsound.PlaySound("C:\\Users\Username\Downloads\ElevatorSounds\\4.wav", winsound.SND_FILENAME)
    if currentfloor == 5:
        winsound.PlaySound("C:\\Users\Username\Downloads\ElevatorSounds\\5.wav", winsound.SND_FILENAME)
    if currentfloor == 6:
        winsound.PlaySound("C:\\Users\Username\Downloads\ElevatorSounds\\6.wav", winsound.SND_FILENAME)
    if currentfloor == 7:
        winsound.PlaySound("C:\\Users\Username\Downloads\ElevatorSounds\\7.wav", winsound.SND_FILENAME)
    if currentfloor == 8:
        winsound.PlaySound("C:\\Users\Username\Downloads\ElevatorSounds\\8.wav", winsound.SND_FILENAME)
    if currentfloor == 9:
        winsound.PlaySound("C:\\Users\Username\Downloads\ElevatorSounds\\9.wav", winsound.SND_FILENAME)
    if currentfloor == 10:
        winsound.PlaySound("C:\\Users\Username\Downloads\ElevatorSounds\\10.wav", winsound.SND_FILENAME)
def doorclose():
    winsound.PlaySound("C:\\Users\Username\Downloads\ElevatorSounds\\Doorsclosing.wav", winsound.SND_FILENAME)
def dooropen():
    winsound.PlaySound("C:\\Users\Username\Downloads\ElevatorSounds\\Doorsopen.wav", winsound.SND_FILENAME)
def emergencymode():
    winsound.PlaySound("C:\\Users\Username\Downloads\ElevatorSounds\\Emergency.wav", winsound.SND_FILENAME)
def emergencymodereminder():
    winsound.PlaySound("C:\\Users\Username\Downloads\ElevatorSounds\\Emergencyreminder.wav", winsound.SND_FILENAME)
def announce1():
    winsound.PlaySound("C:\\Users\Username\Downloads\ElevatorSounds\\Thankyou1.wav", winsound.SND_FILENAME)
def announce2():
    winsound.PlaySound("C:\\Users\Username\Downloads\ElevatorSounds\\Haveaniceday.wav", winsound.SND_FILENAME)
#Main code:
print("Elevator simulator 1.1 Public release")
print("Connecting to elevator...")
time.sleep(random.randint(1,2))
print("Connection stable.")
arrived = time.ctime()
currentfloor = random.randint(1,10) #Change building stories index here if you want to.
calls = 0 #Start with no elevator calls - NEEDS TO BE "0" TO WORK PROPERLY!
doorsensor = 0 #Start with no person in front of the doors
doorstate = "CLOSED" #Start with door closed
emergency = 0 #Start without emergency mode
while True:
    print("______________________________")
    print("ELEVATOR CONSOLE BUILD 2")
    print("CALLFLOOR (Floor number) - Send elevator to a floor")
    print("ELEVATORSTATUS - Get status")
    print("EMERMODE - Emergency mode - elevator cancels all calls and stops even if it´s not on a floor until the mode is stopped.")
    print("EMERMODEOFF - Turn off emergency mode.")
    print("STANDBY (Seconds) - Places the elevator in standby mode for a specific amount of seconds.")
    print("DOOROPEN - Open the elevator doors.")
    print("DOORCLOSE - Close the elevator doors.")
    print("ANNOUNCEMENT - Play a sound in the elevator")
    print("AUTO - Simulate elevator events.")
    mode = input("Please select your desired mode. ")
    if "CALLFLOOR" in mode:
        if calls == 0:
            if emergency == 0:
                calledfloor = int(mode.replace("CALLFLOOR",""))
                if calledfloor > 10:
                    print("Floor " + str(calledfloor) + " could not be found in this buildning.")
                elif calledfloor < 0:
                    print("Floor " + str(calledfloor) + " could not be found in this building.")
                else:
                    if calledfloor == currentfloor:
                        print("Elevator is already on floor " + str(calledfloor) + ".")
                    else:
                        print("Calling on floor " + str(calledfloor) + " from " + str(currentfloor) + ".")
                        if currentfloor > calledfloor:
                            direction = "DOWN"
                            floordifference = currentfloor-calledfloor
                        elif currentfloor < calledfloor:
                            direction = "UP"
                            floordifference = calledfloor - currentfloor
                        time.sleep(floordifference) #Elevator gets to one floor each second.
                        currentfloor = calledfloor
                        print("Elevator headed " + direction + " in " + str(floordifference) + " seconds and is now on floor " + str(currentfloor) + ".")
                        arrived = time.ctime()
                        floorsound()
                        #Opening doors
                        doorstate = "OPEN"
                        dooropen()
                        while doorsensor == 1:
                            print("Door sensor - Person in front of door.")
                            time.sleep(5)
                        doorstate = "CLOSED"
                        time.sleep(5)
                        doorclose()
            else:
                print("Emergency mode activated.")
                emergencymodereminder()
        else:
            print("Please wait for all calls to finish first.")
    elif mode == "ELEVATORSTATUS":
        print("Current elevator status.")
        print("Time: " + time.ctime() + ".")
        print("Current floor: " + str(currentfloor))
        print("Arrived to floor at: " + str(arrived) + ".")
        print("Doorstate: " + str(doorstate) + ".")
        time.sleep(5)

    elif mode == "EMERMODE":
        confirm = input("CONFIRM EMERGENCY MODE WITH YES: ")
        if confirm == "YES":
            if emergency == 0:
                print("EMERGENCY MODE ACTICVATED!")
                emergency = 1
                emergencymode()
            else:
                print("Emergency stop already active!")
        else:
            print("Exiting.")
    elif mode == "EMERMODEOFF":
        confirm2 = input("TURN OFF EMERGENCY MODE WITH YES: ")
        if confirm2 == "YES":
            if emergency == 1:
                emergency = 0
                print("Emergency mode turned off.")
            else:
                print("Emergency stop is already activated.")
        else:
            print("Exiting.")
    elif mode == "AUTO":
        print("Auto mode activated. Stop the program manually to exit.")
        while True:
            if calls == 0:
                if emergency == 0:
                    calledfloorauto = random.randint(0,10)
                    calls = 1
                    if calledfloorauto > 10:
                        print("Floor " + str(calledfloorauto) + " could not be found in this buildning.")
                    elif calledfloorauto < 0:
                        print("Floor " + str(calledfloorauto) + " could not be found in this building.")
                    else:
                        if calledfloorauto == currentfloor:
                            print("Elevator is already on floor " + str(calledfloorauto) + ".")
                        else:
                            print("Calling on floor " + str(calledfloorauto) + " from " + str(currentfloor) + ".")
                            if currentfloor > calledfloorauto:
                                direction = "DOWN"
                                floordifference = currentfloor-calledfloorauto
                            elif currentfloor < calledfloorauto:
                                direction = "UP"
                                floordifference = calledfloorauto - currentfloor
                            announceauto = random.randint(1,2)
                            if announceauto == 1:
                                announcement = random.randint(1, 2)
                                if announcement == "1":
                                    announce1()
                                    print("Announcement " + announcement + " played!")
                                    time.sleep(floordifference)  # Elevator gets to one floor each second.
                                    currentfloor = calledfloorauto
                                    print("Elevator headed " + direction + " in " + str(floordifference) + " seconds and is now on floor " + str(currentfloor) + ".")
                                    arrived = time.ctime()
                                    floorsound()
                                    # Opening doors
                                    doorstate = "OPEN"
                                    dooropen()
                                    doorsensor = random.randint(0, 1)
                                    while doorsensor == 1:
                                        print("Door sensor - Person in front of door.")
                                        time.sleep(5)
                                        doorsensor = random.randint(1, 5)
                                    time.sleep(5)
                                    doorclose()
                                    doorstate = "CLOSED"
                                    calls = 0
                                elif announcement == "2":
                                    announce2()
                                    print("Announcement " + announcement + " played!")
                                    time.sleep(floordifference)  # Elevator gets to one floor each second.
                                    currentfloor = calledfloorauto
                                    print("Elevator headed " + direction + " in " + str(floordifference) + " seconds and is now on floor " + str(currentfloor) + ".")
                                    arrived = time.ctime()
                                    floorsound()
                                    # Opening doors
                                    doorstate = "OPEN"
                                    dooropen()
                                    doorsensor = random.randint(0, 1)
                                    while doorsensor == 1:
                                        print("Door sensor - Person in front of door.")
                                        time.sleep(5)
                                        doorsensor = random.randint(1, 5)
                                    time.sleep(5)
                                    doorclose()
                                    doorstate = "CLOSED"
                                    calls = 0
                            else:
                                time.sleep(floordifference) #Elevator gets to one floor each second.
                                currentfloor = calledfloorauto
                                print("Elevator headed " + direction + " in " + str(floordifference) + " seconds and is now on floor " + str(currentfloor) + ".")
                                arrived = time.ctime()
                                floorsound()
                                #Opening doors
                                doorstate = "OPEN"
                                dooropen()
                                doorsensor = random.randint(0,1)
                                while doorsensor == 1:
                                    print("Door sensor - Person in front of door.")
                                    time.sleep(5)
                                    doorsensor = random.randint(1,5)
                                time.sleep(5)
                                doorclose()
                                doorstate = "CLOSED"
                                calls = 0
            time.sleep(random.randint(1,60)) #Change the second number to (maybe) decrease the time between two calls.
    elif "STANDBY" in mode:
        waitstandby = int(mode.replace("STANDBY",""))
        print("Waiting in standby for " + str(waitstandby) + " seconds." + "(" + str(waitstandby/60) + " minutes)")
        time.sleep(waitstandby)
    elif mode == "DOOROPEN":
        if doorstate == "CLOSED":
            doorstate = "OPEN"
            dooropen()
        else:
            print("Doors are already open.")
    elif mode == "DOORCLOSE":
        if doorstate == "OPEN":
            while doorsensor == 1:
                print("Door sensor - Person in front of door.")
                time.sleep(5)
            doorstate = "CLOSED"
            doorclose()
    elif mode == "ANNOUNCEMENT":
        print("1 - Thank you for visiting us-announcement.")
        print("2 - Have a nice day-announcement.")
        announcement = input(str("Which announcement do you want to play? "))
        if announcement == "1":
            announce1()
            print("Announcement " + announcement + " played!")
        elif announcement == "2":
            announce2()
            print("Announcement " + announcement + " played!")
        else:
            print("Exiting.")
    print("\n\n\n\n\n\n\n\n\n\n\n")

