import json, auth, dictionary, math, requests, traceback

from requests.models import Response
from os import curdir, path, system, close
from time import time, sleep
from pypresence import Presence, presence
from additional import application_path, clear, startRPC, writejsonfile

def request(application_path):
    """Generates a request in a terminal to receive the presence data
    
    What is required to make such a request:
    
    Get request to: https://peoplehub.xboxlive.com/users/me/people/xuids(the xuid)/decoration/presenceDetail
    
    Headers: "Accept: application/json", "Accept-Language: en-US", "x-xbl-contract-version: 4", "Authorization: XBL3.0 x=<userhash>;<XSTSToken>
    
    Args:
        application_path (str): The path of where the .exe or script is located.
    """
    with open(application_path + '\\tokens\\xtoken.json', 'r+') as f:
        data = json.load(f)
    
    display_claims = data['DisplayClaims']['xui'][0]

    host_Url = f"https://peoplehub.xboxlive.com/users/me/people/xuids({display_claims['xid']})/decoration/presenceDetail"
    headers = {
            'Authorization': f"XBL3.0 x={display_claims['uhs']};{data['Token']}",
            'x-xbl-contract-version': '4',
            'Accept-Language': 'en-US',
            'Accept' : 'application/json'
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
        print(f"Invalid request. If the issue persists remove tokens and try again.\n{r.text}")
        auth.main()
        request(application_path)
    elif(r.status_code == 401):
        print(f"Invalid token. Attempting to refresh token.\n{r.text}")
        sleep(2)
        auth.main()
        sleep(1)
        request(application_path)
    else:
        print(f"Unable to complete request. Error {r.status_code}.\n{r.text}")
        return False

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
        request(application_path())
    except Exception as e:
        print(e)
        sleep(5)
