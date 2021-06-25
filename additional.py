import os, json
from os import system, name, sys, path
from pypresence import Presence

def application_path():
    """Get's the current application path

    Returns:
        string: Retruns current application path
    """
    if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
        application_path = os.path.dirname(sys.argv[0])
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    return application_path

def clear(): 
    """Clears terminal of all data.
    """
    if name == 'nt': 
        _ = system('cls') 
    # MacOs support and Linux not likely
    else: 
        _ = system('clear')
        
def startRPC(client_id):
    RPC = Presence(client_id)
    RPC.connect()
    return RPC

def writejsonfile():
    print("No rpc.json. Writting new file ...")
    if(path.isfile(application_path() + '\\rpc.json') != True):
        open("rpc.json", "x")
    print("You can get your steam id here: https://store.steampowered.com/account/ \nYou can also just hit enter to skip this prompt.")
    steamid = str(input("Enter steam id:"))  
    with open("rpc.json", "w") as f:
        activity = {
            "steamid": (steamid or "")
        }
        f.write(json.dumps(activity))
    return
