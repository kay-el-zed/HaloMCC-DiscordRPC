from xbox.webapi.authentication.manager import AuthenticationManager
from xbox.webapi.common.exceptions import AuthenticationException
from xbox.webapi.api.client import XboxLiveClient
from pypresence.presence import Presence
import os,sys,time
def main():
    yn = str(input("Do you want the modify the discord RPC? y/n:"))
    if (yn == "y" or yn == "Y"):
        discord_client_id = int(input("Enter valid Client ID (Must be a Number): "))
        largeI = str(input("Enter Halo Image (Must be a Name): "))
        smallI = str(input("Enter Windows Image (Must be a Name): "))
        smallIM = str(input("Enter Xbox Image (Must be a Name): "))
    elif (yn == "n" or yn == "N"):
        discord_client_id = 700853075023233024
        largeI = "large"
        smallI = "small"
        smallIM = "xbox"
    else:
        print("Wrong input. Setting to default.")
        discord_client_id = 700853075023233024
        largeI = "large"
        smallI = "small"
        smallIM = "xbox"
    #xbox_status_last_change = None
    discord_online_status = False

    if discord_client_id == None:
        print("The discord_client_id variable is None. Update the script with a valid Discord client ID.\nGo to https://discordapp.com/developers to create an application for a Client ID.")
        time.sleep(5)
        sys.exit(0)
    if discord_client_id <= 0:
        print("That is not a valid id")
        time.sleep(5)
        sys.exit(0)
    
    try:
        xbox_token = os.getenv('LOCALAPPDATA') + "\\OpenXbox\\xbox\\tokens.json"
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
    ## Make the connection to XBL
    xbl_client = XboxLiveClient(auth_mgr.userinfo.userhash, auth_mgr.xsts_token.jwt, auth_mgr.userinfo.xuid)

    ## discord RPC init, PID is 13348
    discordRPC = Presence(discord_client_id)

    ## Discord RPC update loop

    while True:
        try:
            ##get current presence
            XboxPresence = xbl_client.presence.get_presence_own().json()
            # currentlyOnline = False
            ##If we're online, do all this
            if (XboxPresence['state'] == 'Online'):
                OnlineDevices = XboxPresence['devices']
                for ActiveTitles in OnlineDevices:
                    # check if we're actually playing MCC
                    print("------------------------------------------------------------------------------------------------------------------------")
                    print("You're on " + ActiveTitles['type'])
                    if(ActiveTitles['titles'][0] != None):
                        print("Main Game: High Priority (This game is the first you ran. Leave the program to switch game.)")
                        print("The ID: " + ActiveTitles['titles'][0]['id'])
                        print("The Name: " + ActiveTitles['titles'][0]['name'])
                        print("The Placement: " + ActiveTitles['titles'][0]['placement'])
                        print("The Current State: " + ActiveTitles['titles'][0]['state'])
                        print("Last Modified: " + ActiveTitles['titles'][0]['lastModified'])
                        print("------------------------------------------------------------------------------------------------------------------------")
                    ##set the current status
                    if ActiveTitles['titles'][0]['name'] == "Halo: The Master Chief Collection":
                        ##start Discord RPC
                        if discord_online_status == False:
                            print("Discord RPC not running. Starting!")
                            discordRPC.connect()
                            discord_online_status = True
                            browsingStamp = int(time.time())
                            print("Discord RPC Started")
                        try:
                            DiscordStatus = ActiveTitles['titles'][0]['activity']['richPresence'].split(" - ")
                            if(ActiveTitles['type'] == "Win32"):
                                discordRPC.update(large_image=largeI, large_text='Halo: MCC', small_image=smallI, small_text="Playing on PC", state=DiscordStatus[0], details=DiscordStatus[1], start=browsingStamp)
                                print("We're playing Halo on PC!")
                            elif(ActiveTitles['type'] == "XboxOne"):
                                discordRPC.update(large_image=largeI, large_text='Halo: MCC', small_image=smallIM, small_text="Playing on Xbox", state=DiscordStatus[0], details=DiscordStatus[1], start=browsingStamp)
                                print("We're playing Halo on Xbox One!")
                                # TODO:
                                # Maps Conditional statements
                                # if (discordRPC.update(details=DiscordStatus[1]) == "Anchor 9"):
                                #     discordRPC.update(large_image="")
                                #     time.sleep(15)
                        except Exception as e:
                            print(e)
                    time.sleep(20)
            else:
                print("You're not online on XBL at the moment.")
                if discord_online_status == True:
                    print("Closing Discord RPC Connection!")
                    discordRPC.close()
                    discord_online_status = False
                    sys.exit(0)
            time.sleep(5)
        except Exception as e:
            print(e)
            print("Crashed or received KeyboardInterrupt! Closing Discord RPC and shutting down script...")
            if discord_online_status == True:
                        print("Closing Discord RPC Connection!")
                        discordRPC.close()
                        discord_online_status == False
            time.sleep(5)
            sys.exit(0)