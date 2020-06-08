
#Imports two Libraries (Subprocess for altering the commands to match the OS & Platform for detecting which commands need to be used)
import subprocess
import sys
import platform
import os
from colorama import init
init (strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format
line = '**************************************'

#**************************************************************************************************************************************

def Menu():
   
    print('Python Network Connector')
    print(line)
    print("Menu")
    print("1:   List Available Networks")
    print("2:   Connect/Disconnect")
    print("3:   Run Connection test")
    print("4:   Exit")
    menuloop = True
    while menuloop == True:
        try: 
            menuinp = input("Please select an option to begin: \n")
            menuinp = int(menuinp)
            if menuinp == 1:
                Results()
            elif menuinp == 2:
                ConnDisconn()
            elif menuinp == 3:
                ConnTest()
            elif menuinp == 4:
                exit
            elif menuinp == 69:
                cprint(figlet_format('kek', font='banner3'), 'green')
            break
        except ValueError:
            print ("Please Enter a Valid Input")
            print(line)
            print("Menu")
            print("1:   List Available Networks")
            print("2:   Connect/Disconnect from a network")
            print("3:   Run Connection test")
            print("4:   Exit")
        


def Results():
    print(line)
    #If statement for Windows OS to list all networks
    if platform.system() == "Windows":
        results = subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True).stdout
        ls = results.split("/n")
        ssids = [k for k in ls if 'SSID' in k]
        print(results)
    
    #If statement for MAC OS X to list all networks - NON TESTED
    elif platform.system() == "Darwin":
        print("You're Working on MAC OS X, PLEASE NOTE YOU WILL HAVE TO ENTER YOUR PASSWORD TO RUN MOST FUNCTIONS")
        results = subprocess.run(["sudo", "ln", "-s" "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport", "airport", "-s"], capture_output=True, text=True).stdout
        ls = results.split("/n")
        ssids = [k for k in ls if 'SSID' in k]
        print(results)

    #If statement for Linux OS to list all networks - NON TESTED
    elif platform.system() == "Linux":
        results = subprocess.run(["nmcli", "dev", "wifi"], capture_output=True, text=True).stdout
        ls = results.split("/n")
        ssids = [k for k in ls if 'SSID' in k]
        print(results)
    Options()


def ConnTest():
    hostname = "www.google.co.uk"
    if platform.system() == "Windows":
        print(line)
        Conntest = subprocess.run(['ping', '-l', '500', '-n' , '5', hostname], capture_output=True, text=True).stdout
        print(Conntest)
    else:
        print(line)
        Conntest = subprocess.run(['ping', 'www.google.co.uk', '-n', '5'], capture_output=True, text=True).stdout
    Options()

def Options():
    print(line)
    print("Options")
    print("1:   Show Available Networks")
    print("2:   Connect/Disconnect")
    print("3:   Run Connection Test")
    print("4:   Return to Menu")
    print("5:   Quit")
    optionloop = True
    while optionloop == True:
        try:
            resultinp = input("What would you like to do? \n")
            resultinp = int(resultinp)
            if resultinp == 1:
                Results()
            elif resultinp == 2:
                ConnDisconn()
            elif resultinp == 3:
                ConnTest()
            elif resultinp == 4:
                Menu()
            elif resultinp == 5:
                exit
            break
        except ValueError:
            print("Please enter a Valid Input")
            print(line)
            print("1:   Show Available Networks")
            print("2:   Connect/Disconnect to a Network")
            print("3:   Run Connection Test")
            print("4:   Return to Menu")
            print("5:   Quit")
            print(line)
     
def ConnDisconn():
    Connected()

def Connected():
    proc = subprocess.Popen(['ping', 'www.google.co.uk'], stdout=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    if proc.returncode == 0:
        current = os.popen('netsh wlan show interfaces | findstr /r "^....SSID"').read()
        if ":" in current: current = current.split(":",1)[1].strip().rstrip("\n")
        print("You are Currently Connected to: " + current)
        
    else:
        print("You are not Currently Connected to a Network via WiFi")

Menu()