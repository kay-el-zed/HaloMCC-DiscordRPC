import json
from os import sys, path, system
from time import time, sleep
from pypresence import Presence
from getpass import getpass
from additional import application_path, clear
import auth


def request(application_path):
    """Generates a request in a terminal to receive the presence data

    Args:
        username (str): The email of the user
        password (str): The password of the user
        xuid (str): The id of the xbox user
        application_path ([type]): The path of where the .exe or script is located.
    """
    system(application_path + "\\node-v14.17.0-win-x64\\node.exe " + application_path + "\\richpresence.js")
    return

def main():
    """The main code need for the presence app to run
    """
    client_id = '700853075023233024'
    try:
        RPC = Presence(client_id)
        RPC.connect()
        browsingStamp = time()
    except FileNotFoundError as e:
        print("Discord is not currently running")
        print(e)
    if(path.isfile(application_path() + '\\rpc.json') != True):
        open("rpc.json", "x")
        
    with open("rpc.json", "w") as f:
        activity = {
            "details": "",
            "state": "",
            "device": "",
            "game": ""
        }
        f.write(json.dumps(activity))
        
    while True:
        auth.main()
        try:
            request(application_path())
            if(readPresence() != False and readPresence()['game'] != ""):
                rpc(RPC, "large", readPresence()['game'], "small", "Windows", readPresence()['state'],readPresence()['details'], browsingStamp)
            else:
                print("Waiting for Halo Master Chief Collection to start.")
            sleep(7)
            clear()
        except KeyboardInterrupt or ValueError as e:
            print(e)
            RPC.close()
            sys.exit()
    

def readPresence():
    """Reads current presence data from rpc.json.

    Returns:
        JSON: Returns json from rpc.json or False.
    """
    if(path.exists(application_path() + '\\rpc.json')):
        with open(application_path() + '\\rpc.json') as f:
            data = json.load(f)

        if(data != None):
            return data
        else:
            return None
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
    except KeyboardInterrupt or Exception as e:
        print(e)
        rpc.close()
        exit()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        print("Check to make sure discord and Halo Master Chief Collection are running.")
        sleep(5)
        try:
            rpc.close()
        except Exception as f:
            print("Rich Presence client either never started or can't be shut down.")
        exit()
        