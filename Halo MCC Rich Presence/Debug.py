from xbox.webapi.authentication.manager import AuthenticationManager
from xbox.webapi.common.exceptions import AuthenticationException
from xbox.webapi.api.client import XboxLiveClient
from pypresence.presence import Presence
import os,sys,time
def main():
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
    # discordRPC = Presence(discord_client_id)

    ## Discord RPC update loop

    while True:
        try:
            ##get current presence
            XboxPresence = xbl_client.presence.get_presence_own().json()
            currentlyOnline = False
            ##If we're online, do all this
            if (XboxPresence['state'] == 'Online'):
                OnlineDevices = XboxPresence['devices']
                for ActiveTitles in OnlineDevices:
                    # check if we're actually playing MCC
                    print("------------------------------------------------------------------------------------------------------------------------")
                    print("You're on " + ActiveTitles['type'])
                    if(ActiveTitles['titles'][0] != None):
                        print("Main Game: High Priority")
                        print("The ID: " + ActiveTitles['titles'][0]['id'])
                        print("The Name: " + ActiveTitles['titles'][0]['name'])
                        print("The Placement: " + ActiveTitles['titles'][0]['placement'])
                        print("The Current State: " + ActiveTitles['titles'][0]['state'])
                        print("Last Modified: " + ActiveTitles['titles'][0]['lastModified'])
                        print("------------------------------------------------------------------------------------------------------------------------")
                    print()
                    currentlyOnline = True
                    time.sleep(20)
            else:
                print("Get online")
                time.sleep(20)
                if(currentlyOnline == True):
                    sys.exit(0)
        except Exception as e:
                print(e)
                print("Crashed or received KeyboardInterrupt! Closing Discord RPC and shutting down script...")