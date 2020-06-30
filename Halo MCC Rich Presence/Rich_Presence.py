from xbox.webapi.authentication.manager import AuthenticationManager
from xbox.webapi.common.exceptions import AuthenticationException
from xbox.webapi.api.client import XboxLiveClient
from pypresence.presence import Presence
import sys, time, os
import math, calendar, datetime
from time import mktime

def main():
    discord_client_id = 700853075023233024
    largeI = "large"
    smallI = "small"
    smallIM = "xbox"
    global discord_online_status
    discord_online_status = False

    if discord_client_id == None:
        print("The discord_client_id variable is None. Update the script with a valid Discord client ID.\nGo to https://discordapp.com/developers to create an application for a Client ID.")
        time.sleep(5)
        sys.exit(0)

    ## Handle XBL API authentication

    xboxApi()

    ## Make the connection to XBL
    xbl_client = XboxLiveClient(auth_mgr.userinfo.userhash, auth_mgr.xsts_token.jwt, auth_mgr.userinfo.xuid)

    ## discord RPC init, PID is 13348
    discordRPC = Presence(discord_client_id)

    ## Discord RPC update loop

    while True:
        try:
            ##get current presence
            XboxPresence = xbl_client.presence.get_presence_own().json()
            ##If we're online, do all this
            if (XboxPresence['state'] == 'Online'):
                OnlineDevices = XboxPresence['devices']
                for ActiveTitles in OnlineDevices:
                    if ActiveTitles['titles'][0]['name'] == "Halo: The Master Chief Collection":
                        ##start Discord RPC:
                        startRPC(discordRPC)
                        ##set the current status
                        try:
                            DiscordStatus = ActiveTitles['titles'][0]['activity']['richPresence'].split(" - ")
                            if(ActiveTitles['type'] == "Win32"):
                                discordRPC.update(large_image=largeI, large_text='Halo: MCC', small_image=smallI, small_text="Playing on PC", state=DiscordStatus[0], details=DiscordStatus[1], start=browsingStamp)
                            elif(ActiveTitles['type'] == "XboxOne"):
                                discordRPC.update(large_image=largeI, large_text='Halo: MCC', small_image=smallIM, small_text="Playing on Xbox", state=DiscordStatus[0], details=DiscordStatus[1], start=browsingStamp)
                            print("We're playing " + ActiveTitles['titles'][0]['name'] + " on " + ActiveTitles['type'])
                        except Exception as e:
                            print(e)
                            time.sleep(5)
                    ## This is for xbox users. For some reason home is set to default game.
                    elif ActiveTitles['titles'][1]['name'] == "Halo: The Master Chief Collection":
                        ##start Discord RPC:
                        startRPC(discordRPC)
                        ##set the current status
                        try:
                            DiscordStatus = ActiveTitles['titles'][1]['activity']['richPresence'].split(" - ")
                            if(ActiveTitles['type'] == "XboxOne"):
                                discordRPC.update(large_image=largeI, large_text='Halo: MCC', small_image=smallIM, small_text="Playing on Xbox", state=DiscordStatus[0], details=DiscordStatus[1], start=browsingStamp)
                            print("We're playing " + ActiveTitles['titles'][0]['name'] + " on " + ActiveTitles['type'])
                        except Exception as e:
                            print(e)
                            time.sleep(5)
                    else:
                        print("Not currently playing Halo: The Master Cheif Collection")
                time.sleep(5)
            else:
                closeRPC(discordRPC)
        except Exception as e:
            print(e)
            print("Crashed or received KeyboardInterrupt! Closing Discord RPC and shutting down script...")
            if discord_online_status == True:
                        print("Closing Discord RPC Connection!")
                        discordRPC.close()
                        discord_online_status == False
            time.sleep(5)
            sys.exit(0)



def startRPC(discordRPC):
    global browsingStamp
    global discord_online_status
    if discord_online_status == False:
        discord = Presence(discordRPC)
        print("Discord RPC not running. Starting!")
        discord_online_status = True
        browsingStamp = int(time.time())
        print("Discord RPC Started")
        return discord.connect()
    elif discord_online_status == True:
        discord = Presence(discordRPC)
        discord.close()
        print("Discord RPC not running. Starting!")
        discord_online_status = True
        browsingStamp = int(time.time())
        print("Discord RPC Started")
        return discordRPC.connect()
    
def closeRPC(discordRPC):
    global discord_online_status
    print("You're not online on XBL at the moment.")
    time.sleep(5)
    if discord_online_status == True:
        print("Closing Discord RPC Connection!")
        discordRPC.close()
        discord_online_status = False
        time.sleep(5)
        sys.exit(0)

def xboxApi():
    try:
        global xbox_token
        xbox_token = os.getenv('LOCALAPPDATA') + "\\OpenXbox\\xbox\\tokens.json"
        global auth_mgr 
        auth_mgr = AuthenticationManager.from_file(xbox_token)
    except FileNotFoundError as e:
        print(
        'Failed to load tokens from \'{}\'.\n'
        'ERROR: {}'.format(e.filename, e.strerror)
        )
        time.sleep(5)
        sys.exit(-1)
    try:
        auth_mgr.authenticate(do_refresh=True)
    except AuthenticationException as e:
        print('Authentication failed! Err: %s' % e)
        time.sleep(5)
        sys.exit(-1)
    return xbox_token, auth_mgr

# These Game Functions are very long and boring to read. To sum it up it checks to see if you can get the current map or current state.

def reach():
    # These Game Function
    print("W.I.P")

def ce():
    # These Game Function
    print("W.I.P")

def two():
    # These Game Function
    print("W.I.P")

def three():
    # These Game Function
    print("W.I.P")

def four():
    # These Game Function
    print("W.I.P")