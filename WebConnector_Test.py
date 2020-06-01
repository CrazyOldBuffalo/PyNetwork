import subprocess
line = '**************************************'

def clear():
    i = 1
    while i < 10:
        print(" \n")
        i += 1


def Menu():
    print("Python Network Connector")
    print(line)
    print("Menu")
    print("1:   List Available Networks")
    print("2:   Connect/Disconnect from a network")
    print("3:   Run Connection test")
    print("4:   Exit")
    menuinp = int(input("Please select an option to begin: \n"))
    if menuinp == 1:
        Results()
    elif menuinp == 2:
        print("Connect/Disconnect")
    elif menuinp == 3:
        print("Run Connection Test")
    elif menuinp == 4:
        exit
    else :
        print ("Please Enter a Valid Input")


def Results():
    clear()
    results = subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True).stdout
    ls = results.split("/n")
    ssids = [k for k in ls if 'SSID' in k]
    print(results)
    print(line)
    print("Options")
    print("1:   Connect/Disconnect to a Network")
    print("2:   Run Connection Test")
    print("3:   Return to Menu")
    print("4:   Quit")
    resultinp = int(input("What would you like to do? \n"))
    if resultinp == 1:
        print("Connect/Disconnect")
    elif resultinp == 2:
        print("Run Connection Test")
    elif resultinp == 3:
        Menu()
    elif resultinp == 4:
        exit

Menu()