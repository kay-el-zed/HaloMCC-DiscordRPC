import json
import os
from os import sys
from time import time, sleep
from pypresence import Presence
from getpass import getpass

def request(username:str, password:str, xuid:str, application_path):
    """Generates a request in a terminal to receive the presence data

    Args:
        username (str): The email of the user
        password (str): The password of the user
        xuid (str): The id of the xbox user
        application_path ([type]): The path of where the .exe or script is located.
    """
    os.system(application_path + "\\node-v14.17.0-win-x64\\node.exe " + application_path + "\\richpresence.js --u " + username + " --p " + password + " --xuid " + xuid)
    return

def main():
    client_id = '700853075023233024'
    RPC = Presence(client_id)
    RPC.connect()
    browsingStamp = time()
        
    if(readCredentials() == False or readCredentials()['email'] == ""):
        UserName = str(input("Email: "))
        Password = getpass()
        print("Get Xuid from https://www.cxkes.me/xbox/xuid. Make sure to select decimal.")
        xuid = str(input("Xuid: "))
        Credentials = {
            "email": UserName,
            "xuid": xuid
        }
        with open(application_path() + '\\credentials.json', 'w') as f:
            json.dump(Credentials, f)
        
    else:
        Password = getpass()
        UserName = readCredentials()['email']
        xuid = readCredentials()['xuid']
    # Gamer tags with # can just be removed
    
    sleep(5)
    
    while True:
        try:
            request(UserName, Password, xuid, application_path())
            if(readPresence() != None):
                rpc(RPC, "large", readPresence()['game'], "small", "Windows", readPresence()['state'],readPresence()['details'], browsingStamp)
            sleep(7)
        except Exception as e:
            print(e)
            sys.exit()
    

def readPresence():
    """Reads current presence data from rpc.json.

    Returns:
        JSON: Returns json from rpc.json or False.
    """
    with open(application_path() + '\\rpc.json') as f:
        data = json.load(f)
    if(data != None):
        return data
    else:
        return None
    
def readCredentials():
    """Reads credentials if any are set in .

    Returns:
        JSON: Returns JSON from credentials.json or False.
    """
    with open('credentials.json') as f:
        data = json.load(f)
    if(data != None):
        return data
    else:
        return False
    
def rpc(rpc:object, li:str, lt:str, si:str, st:str, state:str, details:str, startTimestamp:float):
    """Creates a rich presence setting. Will continuouls go on till an error occurs

    Args:
        rpc (object): Presence(client_id).connect()
        li (str): Large Image Key
        lt (str): Large Image Text
        si (str): Small Image Key
        st (str): Small Image Text
        state (str): Current state the user is in.
        details (str): Ussually the game details
        startTimestamp (float): A timer that starts when a new rpc is set.
    """
    try:
        rpc.update(
            large_image=li,
            large_text=lt,
            small_image=si,
            small_text=st,
            state=state,
            details=details,
            start=startTimestamp
        )
    except Exception as e:
        print(e)
        rpc.close()
        sys.exit()

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

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        print("Check to make sure discord and Halo Master Chief Collection are running.")
        sleep(5)
        sys.exit()
        