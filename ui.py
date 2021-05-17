import richpresence, json
from time import sleep
from os import system, name, sys
from additional import clear

def main():
    splashScreen()
    option(UI())
    
def optionUI():
    while True:
        option(UI())

def option(selection):
    if(selection == 1):
        print("Run the command 'Ctrl C' to return to the menu.")
        print("Loading Code ...")
        sleep(2)
        clear()
        richpresence.main()
    elif(selection == 2):
        with open(richpresence.application_path() + "\\credentials.json", 'w') as f:
            Credentials = {
                "email": "",
                "xuid": ""
            }
            json.dump(Credentials, f, indent=2)
        
        with open(richpresence.application_path() + "\\rpc.json", 'w') as j:
            rpc = {
                "details": "",
                "state": "",
                "device": "",
                "game": ""
            }
            json.dump(rpc, j, indent=2)
        sleep(2)
        clear()
        optionUI()
    elif(selection == 3):
        sys.exit()
    else:
        print("WIP")
        sleep(2)
        clear()
        optionUI()
        
def UI():
    system('color 2')
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Halo: MCC Rich Presence")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("List: ")
    print("1. Launch the Rich Presence (Requires Email, Password, and XUID)")
    print("2. Delete your Credentials")
    print("3. Exit")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Current Build: 0.3.0")
    print("------------------------------------------------------------------------------------------------------------------------")
    selection = int(input("Select from list: "))
    return selection

def splashScreen():
    clear()
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Halo: MCC Rich Presence")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Created by kay-el-zed, Gurrman375D.")
    print("Maintained by Gurrman375D.")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Current Build: 0.3.0")
    print("------------------------------------------------------------------------------------------------------------------------")
    sleep(5)
    clear()

        
if __name__ == "__main__":
    system('color 2')
    try:
        main()
    except KeyboardInterrupt as e:
        print(e)
        sleep(1)
        clear()
        print("Manually Close the App")
        optionUI()