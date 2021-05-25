import json, auth, dictionary
from os import curdir, path, system
from time import time, sleep
from pypresence import Presence
from additional import application_path, clear


def request(application_path):
    """Generates a request in a terminal to receive the presence data

    Args:
        application_path (str): The path of where the .exe or script is located.
    """
    system(application_path + "\\node-v14.17.0-win-x64\\node.exe " + application_path + "\\richpresence.js")
    return

def main():
    """The main code need for the presence app to run
    """
    writejsonfile()
    
    client_id = {
        "main": "700853075023233024",
        "Halo R": "725163293240590386",
        "Halo CE": "725898626290942053",
        "Halo 2": "730097982523047936",
        "Halo 3": "748408159479005294",
        "Halo 4": "748413810548801587"
        }
    changedRPC = {
        "Else": "700853075023233024",
        "Halo R": False,
        "Halo CE": False,
        "Halo 2": False,
        "Halo 3": False,
        "Halo 4": False
        }
    currentRPC = startRPC(client_id['main'])
    currentRPC.connect()
    browsingStamp = timestamp()   
    while True:
        auth.main()
        try:
            request(application_path())
            presence = readPresence()
            if(presence != False and presence['game'] != ""):
                ## Halo 3
                if(presence['state'].find("H3:") != -1):
                    if(changedRPC['Halo 3'] == False):
                        if((changedRPC['Else'] or changedRPC['Halo CE'] or changedRPC['Halo 2'] or changedRPC['Halo 4']) != False):
                            currentRPC.close()
                            changedRPC['Halo CE'] = False
                            changedRPC['Halo 2'] = False
                            changedRPC['Halo R'] = False
                            changedRPC['Halo 4'] = False
                        currentRPC = startRPC(client_id['Halo 3'])
                        currentRPC.connect()
                        changedRPC['Else'] = False
                        changedRPC['Halo 3'] = client_id['Halo 3']
                        browsingStamp = timestamp()
                        rpc(currentRPC, dictionary.jsonDictionary(3)[presence['details']], presence['details'], dictionary.jsonDictionary(3)['Halo3'], presence['state'], presence['state'], presence['details'], browsingStamp)
                    else:                            
                        rpc(currentRPC, dictionary.jsonDictionary(3)[presence['details']], presence['details'], dictionary.jsonDictionary(3)['Halo3'], presence['state'], presence['state'], presence['details'], browsingStamp)
                
                elif(presence['state'].find("H4:") != -1):
                    if(changedRPC['Halo 4'] == False):
                        if((changedRPC['Else'] or changedRPC['Halo CE'] or changedRPC['Halo 2'] or changedRPC['Halo 4']) != False):
                            currentRPC.close()
                            changedRPC['Halo CE'] = False
                            changedRPC['Halo 2'] = False
                            changedRPC['Halo R'] = False
                            changedRPC['Halo 3'] = False
                        currentRPC = startRPC(client_id['Halo 4'])
                        currentRPC.connect()
                        changedRPC['Else'] = False
                        changedRPC['Halo 4'] = client_id['Halo 4']
                        browsingStamp = timestamp()
                        rpc(currentRPC, dictionary.jsonDictionary(4)[presence['details']], presence['details'], dictionary.jsonDictionary(4)['Halo4'], presence['state'], presence['state'], presence['details'], browsingStamp)
                    else:                            
                        rpc(currentRPC, dictionary.jsonDictionary(4)[presence['details']], presence['details'], dictionary.jsonDictionary(4)['Halo4'], presence['state'], presence['state'], presence['details'], browsingStamp)
                        
                elif(presence['state'].find("H: CE:") != -1):
                    if(changedRPC['Halo CE'] == False):
                        if((changedRPC['Else'] or changedRPC['Halo 4'] or changedRPC['Halo 2'] or changedRPC['Halo 4']) != False):
                            currentRPC.close()
                            changedRPC['Halo 4'] = False
                            changedRPC['Halo 2'] = False
                            changedRPC['Halo 3'] = False
                            changedRPC['Halo R'] = False
                            changedRPC['Else'] = False
                        currentRPC = startRPC(client_id['Halo CE'])
                        currentRPC.connect()
                        changedRPC['Halo CE'] = client_id['Halo CE']
                        browsingStamp = timestamp()
                        rpc(currentRPC, dictionary.jsonDictionary(1)[presence['details']], presence['details'], dictionary.jsonDictionary(1)['HaloCE'], presence['state'], presence['state'], presence['details'], browsingStamp)
                    else:                            
                        rpc(currentRPC, dictionary.jsonDictionary(1)[presence['details']], presence['details'], dictionary.jsonDictionary(1)['HaloCE'], presence['state'], presence['state'], presence['details'], browsingStamp)
                        
                elif(presence['state'].find("H2A: ") != -1):
                    if(changedRPC['Halo 2'] == False):
                        if((changedRPC['Else'] or changedRPC['Halo 4'] or changedRPC['Halo 2'] or changedRPC['Halo 4']) != False):
                            currentRPC.close()
                            changedRPC['Halo CE'] = False
                            changedRPC['Halo 4'] = False
                            changedRPC['Halo 3'] = False
                            changedRPC['Halo R'] = False
                            changedRPC['Else'] = False
                        currentRPC = startRPC(client_id['Halo 2'])
                        currentRPC.connect()
                        changedRPC['Halo 2'] = client_id['Halo 2']
                        browsingStamp = timestamp()
                        rpc(currentRPC, dictionary.jsonDictionary(2)['Halo2Aniversary'][presence['details']], presence['details'], dictionary.jsonDictionary(2)['Halo2Aniversary']['Halo2A'], presence['state'], presence['state'], presence['details'], browsingStamp)
                    else:                            
                        rpc(currentRPC, dictionary.jsonDictionary(2)['Halo2Aniversary'][presence['details']], presence['details'], dictionary.jsonDictionary(2)['Halo2Aniversary']['Halo2A'], presence['state'], presence['state'], presence['details'], browsingStamp)
                elif(presence['state'].find("H2: ") != -1):
                    if(changedRPC['Halo 2'] == False):
                        if((changedRPC['Else'] or changedRPC['Halo 4'] or changedRPC['Halo 2'] or changedRPC['Halo 4']) != False):
                            currentRPC.close()
                            changedRPC['Halo CE'] = False
                            changedRPC['Halo 4'] = False
                            changedRPC['Halo R'] = False
                            changedRPC['Halo 3'] = False
                            changedRPC['Else'] = False
                        currentRPC = startRPC(client_id['Halo 2'])
                        currentRPC.connect()
                        changedRPC['Halo 2'] = client_id['Halo 2']
                        browsingStamp = timestamp()
                        rpc(currentRPC, dictionary.jsonDictionary(2)['Halo2Classic'][presence['details']], presence['details'], dictionary.jsonDictionary(2)['Halo2Classic']['Halo2'], presence['state'], presence['state'], presence['details'], browsingStamp)
                    else:                            
                        rpc(currentRPC, dictionary.jsonDictionary(2)['Halo2Classic'][presence['details']], presence['details'], dictionary.jsonDictionary(2)['Halo2Classic']['Halo2'], presence['state'], presence['state'], presence['details'], browsingStamp)                        

                elif(presence['state'].find("H: R:") != -1):
                    if(changedRPC['Halo R'] == False):
                        if((changedRPC['Else'] or changedRPC['Halo 4'] or changedRPC['Halo 2'] or changedRPC['Halo 4']) != False):
                            currentRPC.close()
                            changedRPC['Halo CE'] = False
                            changedRPC['Halo 4'] = False
                            changedRPC['Halo 3'] = False
                            changedRPC['Else'] = False
                        currentRPC = startRPC(client_id['Halo R'])
                        currentRPC.connect()
                        changedRPC['Halo R'] = client_id['Halo R']
                        browsingStamp = timestamp()
                        rpc(currentRPC, dictionary.jsonDictionary(0)[presence['details']], presence['details'], dictionary.jsonDictionary(0)['HaloReach'], presence['state'], presence['state'], presence['details'], browsingStamp)
                    else:                            
                        rpc(currentRPC, dictionary.jsonDictionary(0)[presence['details']], presence['details'], dictionary.jsonDictionary(0)['HaloReach'], presence['state'], presence['state'], presence['details'], browsingStamp)
                else:
                    if(changedRPC['Else'] == False):
                        currentRPC.close()
                        changedRPC['Halo CE'] = False
                        changedRPC['Halo 2'] = False
                        changedRPC['Halo 3'] = False
                        changedRPC['Halo 4'] = False
                        currentRPC = startRPC(client_id['main'])
                        currentRPC.connect()
                        changedRPC['Else'] = client_id['main']
                        browsingStamp = timestamp()
                        rpc(currentRPC, "large", presence['game'], "small", "Windows", presence['state'], presence['details'], browsingStamp)
                    else:
                        rpc(currentRPC, "large", presence['game'], "small", "Windows", presence['state'], presence['details'], browsingStamp)
            else:
                print("Waiting for Halo Master Chief Collection to start.")
            sleep(7)
            clear()
        except KeyboardInterrupt or ValueError as e:
            print(e)
            currentRPC.close()
    

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

def timestamp():
    browsingStamp = time()
    return browsingStamp

def startRPC(client_id):
    RPC = Presence(client_id)
    RPC.connect()
    return RPC

def closeRPC(RPC):
    Presence(RPC).close()
        
def rpc(rpc:object, li:str, lt:str, si:str, st:str, state:str, details:str, startTimestamp:float):
    """Creates a rich presence setting. Will continuously go on till an error occurs

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
    
def writejsonfile():
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
    return

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        print("Check to make sure discord and Halo Master Chief Collection are running.")
        sleep(5)
        