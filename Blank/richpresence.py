import json
import os
from os import sys
from time import time
from pypresence import Presence


def main():
    client_id = '700853075023233024'
    RPC = Presence(client_id)
    RPC.connect()
    browsingStamp = int(time())
    while True:
        try:
            os.system(os.path.dirname(os.path.abspath(__file__)) + "\\node-v14.17.0-win-x64\\node.exe richpresence.js --u <UserName> --p <Password>")
            rpc(RPC, "large", readPresence()['game'], "small", "Windows", readPresence()['state'],readPresence()['details'], browsingStamp)
        except Exception as e:
            print(e)
            sys.exit(-1)
    

def readPresence():
    with open('rpc.json') as f:
        data = json.load(f)
    if(data != None):
        return data
    else:
        return None
    
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
        sys.exit(1)

if __name__ == '__main__':
    main()