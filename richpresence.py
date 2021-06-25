import json, auth, dictionary, math, requests, traceback

from requests.models import Response
from os import curdir, path, system, close
from time import time, sleep
from pypresence import Presence, presence
from additional import application_path, clear, startRPC, writejsonfile

def request(application_path):
    """Generates a request in a terminal to receive the presence data

    Args:
        application_path (str): The path of where the .exe or script is located.
    """
    with open(application_path + '\\tokens\\xtoken.json', 'r+') as f:
        data = json.load(f)
    
    displayclaims = data['DisplayClaims']['xui'][0]

    host_Url = f"https://peoplehub.xboxlive.com/users/me/people/xuids({ displayclaims['xid'] })/decoration/presenceDetail"
    headers = {
            'Authorization': f"XBL3.0 x={ displayclaims['uhs'] };{ data['Token'] }",
            'x-xbl-contract-version': '1',
            'Accept-Language': 'en-US'
            }
    r = requests.get(host_Url,headers=headers)
    if(r.status_code == 200):
        response = json.loads(r.text)['people'][0]
        print(r.status_code)
        print(f"Successful response:\n{ json.dumps(response['presenceDetails'], indent=2) }")
        i = 0
        while(i < len(response['presenceDetails'])):
            if("Halo: The Master Chief Collection - " in response['presenceDetails'][i]['PresenceText']):
                presenceText = response['presenceDetails'][i]['PresenceText'].split(" - ")
                presenceInfo = {
                    "device": response['presenceDetails'][i]['Device'],
                    "details": presenceText[2],
                    "state": presenceText[1],
                    "game": presenceText[0]
                }
                return presenceInfo
            else:
                i += 1
                presenceInfo = False
        return presenceInfo
    elif(r.status_code == 403):
        print("Invalid request. If the issue persists remove tokens and try again.")
        auth.main()
        request(application_path)
    elif(r.status_code == 401):
        print("Invalid token. Attempting to refresh token.")
        sleep(2)
        auth.main()
        sleep(1)
        request(application_path)
    else:
        print(f"Unable to complete request. Error {r.status_code}.\n{r.text}")
        return False

def richpresence(client_id, changedRPC, currentRPC, browsingStamp):
    """The main code need for the presence app to run
    """    
    while True:
        try:
            presence = request(application_path())
            steam_invite_url = steamInviteLink()
            if(presence != False and presence != "" and presence != None):
                if(presence['device'] == "Win32" or presence['device'] == "WindowsOneCore"):
                    if(presence['device'] == "Win32"):
                        deviceTitle = "Steam"
                        device = "steam"
                    elif(presence['device'] == "WindowsOneCore"):
                        deviceTitle = "Windows Store/Gamepass"
                        device = "small"
                    else:
                        deviceTitle = "Windows"
                        device = "small"
                elif(presence['device'] == "XboxOne"):
                    deviceTitle = "Xbox One"
                    device = "xbox"
                else:
                    device = "xbox"
                    deviceTitle = "Xbox"
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
                        if(steam_invite_url != ""):
                            rpc(currentRPC, dictionary.jsonDictionary(3)[presence['details']], presence['details'], dictionary.jsonDictionary(3)['Halo3'], presence['state'], presence['state'], presence['details'], browsingStamp, steam_invite_url)
                        else:
                            rpc(currentRPC, dictionary.jsonDictionary(3)[presence['details']], presence['details'], dictionary.jsonDictionary(3)['Halo3'], presence['state'], presence['state'], presence['details'], browsingStamp)
                    else:      
                        if(steam_invite_url != ""):
                            rpc(currentRPC, dictionary.jsonDictionary(3)[presence['details']], presence['details'], dictionary.jsonDictionary(3)['Halo3'], presence['state'], presence['state'], presence['details'], browsingStamp, steam_invite_url)
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
                        if(steam_invite_url != ""):
                            rpc(currentRPC, dictionary.jsonDictionary(4)[presence['details']], presence['details'], dictionary.jsonDictionary(4)['Halo4'], presence['state'], presence['state'], presence['details'], browsingStamp, steam_invite_url)
                        else:
                            rpc(currentRPC, dictionary.jsonDictionary(4)[presence['details']], presence['details'], dictionary.jsonDictionary(4)['Halo4'], presence['state'], presence['state'], presence['details'], browsingStamp)                    
                    else: 
                        if(steam_invite_url != ""):
                            rpc(currentRPC, dictionary.jsonDictionary(4)[presence['details']], presence['details'], dictionary.jsonDictionary(4)['Halo4'], presence['state'], presence['state'], presence['details'], browsingStamp, steam_invite_url)
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
                        if(steam_invite_url != ""):
                            rpc(currentRPC, dictionary.jsonDictionary(1)[presence['details']], presence['details'], dictionary.jsonDictionary(1)['HaloCE'], presence['state'], presence['state'], presence['details'], browsingStamp, steam_invite_url)
                        else:
                            rpc(currentRPC, dictionary.jsonDictionary(1)[presence['details']], presence['details'], dictionary.jsonDictionary(1)['HaloCE'], presence['state'], presence['state'], presence['details'], browsingStamp)
                    else:   
                        if(steam_invite_url != ""):
                            rpc(currentRPC, dictionary.jsonDictionary(1)[presence['details']], presence['details'], dictionary.jsonDictionary(1)['HaloCE'], presence['state'], presence['state'], presence['details'], browsingStamp, steam_invite_url)
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
                        if(steam_invite_url != ""):
                            rpc(currentRPC, dictionary.jsonDictionary(2)['Halo2Aniversary'][presence['details']], presence['details'], dictionary.jsonDictionary(2)['Halo2Aniversary']['Halo2A'], presence['state'], presence['state'], presence['details'], browsingStamp, steam_invite_url)
                        else:
                            rpc(currentRPC, dictionary.jsonDictionary(2)['Halo2Aniversary'][presence['details']], presence['details'], dictionary.jsonDictionary(2)['Halo2Aniversary']['Halo2A'], presence['state'], presence['state'], presence['details'], browsingStamp)
                    else:   
                        if(steam_invite_url != ""):
                            rpc(currentRPC, dictionary.jsonDictionary(2)['Halo2Aniversary'][presence['details']], presence['details'], dictionary.jsonDictionary(2)['Halo2Aniversary']['Halo2A'], presence['state'], presence['state'], presence['details'], browsingStamp, steam_invite_url)
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
                        if(steam_invite_url != ""):
                            rpc(currentRPC, dictionary.jsonDictionary(2)['Halo2Classic'][presence['details']], presence['details'], dictionary.jsonDictionary(2)['Halo2Classic']['Halo2'], presence['state'], presence['state'], presence['details'], browsingStamp, steam_invite_url)
                        else:
                            rpc(currentRPC, dictionary.jsonDictionary(2)['Halo2Classic'][presence['details']], presence['details'], dictionary.jsonDictionary(2)['Halo2Classic']['Halo2'], presence['state'], presence['state'], presence['details'], browsingStamp)
                    else: 
                        if(steam_invite_url != ""):
                            rpc(currentRPC, dictionary.jsonDictionary(2)['Halo2Classic'][presence['details']], presence['details'], dictionary.jsonDictionary(2)['Halo2Classic']['Halo2'], presence['state'], presence['state'], presence['details'], browsingStamp, steam_invite_url)
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
                        if(steam_invite_url != ""):
                            rpc(currentRPC, dictionary.jsonDictionary(0)[presence['details']], presence['details'], dictionary.jsonDictionary(0)['HaloReach'], presence['state'], presence['state'], presence['details'], browsingStamp, steam_invite_url)
                        else:
                            rpc(currentRPC, dictionary.jsonDictionary(0)[presence['details']], presence['details'], dictionary.jsonDictionary(0)['HaloReach'], presence['state'], presence['state'], presence['details'], browsingStamp)
                    else:  
                        if(steam_invite_url != ""):
                            rpc(currentRPC, dictionary.jsonDictionary(0)[presence['details']], presence['details'], dictionary.jsonDictionary(0)['HaloReach'], presence['state'], presence['state'], presence['details'], browsingStamp, steam_invite_url)
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
                        if(steam_invite_url != ""):
                            rpc(currentRPC, "large", presence['game'], device, deviceTitle, presence['state'], presence['details'], browsingStamp, steam_invite_url)
                        else:
                            rpc(currentRPC, "large", presence['game'], device, deviceTitle, presence['state'], presence['details'], browsingStamp)
                    else:
                        if(steam_invite_url != ""):
                            rpc(currentRPC, "large", presence['game'], device, deviceTitle, presence['state'], presence['details'], browsingStamp, steam_invite_url)
                        else:
                            rpc(currentRPC, "large", presence['game'], device, deviceTitle, presence['state'], presence['details'], browsingStamp)    
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


