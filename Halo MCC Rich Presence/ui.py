import authenticate, Rich_Presence, removetoken, os, time, xbox, sys, ui, Debug
from os import system, name
os.system('color 2')

def UI():
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Halo: MCC Rich Presence")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("List: ")
    print("1. Create a Token")
    print("2. Launch the Rich Presence (Requires a Token)")
    print("3. Current Xbox Live Status (Requires a Token)")
    print("4. Delete your Token")
    print("5. Exit (You might have to press twice)")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Current Build: 0.2.7")
    print("------------------------------------------------------------------------------------------------------------------------")
    selection = int(input("Select from list: "))
    return selection

def option(selection):
    try:
        if(selection == 1):
            clear()
            removetoken.createToken()
            authenticate.main()
            clear()
            UI()
        elif(selection == 2):
            clear()
            Rich_Presence.main()
            clear()
            UI()
        elif(selection == 3):
            clear()
            Debug.main()
            clear()
            UI()
        elif(selection == 4):
            clear()
            removetoken.main()
            clear()
            UI()
        elif(selection == 5):
            print("Goodbye")
            time.sleep(2)
            sys.exit(0)
        else:
            print("Invalid Input.")
            clear()
            UI()
    except Exception as e:
        print(e)
        sys.exit(-1)

def splashScreen():
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Halo: MCC Rich Presence")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Created by kay-el-zed.")
    print("Maintained by Gurrman375D.")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Current Build: 0.2.7")
    print("------------------------------------------------------------------------------------------------------------------------")
    time.sleep(5)
    clear()

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    # MacOs support and Linux Support someday 
    else: 
        _ = system('clear')