import json, ctypes, auth, shutil, richpresence 
from time import sleep
from os import system, name, sys, path
from additional import application_path, clear

def main():
    splashScreen()
    option(UI())
    
def optionUI():
    while True:
        option(UI())

def option(selection):
    """Selction based on the number you chose. Look at list to modify.

    Args:
        selection (int): Runs lines of code based on a conditional

    Returns:
        [void]: Doesn't return anything. Just here in case errors.
    """
    if(selection == 1):
        clear()
        auth.main()
        optionUI()
    elif(selection == 2):
        print("Run the command 'Ctrl C' to exit the program.")
        print("Loading Code ...")
        sleep(2)
        clear()
        richpresence.richpresence()
    elif(selection == 3):
        if(path.isdir(application_path() + "\\tokens") == True):
            shutil.rmtree(application_path() + "\\tokens")
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
    elif(selection == 4):
        sys.exit()
    else:
        print("WIP")
        sleep(2)
        clear()
        optionUI()
        
def UI():
    """Main graphics ui. Currently it is a terminal UI.

    Returns:
        [void]: Doesn't return anything. Here in case errors.
    """
    system('color 2')
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Halo: MCC Rich Presence")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("List: ")
    print('1. Sign in using Oauth 2.0 (Requires you to save a link that looks like "https://localhost/oauth_success?code=M.R3_BAY.<code>")')
    print("2. Launch the Rich Presence (Requires /tokens folder)")
    print("3. Delete your Credentials")
    print("4. Exit")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Current Build: 0.3.3")
    print("------------------------------------------------------------------------------------------------------------------------")
    selection = int(input("Select from list: "))
    return selection

def splashScreen():
    """Creates a Screen to show the devs and other program info.
    """
    clear()
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Halo: MCC Rich Presence")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Created by kay-el-zed, Gurrman375D.")
    print("Maintained by Gurrman375D.")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Current Build: 0.3.3")
    print("------------------------------------------------------------------------------------------------------------------------")
    sleep(5)
    clear()

        
if __name__ == "__main__":
    system('color 2')
    try:
        ctypes.windll.kernel32.SetConsoleTitleW("Halo Master Chief Collection Rich Presence")
        main()
    except KeyboardInterrupt as e:
        print(e)
        sleep(1)
        clear()
        print("Manually Close the App")
        optionUI()