def closeRPC(RPC):
    Presence(RPC).close()
        
def rpc(rpc:object, li:str, lt:str, si:str, st:str, state:str, details:str, startTimestamp:float, buttonUrl = None):
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
        if(buttonUrl != None):
            rpc.update(
                large_image=li,
                large_text=lt,
                small_image=si,
                small_text=st,
                state=state,
                details=details,
                start=startTimestamp,
                buttons=[{
                    "label": "Join Game",
                    "url": buttonUrl
                }]
            )
        else:
            rpc.update(
                large_image=li,
                large_text=lt,
                small_image=si,
                small_text=st,
                state=state,
                details=details,
                start=startTimestamp,
            )
            
    except KeyboardInterrupt or Exception as e:
        print(e)
        rpc.close()



def steamInviteLink():
    with open(application_path() + "\\rpc.json", "r") as f:
        data = json.load(f)
    if(data['steamid']):
        steamid = data['steamid']
    else:
        steamid = ""
    if(steamid != ""):
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        try:
            print("Getting steam url code:")
            r = requests.get(f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=80EC429274AF252714363656B71562C0&format=json&steamids={steamid}", headers=headers)
            response = json.loads(r.text)
            if(type(response) == dict):
                lobbysteamid = response['response']['players'][0]['lobbysteamid']
                gameid = response['response']['players'][0]['gameid']
                steam_invite_url = "steam://joinlobby/" + gameid + "/" + lobbysteamid + "/" + steamid
                print(steam_invite_url)
                return steam_invite_url
            else:
                print("It appears steam services aren't making requests, or you haven't started steam, or that the game isn't running on steam.")
        except Exception as e:
            print("Unable to get steam id. Check to make sure Halo is running.")
            print(e)
            sleep(5)
            steam_invite_url = None
            return steam_invite_url
    else:
        print("Steam url is None.")
        steam_invite_url = None
        return steam_invite_url
    
 
if __name__ == '__main__':
    try:
        if(path.exists(application_path() + '\\rpc.json') != True):
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
        richpresence(client_id, changedRPC, currentRPC, browsingStamp)

    except Exception as e:
        print(e)
        print(traceback.format_exc())
        print("Check to make sure discord and Halo Master Chief Collection are running.")
        sleep(5)
