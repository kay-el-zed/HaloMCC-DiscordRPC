from xbox.webapi.authentication.manager import AuthenticationManager
from xbox.webapi.common.exceptions import AuthenticationException
from xbox.webapi.api.client import XboxLiveClient
from pypresence import Presence
import sys, time

discord_client_id = 655596739138551848

## Handle XBL API authentication.
try:
  auth_mgr = AuthenticationManager.from_file('C:/Users/toxic/AppData/Local/OpenXbox/xbox/tokens.json')
except FileNotFoundError as e:
  print(
    'Failed to load tokens from \'{}\'.\n'
    'ERROR: {}'.format(e.filename, e.strerror)
  )
  sys.exit(-1)

try:
  auth_mgr.authenticate(do_refresh=True)
except AuthenticationException as e:
  print('Authentication failed! Err: %s' % e)
  sys.exit(-1)
## Make the connection to XBL
xbl_client = XboxLiveClient(auth_mgr.userinfo.userhash, auth_mgr.xsts_token.jwt, auth_mgr.userinfo.xuid)

## discord RPC init 
discordRPC = Presence(discord_client_id)
discordRPC.connect()
discordRPC.update(large_image='cover', large_text='Halo: MCC',
           small_image='win10', small_text="Playing on PC")


## Discord RPC update loop
while True:
    try:
        XboxPresence = xbl_client.presence.get_presence_own().json()
        print ("Current Presence: ", XboxPresence)
        time.sleep(15)
    except:
        RPC.close()
        sys.exit(0)
